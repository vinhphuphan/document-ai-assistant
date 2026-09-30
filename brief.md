# Brief — Northstar AI

## Summary

**Northstar AI** is a fictional independent investment research firm with ~40 analysts. They sell deep equity research to institutional clients such as hedge funds, mutual funds, and pension funds under annual subscriptions, along with custom research and analyst calls.

They do not manage money themselves. Their product is research and access to their analysts.

## How Northstar makes money

- Each analyst covers ~15 US public companies in a specific industry.
- Analysts produce research reports, financial models, and stock-level recommendations.
- Clients pay for access to the research and the ability to speak with analysts.
- Reputation is critical. A single bad call can damage the firm's credibility.

## How they add value

Portfolio managers do not have enough time to read every 10-K, 10-Q, earnings transcript, and industry filing for the companies they follow.

Northstar's analysts do that work for them and turn thousands of pages of information into concise, actionable research.

The core value is **condensation**: turning large volumes of source material into a clear thesis that a portfolio manager can act on.

## The problem

Each analyst spends roughly **half of every week** on source-document intake:

- Opening SEC filings
- Finding relevant sections such as Risk Factors, MD&A, and Business Segments
- Copying and comparing passages
- Reviewing year-over-year changes

Only after completing this work can they begin their original analysis.

This work is:

- Boring
- Necessary
- Repetitive across analysts
- The biggest constraint on analyst productivity

Hiring more analysts does not solve the problem because the document-intake workload grows with the amount of coverage.

## What they want

An internal chatbot called **Document AI Assistant** that allows analysts to:

- Ask questions in plain English about documents in Northstar's curated corpus
- Get answers grounded in the source documents
- Cite the specific filing and page
- View the supporting passage
- Use the system from a browser
- Sign in with their Northstar email address
- View their own conversation history

## Example analyst questions

The initial sample corpus contains 10-K filings for Apple, Amazon, Alphabet, Microsoft, and NVIDIA across fiscal years 2021–2025.

The assistant should handle questions such as:

1. How did Apple's revenue mix between iPhone, Services, Mac, iPad, and Wearables change from 2021 to 2025?
2. How did Amazon's AWS operating income and margin compare with North America and International from 2021 to 2025?
3. How did NVIDIA describe demand drivers, customer concentration, and supply constraints for its Data Center business from 2021 to 2025?
4. What changed in Microsoft's description of Azure, AI infrastructure, and cloud capacity constraints from 2021 to 2025?
5. How did Alphabet's revenue trends differ across Google Search, YouTube ads, Google Network, subscriptions/platforms/devices, and Google Cloud?
6. Which companies changed their risk-factor language around AI, cloud infrastructure, export controls, supply-chain concentration, or regulation between 2021 and 2025?
7. What do Apple's and NVIDIA's filings say about supplier concentration and dependence on third-party manufacturing, and how did this language change over time?
8. How did capital expenditures and purchase commitments compare across Microsoft, Alphabet, Amazon, and NVIDIA?
9. What are the most important geographic revenue exposures disclosed in each company's latest 10-K?
10. Do the filings provide evidence that generative AI improved margins for any of these companies? Where should the assistant refuse to infer beyond the available evidence?

## Trust requirements

Northstar is a research firm, so **accuracy and traceability are critical**.

The assistant must:

- Never invent facts
- Only answer from the configured document corpus
- Cite the source filing and page for factual claims
- Show the underlying passage used to support the answer
- Say when the available evidence is insufficient

A confident but unsupported answer is worse than no answer.

## Constraints

- **Corpus:** SEC 10-K and 10-Q filings for S&P 500 companies, 2020–2025
- **Source:** SEC EDGAR
- **Users:** ~40 analysts plus a few partners
- **Authentication:** Northstar email addresses; no SSO required
- **Hosting:** Small/medium cloud footprint
- **Infrastructure:** No dedicated infrastructure team

## Out of scope

- Trading recommendations or stock picks
- External data sources such as news, social media, or alternative data
- Analysis not grounded in the document corpus
- Multi-tenant or multi-client support
- Billing, plans, or paywalls
- Mobile applications

## Definition of done

A pilot group of **5 senior analysts** uses the assistant for one week.

The project is considered successful if they report saving at least **3 hours per analyst per week**.

If the pilot meets this goal, Northstar will consider rolling the system out to the wider firm.
