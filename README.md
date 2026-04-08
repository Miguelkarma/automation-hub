# ⚡ Automation Workflows

This repo contains automated workflows that streamline business processes, reduce manual work, and improve efficiency using modern automation and AI tools.

---

## 🛠 Tools

n8n · Make.com · Typeform · HubSpot · Slack · Google Gemini AI · Gmail · Airtable · Notion · Google Drive

---

## 📂 Workflows

### 1. IT Helpdesk Ticket Auto-Router

- Automates ticket intake, prioritization, HubSpot ticket creation, Slack alerts, and AI confirmation emails.
- **Result:** No manual sorting, instant P1 alerts, clean CRM data.
- **Flow:** `Typeform → n8n → HubSpot → Slack → Gemini → Gmail`

### 2. Client Onboarding

- Automates HubSpot contacts, Notion pages, welcome emails, Slack notifications, and Drive folders from Airtable.
- **Result:** Full onboarding in <30s, consistent setup.
- **Flow:** `Airtable → HubSpot → Notion → Gemini → Gmail → Slack → Drive`

### 3. Expense Approval

- Employees submit expenses via Typeform, AI flags anomalies, managers approve in Slack, and employees get instant emails.
- **Result:** Zero email chains, instant approvals, full audit trail.
- **Flow:** `Typeform → n8n → Gemini → Airtable → Slack → Webhook → Gmail`

---

## ⚡ Benefits

- Saves time & reduces errors
- Instant notifications & approvals
- Clean, consistent records
- Scalable, AI-enhanced automation
