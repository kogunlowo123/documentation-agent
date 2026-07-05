# Documentation Agent

[![CI](https://github.com/kogunlowo123/documentation-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/documentation-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Software Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Automated documentation generator that produces API references, architecture diagrams, onboarding guides, changelogs, and inline documentation from source code analysis with automatic staleness detection and update suggestions.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `generate_api_docs` | Generate OpenAPI/Swagger documentation from source code |
| `generate_architecture_diagram` | Generate architecture diagram from codebase analysis |
| `generate_changelog` | Generate changelog from git commit history |
| `detect_stale_docs` | Find documentation that is out of sync with code |
| `generate_onboarding_guide` | Generate developer onboarding documentation |
| `generate_docstrings` | Generate docstrings for undocumented functions |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/docs/api` | Generate API documentation |
| `POST` | `/api/v1/docs/architecture` | Generate architecture diagrams |
| `POST` | `/api/v1/docs/changelog` | Generate changelog |
| `POST` | `/api/v1/docs/onboarding` | Generate onboarding guide |
| `POST` | `/api/v1/docs/staleness` | Detect stale documentation |
| `POST` | `/api/v1/docs/docstrings` | Generate inline documentation |

## Features

- Api Docs
- Architecture Diagrams
- Changelog Generation
- Staleness Detection
- Onboarding Guides

## Integrations

- Github Connector
- Gitlab Connector
- Confluence
- Notion Connector

## Architecture

```
documentation-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── documentation_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 6 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 6 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 4 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**LLM + Source Analysis + Diagram Generation**

---

Built as part of the Enterprise AI Agent Platform.
