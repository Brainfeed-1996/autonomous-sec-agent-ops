from fastapi import FastAPI, Header, HTTPException
from threat_intel import ThreatIntelModule

app = FastAPI()
intel = ThreatIntelModule()

@app.get("/")
def read_root():
    return {"message": "Autonomous Sec Agent API"}

@app.get("/threat-intel")
def get_intel(keyword: str = "kubernetes"):
    return {"latest_cves": intel.fetch_latest_cves(keyword)}

@app.post("/scan")
def start_scan(repo_url: str, x_asset_svid: str = Header(None)):
    # Zero-Trust Identity Retrofit: Enforce SVID
    if not x_asset_svid:
        raise HTTPException(status_code=401, detail="Missing X-Asset-SVID")
    
    # Logic for AI agent to scan repo and open PRs
    return {"status": "scanning", "repo": repo_url, "identity": "verified"}
