import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_email(email_text):
    prompt = f"""
    Classify this email into:
    Urgent / Request / Info / Spam

    Email:
    {email_text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()


def generate_reply(email_text):
    prompt = f"""
    Write a professional reply.

    Context:
    - You are a college coordinator
    - Keep it concise and formal

    Email:
    {email_text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()