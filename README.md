# Document AI Assistant

A full-stack GenAI application that lets investors and equity analysts query Vietnamese financial reports in natural language and get grounded, citable answers with supporting source passages and multi-year financial analysis.

## The client

**Vietnamese Equity Research System** — a fictional Vietnamese equity research platform for investors and securities analysts.

Analysts spend a significant amount of time manually copying financial data from annual reports and financial statements into spreadsheets, calculating multi-year growth rates, and comparing companies before they can perform original analysis based on growth-investing principles such as CANSLIM.

The goal of this project is to reduce that repetitive financial-data and document-analysis workload while keeping answers grounded in the source documents.

## Core requirements

The assistant should:

- Answer questions about Vietnamese companies and financial reports in the corpus
- Analyze financial performance across multiple years
- Identify multi-year growth trends and calculate relevant financial metrics
- Evaluate documented evidence related to CANSLIM investing factors
- Cite the source report and page
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
northstar-vietnamese-equity-research-ai/
├── AGENTS.md
├── README.md
├── data/
│   └── download.py
├── docs/
│   ├── client-brief.md
│   └── guides/
├── backend/
└── frontend/