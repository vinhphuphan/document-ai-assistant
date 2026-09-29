# Northstar Document AI Assistant

A full-stack GenAI application that lets analysts query financial filings in natural language and get grounded, citable answers with supporting source passages.

## The client

**Northstar AI** — a fictional independent investment research firm with ~40 analysts.

Analysts spend a significant amount of time reading 10-Ks and 10-Qs, finding relevant sections, and comparing disclosures across years before they can perform original analysis.

The goal of this project is to reduce that document-intake workload while keeping answers grounded in the source documents.

## Core requirements

The assistant should:

- Answer questions about documents in the corpus
- Cite the source filing and page
- Show the supporting passage
- Refuse when the answer is not supported by the corpus
- Support authenticated users and conversation history

## Stack

| Layer | Choice |
| --- | --- |
| Backend | Python + FastAPI |
| Frontend | React + TypeScript + Vite |
| Database | Supabase Postgres |
| Retrieval | `pgvector` + PostgreSQL full-text search |
| Auth | Supabase Auth |
| ORM / Migrations | SQLAlchemy + Alembic |
| LLM + Embeddings | OpenAI |
| Hosting | Railway |

## Prerequisites

Install these before setting up `backend/` or `frontend/`:

| Tool | Version | Used for | Install |
| ---- | ------- | -------- | ------- |
| [Python](https://www.python.org/downloads/) | 3.12+ | Backend runtime | OS package manager or python.org |
| [uv](https://docs.astral.sh/uv/getting-started/installation/) | latest | Backend deps + `data/download.py` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| [Node.js](https://nodejs.org/) | 20+ (LTS) | Frontend toolchain | nodejs.org or `nvm install --lts` |
| [pnpm](https://pnpm.io/installation) | latest | Frontend package manager | `corepack enable && corepack prepare pnpm@latest --activate` |

You also need accounts/keys for external services once the app is wired up. 
## Repo layout

```text
northstar-document-ai-assistant/
├── AGENTS.md
├── README.md
├── data/
│   └── download.py
├── docs/
│   ├── client-brief.md
│   └── guides/
├── backend/
└── frontend/
