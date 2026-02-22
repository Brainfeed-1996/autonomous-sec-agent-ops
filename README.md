# 🤖 Autonomous Security Agent Ops

[![Python](https://img.shields.io/badge/Language-Python-3776AB.svg)](https://www.python.org)
[![LangChain](https://img.shields.io/badge/AI-LangChain-121212.svg)](https://langchain.com)
[![DevSecOps](https://img.shields.io/badge/Role-DevSecOps-blueviolet.svg)]()

An AI-powered platform (LangChain/AutoGPT style) that monitors GitHub repositories for vulnerabilities and automatically opens Pull Requests with security fixes.

## Architecture
- **Agentic Core**: LangChain-based agents for vulnerability scanning and remediation.
- **Verification Engine**: Automated testing of proposed security fixes.
- **Web Dashboard**: Real-time visibility into agent activities.

## SRE/Monitoring
- Agent performance metrics (tokens used, success rate).
- Health checks for the backend and verification engine.

## ADR
- [ADR-001: LangChain for Agentic Orchestration](docs/adr/001-langchain-agents.md)
- [ADR-002: Docker-in-Docker for Safe Fix Verification](docs/adr/002-dind-verification.md)
