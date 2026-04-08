# Automation Workflows

This repository contains automated workflows that streamline business processes, reduce manual work, and improve efficiency using modern automation and AI tools.

---

## Tools

<a href="https://n8n.io"><img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/n8n.svg" alt="n8n" height="30" style="filter: brightness(0) invert(1);"/></a>
<a href="https://www.make.com"><img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/make.svg" alt="Make.com" height="30" style="filter: brightness(0) invert(1);"/></a>
<a href="https://www.typeform.com"><img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/typeform.svg" alt="Typeform" height="30" style="filter: brightness(0) invert(1);"/></a>
<a href="https://www.hubspot.com"><img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/hubspot.svg" alt="HubSpot" height="30" style="filter: brightness(0) invert(1);"/></a>
<a href="https://slack.com"><img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/slack.svg" alt="Slack" height="30" style="filter: brightness(0) invert(1);"/></a>
<a href="https://ai.google"><img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/google.svg" alt="Google Gemini" height="30" style="filter: brightness(0) invert(1);"/></a>
<a href="https://mail.google.com"><img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/gmail.svg" alt="Gmail" height="30" style="filter: brightness(0) invert(1);"/></a>
<a href="https://airtable.com"><img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/airtable.svg" alt="Airtable" height="30" style="filter: brightness(0) invert(1);"/></a>
<a href="https://www.notion.so"><img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/notion.svg" alt="Notion" height="30" style="filter: brightness(0) invert(1);"/></a>
<a href="https://drive.google.com"><img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/googledrive.svg" alt="Google Drive" height="30" style="filter: brightness(0) invert(1);"/></a>

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
