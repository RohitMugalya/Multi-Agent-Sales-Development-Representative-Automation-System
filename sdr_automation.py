from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, function_tool
from dotenv import load_dotenv
import os

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

