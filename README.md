# Automation Workflows

This repository contains automated workflows that streamline business processes, reduce manual work, and improve efficiency using modern automation and AI tools.

---

## Tools

[![n8n](https://img.shields.io/badge/n8n-%23FFFFFF?style=for-the-badge&logo=n8n&logoColor=white)](https://n8n.io)
[![Make](https://img.shields.io/badge/Make.com-%23FFFFFF?style=for-the-badge&logo=make&logoColor=white)](https://www.make.com)
[![Typeform](https://img.shields.io/badge/Typeform-%23FFFFFF?style=for-the-badge&logo=typeform&logoColor=white)](https://www.typeform.com)
[![HubSpot](https://img.shields.io/badge/HubSpot-%23FFFFFF?style=for-the-badge&logo=hubspot&logoColor=white)](https://www.hubspot.com)
[![Slack](https://img.shields.io/badge/Slack-%23FFFFFF?style=for-the-badge&logo=slack&logoColor=white)](https://slack.com)
[![Google](https://img.shields.io/badge/Google-%23FFFFFF?style=for-the-badge&logo=google&logoColor=white)](https://ai.google)
[![Gmail](https://img.shields.io/badge/Gmail-%23FFFFFF?style=for-the-badge&logo=gmail&logoColor=white)](https://mail.google.com)
[![Airtable](https://img.shields.io/badge/Airtable-%23FFFFFF?style=for-the-badge&logo=airtable&logoColor=white)](https://airtable.com)
[![Notion](https://img.shields.io/badge/Notion-%23FFFFFF?style=for-the-badge&logo=notion&logoColor=white)](https://www.notion.so)
[![Google Drive](https://img.shields.io/badge/Google_Drive-%23FFFFFF?style=for-the-badge&logo=googledrive&logoColor=white)](https://drive.google.com)

---

## Workflows

### IT Helpdesk Ticket Auto-Router

- Automates ticket intake, prioritization, HubSpot ticket creation, Slack alerts, and AI confirmation emails.
- **Result:** No manual sorting, instant P1 alerts, clean CRM data.
- **Flow:** `Typeform → n8n → HubSpot → Slack → Gemini → Gmail`

### Client Onboarding

- Automates HubSpot contacts, Notion pages, welcome emails, Slack notifications, and Drive folders from Airtable.
- **Result:** Full onboarding in <30s, consistent setup.
- **Flow:** `Airtable → HubSpot → Notion → Gemini → Gmail → Slack → Drive`

### Expense Approval

- Employees submit expenses via Typeform, AI flags anomalies, managers approve in Slack, and employees get instant emails.
- **Result:** Zero email chains, instant approvals, full audit trail.
- **Flow:** `Typeform → n8n → Gemini → Airtable → Slack → Webhook → Gmail`

---

## Benefits

- Saves time & reduces errors
- Instant notifications & approvals
- Clean, consistent records
- Scalable, AI-enhanced automation
