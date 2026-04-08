# Automation Workflows

This repository contains automated workflows that streamline business processes, reduce manual work, and improve efficiency using modern automation and AI tools.

---

## Tools

<a href="https://n8n.io"><img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/n8n.svg" alt="n8n" height="30"/></a>
<a href="https://www.make.com"><img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/make.svg" alt="Make.com" height="30"/></a>
<a href="https://www.typeform.com"><img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/typeform.svg" alt="Typeform" height="30"/></a>
<a href="https://www.hubspot.com"><img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/hubspot.svg" alt="HubSpot" height="30"/></a>
<a href="https://slack.com"><img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/slack.svg" alt="Slack" height="30"/></a>
<a href="https://ai.google"><img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/google.svg" alt="Google Gemini" height="30"/></a>
<a href="https://mail.google.com"><img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/gmail.svg" alt="Gmail" height="30"/></a>
<a href="https://airtable.com"><img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/airtable.svg" alt="Airtable" height="30"/></a>
<a href="https://www.notion.so"><img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/notion.svg" alt="Notion" height="30"/></a>
<a href="https://drive.google.com"><img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/googledrive.svg" alt="Google Drive" height="30"/></a>

[![n8n](https://img.shields.io/badge/n8n-automation-blue?style=for-the-badge)](https://n8n.io)
[![Make](https://img.shields.io/badge/Make.com-automation-blue?style=for-the-badge)](https://www.make.com)
[![Typeform](https://img.shields.io/badge/Typeform-forms-blue?style=for-the-badge)](https://www.typeform.com)
[![HubSpot](https://img.shields.io/badge/HubSpot-CRM-blue?style=for-the-badge)](https://www.hubspot.com)
[![Slack](https://img.shields.io/badge/Slack-chat-blue?style=for-the-badge)](https://slack.com)
[![Google Gemini](https://img.shields.io/badge/Google_Gemini-AI-blue?style=for-the-badge)](https://ai.google)
[![Gmail](https://img.shields.io/badge/Gmail-email-blue?style=for-the-badge)](https://mail.google.com)
[![Airtable](https://img.shields.io/badge/Airtable-database-blue?style=for-the-badge)](https://airtable.com)
[![Notion](https://img.shields.io/badge/Notion-docs-blue?style=for-the-badge)](https://www.notion.so)
[![Google Drive](https://img.shields.io/badge/Google_Drive-storage-blue?style=for-the-badge)](https://drive.google.com)

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
