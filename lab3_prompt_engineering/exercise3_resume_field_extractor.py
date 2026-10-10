from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()
client = Groq(api_key=os.environ["GROQ_API_KEY"])

SYSTEM_PROMPT = """
You extract requested fields from resume text.
Return only valid JSON.
Extract only the fields requested by the user.
Use only information present in the resume.
Do not invent or guess missing information.
If a requested field is missing, use an empty string.
Use the exact requested field names as JSON keys.
Do not include markdown or explanations.
"""

user_prompt = """
Resume text:
{resume_text}

Fields to extract:
{fields_to_extract}

Return a valid JSON object containing only the requested fields.
"""

resume_text = input("Please enter resume text: ")
fields_input = input("Enter fields to extract (comma-separated): ")

fields_to_extract = [
    field.strip() for field in fields_input.split(",")
    if field.strip()
]

user_message = user_prompt.format(
    resume_text=resume_text,
    fields_to_extract=", ".join(fields_to_extract)
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

try:
    extracted_data = json.loads(response)
    print("\n--- EXTRACTED RESUME FIELDS ---")
    print(json.dumps(extracted_data, indent=2))
except json.JSONDecodeError:
    print("Invalid JSON response received:")
    print(response)
