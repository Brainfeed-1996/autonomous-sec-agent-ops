# ADR 006: LLM Reasoning Engine for Security RCA

## Status
Accepted

## Context
Automated scanning finds vulnerabilities but lacks the context for deep mitigation and root cause identification.

## Decision
Integrate an LLM-based Reasoning Engine using LangChain and GPT-4. The engine will perform Root Cause Analysis (RCA) and generate structured mitigation strategies.

## Consequences
- Better quality findings for developers.
- Dependency on external LLM APIs (OpenAI).
