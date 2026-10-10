from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.environ["GROQ_API_KEY"])

SYSTEM_PROMPT = """
You are a customer support representative.
Write polite, friendly, professional, and empathetic replies.
Keep the same tone for every customer.
Address the customer's concern clearly.
Do not make promises or invent company policies.
Follow the requested maximum word limit.
Return only the customer support reply.
"""

user_prompt = """
Company name: {company_name}
Customer message: {customer_message}

Write a customer support reply on behalf of {company_name}.
The reply must not exceed {max_words} words.
Use a polite, friendly, professional, and empathetic tone.
Return only the reply.
"""

customer_message = input("Enter customer message: ")
company_name = input("Enter company name: ")
max_words = int(input("Enter maximum word limit: "))

user_message = user_prompt.format(
    customer_message=customer_message,
    company_name=company_name,
    max_words=max_words
)

message = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    },
    {
        "role": "user",
        "content": user_message
    },
]

chat_comp = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=message,
    temperature=0
)

response = chat_comp.choices[0].message.content.strip()

words = response.split()

if len(words) > max_words:
    response = " ".join(words[:max_words])

print("\n--- CUSTOMER SUPPORT REPLY ---")
print(response)
