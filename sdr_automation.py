from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, function_tool
from dotenv import load_dotenv

import os
import asyncio

import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

load_dotenv()


@function_tool
def send_html_email(subject: str, html_body: str) -> dict[str, str]:
    """ Send out an email with the given subject and HTML body to all sales prospects """
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email(os.getenv("FROM_EMAIL"))
    to_email = To(os.getenv("TO_EMAIL"))
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content).get()
    sg.client.mail.send.post(request_body=mail)
    
    return {"status": "success"}


gemini_client = AsyncOpenAI(
    base_url=os.getenv("GEMINI_BASE_URL"),
    api_key=os.getenv("GEMINI_API_KEY")
)
gemini_model = OpenAIChatCompletionsModel(os.getenv("GEMINI_MODEL_NAME"), gemini_client)

company_background = open("system-prompts/company_background.md").read()
casual_sales_system_prompt = open("system-prompts/casual_sales_agent.md", encoding="utf-8").read().format(company_background=company_background)
engaging_sales_system_prompt = open("system-prompts/engaging_sales_agent.md").read().format(company_background=company_background)
busy_sales_system_prompt = open("system-prompts/busy_sales_agent.md").read().format(company_background=company_background)
sales_manager_system_prompt = open("system-prompts/sales_manager_agent.md").read().format(company_background=company_background)


busy_sales_agent = Agent(
    name="Busy Sales Agent",
    instructions=busy_sales_system_prompt,
    model=gemini_model,
).as_tool("busy_sales_agent", "Busy sales cold email writer")

casual_sales_agent = Agent(
    name="Casual Sales Agent",
    instructions=casual_sales_system_prompt,
    model=gemini_model,
).as_tool("casual_sales_agent", "Casual sales cold email writer")

engaging_sales_agent = Agent(
    name="Engaging Sales Agent",
    instructions=engaging_sales_system_prompt,
    model=gemini_model,
).as_tool("engaging_sales_agent", "Engaging sales cold email writer")


sales_manager = Agent(
    name="Sales Manager",
    instructions=sales_manager_system_prompt,
    model=gemini_model,
    tools=[casual_sales_agent, engaging_sales_agent, busy_sales_agent]
)


message = "Write a cold email showcasing our product to a CTO of a company"
result = Runner.run_sync(sales_manager, message)
