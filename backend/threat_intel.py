import requests
from datetime import datetime

class ThreatIntelModule:
    def __init__(self):
        self.nvd_url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

    def fetch_latest_cves(self, keyword="kubernetes"):
        """Pulls recent CVEs from NVD for prioritization."""
        try:
            params = {
                "keywordSearch": keyword,
                "pubStartDate": datetime.now().strftime("%Y-%m-%dT00:00:00.000"),
                "resultsPerPage": 5
            }
            # Note: In production, use API Key and respect rate limits
            response = requests.get(self.nvd_url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return self._parse_cves(data)
            return []
        except Exception as e:
            print(f"Error fetching threat intel: {e}")
            return []

    def _parse_cves(self, data):
        cve_list = []
        for item in data.get("vulnerabilities", []):
            cve = item.get("cve", {})
            cve_id = cve.get("id")
            metrics = cve.get("metrics", {}).get("cvssMetricV31", [{}])[0].get("cvssData", {})
            score = metrics.get("baseScore", 0.0)
            cve_list.append({
                "id": cve_id,
                "score": score,
                "severity": metrics.get("baseSeverity", "UNKNOWN")
            })
        return sorted(cve_list, key=lambda x: x['score'], reverse=True)

    def prioritize_fixes(self, detected_vulns):
        """Cross-references detected vulnerabilities with real-time threat intel."""
        intel = self.fetch_latest_cves()
        intel_ids = {c['id']: c for c in intel}
        
        prioritized = []
        for vuln in detected_vulns:
            priority = "MEDIUM"
            if vuln['id'] in intel_ids:
                if intel_ids[vuln['id']]['score'] >= 9.0:
                    priority = "CRITICAL (THREAT INTEL CONFIRMED)"
                elif intel_ids[vuln['id']]['score'] >= 7.0:
                    priority = "HIGH"
            
            vuln['priority'] = priority
            prioritized.append(vuln)
            
        return sorted(prioritized, key=lambda x: x.get('score', 0), reverse=True)
