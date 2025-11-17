# Multi Agent Sales Development Representative Automation System

![Agent Workflow Diagram](path/to/your/workflow-diagram.png)

An intelligent, AI-powered sales automation system that uses multiple specialized agents to craft personalized cold emails based on recipient profiles and sales intent.

## Features

- **Multi-Agent Architecture**: Sales Manager orchestrates three specialized writing agents (Casual, Engaging, Busy) that adapt to different recipient personas
- **End-to-End Automation**: From intent analysis to HTML formatting and email delivery
- **Intelligent Subject Lines**: Dedicated agent optimizes for open rates
- **Professional Formatting**: Clean, distraction-free HTML optimized for B2B outreach
- **SendGrid Integration**: Direct email delivery with API automation

## Prerequisites

- Python 3.8+
- [uv package manager](https://docs.astral.sh/uv/getting-started/installation/) - Fast Python package installer
- OpenAI-compatible API access (configured for Gemini)
- SendGrid account and API key

## Installation

1. Install `uv` if you haven't already:  
Visit official uv installation [page](https://docs.astral.sh/uv/getting-started/installation/)


2. Clone and navigate to the project:
```bash
git clone https://github.com/RohitMugalya/Multi-Agent-Sales-Development-Representative-Automation-System
cd Multi-Agent-Sales-Development-Representative-Automation-System
```

3. Install dependencies:
```bash
uv sync
```

4. Configure `.env` file:
```env
GEMINI_BASE_URL=<your-gemini-base-url>
GEMINI_API_KEY=<your-gemini-api-key>
GEMINI_MODEL_NAME=<your-model-name>
SENDGRID_API_KEY=<your-sendgrid-api-key>
FROM_EMAIL=<sender-email-address>
TO_EMAIL=<recipient-email-address>
```

## Project Structure

```
.
├── sdr_automation.py                # Main entry point
├── .env                             # Environment variables
└── system-prompts/
    ├── company_background.md        # Company information
    ├── casual_sales_agent.md        # Casual writing style
    ├── engaging_sales_agent.md      # Engaging writing style
    ├── busy_sales_agent.md          # Concise professional style
    ├── sales_manager_agent.md       # Orchestration logic
    └── subject_writer_agent.md      # Subject line generation
```

## Usage

1. Run the application:
```bash
uv run sdr_automation.py
```

2. Describe your intent and target:
```
Describe your intent and the target recipient role: 
Reaching out to CTOs at mid-sized SaaS companies about our API security solution
```

3. The system automatically:
   - Selects the appropriate writing style
   - Generates the email body and subject line
   - Converts to professional HTML
   - Sends via SendGrid

## Configuration

### Company Background
Edit `system-prompts/company_background.md` with your company's value proposition, products, target market, and unique selling points.

### Agent Customization (Optional)
Modify system prompt files to adjust agent behavior and writing styles for your specific needs.

## How It Works

**Input** → **Sales Manager** (analyzes & selects agent) → **Sales Agent** (writes body) → **Emailer Agent** (formats & sends)

The Sales Manager delegates to the most appropriate writing agent based on your target recipient, then hands off to the Emailer Agent which coordinates subject generation, HTML conversion, and delivery.

## Environment Variables

| Variable | Description |
|----------|-------------|
| `GEMINI_BASE_URL` | Gemini API endpoint |
| `GEMINI_API_KEY` | Gemini authentication key |
| `GEMINI_MODEL_NAME` | Model identifier |
| `SENDGRID_API_KEY` | SendGrid API key |
| `FROM_EMAIL` | Sender email address |
| `TO_EMAIL` | Recipient email address |