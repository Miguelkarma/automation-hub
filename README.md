# Automation Hub

A collection of business process automations and AI-assisted workflows built with n8n and Make. The projects cover operations, customer onboarding, research, recruiting, finance, IT support, and CRM pipeline management.

## Projects

| Project | What it automates | Platform |
| --- | --- | --- |
| [AI Job Search Tracker & Job Matching Automation](./AI%20Job%20Search%20Tracker%20%26%20Job%20Matching%20Automation/) | Captures job listings from Gmail alerts or a browser extension, extracts structured details with AI, and saves or updates them in Airtable. | n8n |
| [Client Onboarding Automation](./Client%20Onboarding%20Automation/) | Turns a new Airtable client record into a coordinated onboarding process across HubSpot, Google Sheets, Gmail, Slack, and Google Drive. | Make |
| [Company Profile Enrichment Agent](./Company%20Profile%20Enrichment%20Agent/) | Scrapes and extracts company information with Firecrawl, enriches it with external data, and emails the completed result. | n8n |
| [Expense Approval Workflow](./Expense%20Approval%20Workflow/) | Receives expense submissions, uses AI to flag anomalies, records decisions in Airtable, and handles approval notifications. | n8n |
| [IT Helpdesk Ticket Auto-Router](./IT%20Helpdesk%20Ticket%20Auto-Router/) | Classifies support requests by priority, manages HubSpot contacts and tickets, alerts Slack for urgent cases, and emails AI-written confirmations. | n8n |
| [Research AI Agent](./Research%20AI%20Agent/) | Monitors Valorant updates on a schedule, checks past research logs, summarizes new information, emails a report, and records the result in Google Sheets. | n8n |
| [Zoho CRM Pipeline Recovery Automation](./Zoho%20Crm%20Pipeline%20Recovery%20Automation/) | Finds stale deals, generates follow-ups, creates CRM tasks and Gmail drafts, routes them for review, and sends approved messages. | n8n |

## Workflow Details

### AI Job Search Tracker & Job Matching Automation

Two complementary workflows create a single Airtable-based job tracker:

- **Gmail Job Alerts to Airtable** parses incoming job-alert emails with Gemini and upserts the extracted listings.
- **Job One-Click Saver to Airtable** receives pages captured by the included Chrome extension, extracts job details, checks for duplicates, and creates or updates the matching record.

`Gmail / Chrome extension -> n8n -> Gemini -> Airtable`

### Client Onboarding Automation

Watches Airtable for new clients, creates or updates their HubSpot contact, adds a tracking row in Google Sheets, creates a Drive folder, and sends welcome and internal Slack notifications. Gemini helps generate personalized content.

`Airtable -> Make -> HubSpot -> Google Sheets -> Gemini -> Gmail -> Slack -> Google Drive`

### Company Profile Enrichment Agent

Uses Firecrawl to scrape and extract structured company data, supplements the profile with external API data, waits for asynchronous extraction when needed, and emails the finished result.

`Manual trigger -> Firecrawl -> external API -> n8n -> Gmail`

### Expense Approval Workflow

The submission workflow captures Typeform responses, uses Gemini to assess the expense, stores it in Airtable, and initiates the approval request. A separate webhook handler processes the decision, updates the record, and emails the employee.

`Typeform -> n8n -> Gemini -> Airtable -> approval webhook -> Gmail`

### IT Helpdesk Ticket Auto-Router

Receives Typeform tickets, assigns P1, P2, or P3 priority, maintains the requester in HubSpot, and creates the appropriate ticket. Urgent requests trigger a Slack alert, while Gemini produces tailored email confirmations for every priority.

`Typeform -> n8n -> HubSpot -> Slack -> Gemini -> Gmail`

### Research AI Agent

A scheduled AI agent checks for new Valorant updates, consults previous logs in Google Sheets to avoid repeating research, generates a summary using Gemini and Groq, sends it by email, and appends the latest result to the log.

`Schedule -> n8n AI agent -> Gemini / Groq -> Google Sheets -> Gmail`

### Zoho CRM Pipeline Recovery Automation

The first workflow identifies inactive Zoho CRM deals, calculates their age, generates a suggested follow-up with Groq, creates a Zoho task and note, saves a Gmail draft, and requests review in Discord. The second workflow checks reviewed items, sends approved drafts, updates their status, and reports successes or failures in Discord.

`Schedule -> Zoho CRM -> n8n AI agent -> Groq -> Gmail drafts -> review -> Discord`

## Tools and Integrations

![n8n](https://img.shields.io/badge/n8n-workflow_automation-EA4B71?style=flat-square)
![Make](https://img.shields.io/badge/Make-workflow_automation-6D00CC?style=flat-square)
![Gemini](https://img.shields.io/badge/Google_Gemini-AI-4285F4?style=flat-square)
![Groq](https://img.shields.io/badge/Groq-AI-F55036?style=flat-square)
![Airtable](https://img.shields.io/badge/Airtable-database-18BFFF?style=flat-square)
![HubSpot](https://img.shields.io/badge/HubSpot-CRM-FF7A59?style=flat-square)
![Zoho CRM](https://img.shields.io/badge/Zoho_CRM-CRM-E42527?style=flat-square)
![Gmail](https://img.shields.io/badge/Gmail-email-EA4335?style=flat-square)
![Google Sheets](https://img.shields.io/badge/Google_Sheets-data-34A853?style=flat-square)
![Google Drive](https://img.shields.io/badge/Google_Drive-storage-4285F4?style=flat-square)
![Slack](https://img.shields.io/badge/Slack-notifications-4A154B?style=flat-square)
![Discord](https://img.shields.io/badge/Discord-notifications-5865F2?style=flat-square)
![Typeform](https://img.shields.io/badge/Typeform-forms-262627?style=flat-square)
![Firecrawl](https://img.shields.io/badge/Firecrawl-web_data-FF4C01?style=flat-square)

## Using the Workflows

1. Open the folder for the project you want to use.
2. Import `.json` workflows into n8n or the `.blueprint.json` file into Make.
3. Create the credentials required by the workflow's integrations.
4. Review trigger settings, record IDs, field mappings, webhook URLs, recipients, and prompts before activating the workflow.
5. Run a test with sample data, then enable the trigger or schedule.

The workflow files are templates. You will need to connect your own accounts and adapt IDs, fields, and business rules to your environment. Never commit API keys, access tokens, webhook secrets, or exported credentials.

## Utilities

- `sanitize-n8n-flow.py` removes sensitive values from exported n8n workflows before they are committed.
- `sanitize-make-blueprint.py` removes sensitive values from exported Make blueprints before they are committed.
