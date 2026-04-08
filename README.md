# Automation Workflows

This repository contains automated workflows that streamline business processes, reduce manual work, and improve efficiency using modern automation and AI tools.

---

## Tools

[![n8n](https://cdn.worldvectorlogo.com/logos/n8n.svg)](https://n8n.io)
[![Make.com](https://cdn.worldvectorlogo.com/logos/make-1.svg)](https://www.make.com)
[![Typeform](https://cdn.worldvectorlogo.com/logos/typeform.svg)](https://www.typeform.com)
[![HubSpot](https://cdn.worldvectorlogo.com/logos/hubspot.svg)](https://www.hubspot.com)
[![Slack](https://cdn.worldvectorlogo.com/logos/slack-new-logo.svg)](https://slack.com)
[![Google Gemini](https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2023_logo.svg)](https://ai.google)
[![Gmail](https://cdn.worldvectorlogo.com/logos/gmail-icon.svg)](https://mail.google.com)
[![Airtable](https://cdn.worldvectorlogo.com/logos/airtable.svg)](https://airtable.com)
[![Notion](https://cdn.worldvectorlogo.com/logos/notion.svg)](https://www.notion.so)
[![Google Drive](https://cdn.worldvectorlogo.com/logos/google-drive-1.svg)](https://drive.google.com)

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
