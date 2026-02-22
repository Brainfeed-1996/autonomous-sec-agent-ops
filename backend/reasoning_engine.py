import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

class MitigationStep(BaseModel):
    step: int
    action: str
    description: str

class RCAnalysis(BaseModel):
    vulnerability_id: str
    root_cause: str
    impact_analysis: str
    cvss_score: float = Field(..., description="CVSS v3.1 base score")
    severity: str = Field(..., description="Critical, High, Medium, or Low")
    theoretical_poc: str = Field(..., description="A detailed theoretical Proof of Concept demonstrating exploitability")
    mitigation_strategy: List[MitigationStep]

class ReasoningEngine:
    def __init__(self, model_name="gpt-4-turbo-preview"):
        self.llm = ChatOpenAI(model=model_name, temperature=0)
        self.parser = PydanticOutputParser(pydantic_object=RCAnalysis)

    def perform_rca(self, vulnerability_data: str) -> RCAnalysis:
        prompt = ChatPromptTemplate.from_template(
            "You are an expert Security Engineer performing Root Cause Analysis (RCA).\n"
            "Analyze the following vulnerability and provide a structured breakdown including "
            "the root cause, technical impact, and a multi-step mitigation plan.\n\n"
            "Vulnerability Data:\n{data}\n\n"
            "{format_instructions}"
        )
        
        format_instructions = self.parser.get_format_instructions()
        input_data = prompt.format_messages(
            data=vulnerability_data,
            format_instructions=format_instructions
        )
        
        response = self.llm.invoke(input_data)
        return self.parser.parse(response.content)

# Integration Example (Internal)
if __name__ == "__main__":
    engine = ReasoningEngine()
    # Dummy data for demonstration
    vuln = "SQL Injection in user profile search via 'username' parameter in search.php."
    analysis = engine.perform_rca(vuln)
    print(analysis.json(indent=2))
