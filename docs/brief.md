# Client Brief — Vietnamese Equity Research System

## The client

**Vietnamese Equity Research System** is a fictional independent Vietnamese equity research platform for investors and securities analysts. They provide structured financial research on Vietnamese public companies, focusing on company fundamentals, multi-year financial performance, and growth-investing analysis based on the CANSLIM framework.

Their product is research, financial analysis, and an AI-powered research assistant that helps analysts reduce repetitive document and spreadsheet work.

## How Northstar makes money

- Each analyst covers a selected group of Vietnamese public companies across different industries.
- Analysts produce research reports, financial analysis, financial models, and company-level investment research.
- Clients pay for access to the research and analytical tools.
- Research quality and data accuracy are critical because financial analysis depends on reliable and traceable information.

## How they add value

Investors and analysts do not have enough time to manually read every annual report, financial statement, and company disclosure for the companies they follow.

Northstar's analysts collect and analyze this information, compare financial performance across multiple years, and turn large volumes of financial data into concise, structured research.

The core value is **automation and condensation**: turning large volumes of source material and repetitive spreadsheet work into clear financial evidence that analysts can use for further investment research.

## The problem

Each analyst spends significant time on repetitive financial-data intake and analysis:

- Opening annual reports and financial statements
- Finding relevant financial figures and disclosures
- Copying financial data into spreadsheets
- Calculating year-over-year growth rates
- Comparing financial performance across four or more years
- Checking whether companies demonstrate consistent growth
- Reviewing factors related to the CANSLIM investing framework

Only after completing this work can they begin their original analysis.

This work is:

- Boring
- Necessary
- Repetitive across analysts
- Time-consuming
- Prone to copy-paste and calculation errors
- A significant constraint on analyst productivity

Repeating the same process every year does not solve the problem because the document-intake and financial-analysis workload grows with the number of companies being covered.

## What they want

An internal AI research assistant called **Equity Research AI Assistant** that allows analysts to:

- Ask questions in plain English or Vietnamese about companies and financial reports in Northstar's curated corpus
- Get answers grounded in the source documents
- Compare financial performance across multiple years
- Calculate and explain relevant financial growth metrics
- Identify evidence related to CANSLIM investing factors
- Cite the specific report and page
- View the supporting passage
- Use the system from a browser
- Sign in with their Northstar email address
- View their own conversation history

## Example analyst questions

The initial sample corpus contains annual reports and financial statements for FPT, VCB, HPG, MWG, and VIC across fiscal years 2021–2025.

The assistant should handle questions such as:

1. How did FPT's revenue and net profit change from 2021 to 2025?
2. Has FPT demonstrated consistent revenue and earnings growth over the last four years?
3. What were the year-over-year growth rates of HPG's revenue and net profit from 2022 to 2025?
4. How did MWG's business performance change across the 2021–2025 period?
5. How did VCB's profitability and asset growth change from 2021 to 2025?
6. What were the major changes in VIC's business performance and financial position across the five-year period?
7. Which companies in the corpus show consistent multi-year growth in revenue, earnings, or other selected financial metrics?
8. What evidence in the reports is relevant to the CANSLIM factors for a selected company?
9. What do the annual reports say about a company's earnings growth, new products or business developments, management, and other factors relevant to growth-investing research?
10. Where does the available financial data provide insufficient evidence to evaluate a particular CANSLIM factor, and where should the assistant refuse to infer beyond the available evidence?

## Trust requirements

Northstar is an equity research platform, so **accuracy and traceability are critical**.

The assistant must:

- Never invent financial facts
- Only answer from the configured document corpus
- Calculate financial metrics deterministically where possible
- Cite the source report and page for factual claims
- Show the underlying passage used to support the answer
- Say when the available evidence is insufficient
- Distinguish reported financial facts from AI-generated interpretation

A confident but unsupported answer is worse than no answer.

## Constraints

- **Corpus:** Vietnamese annual reports and financial statements for selected Vietnamese public companies, 2021–2025
- **Initial companies:** FPT, VCB, HPG, MWG, VIC
- **Source:** Vietstock-hosted Vietnamese public-company reports
- **Users:** Equity analysts and investment researchers
- **Authentication:** Northstar email addresses; no SSO required
- **Hosting:** Small/medium cloud footprint
- **Infrastructure:** No dedicated infrastructure team

## Out of scope

- Automated trading
- Direct buy/sell recommendations
- Portfolio management
- External data sources such as news, social media, or alternative data
- Analysis not grounded in the document corpus
- Multi-tenant or multi-client support
- Billing, plans, or paywalls
- Mobile applications
- Replacing human investment decisions

## Definition of done

A pilot group of **5 equity analysts** uses the assistant for one week.

The project is considered successful if they report saving at least **3 hours per analyst per week** on financial-document intake, spreadsheet preparation, and repetitive multi-year financial analysis.

If the pilot meets this goal, Northstar will consider expanding the system to additional Vietnamese public companies and wider research workflows.