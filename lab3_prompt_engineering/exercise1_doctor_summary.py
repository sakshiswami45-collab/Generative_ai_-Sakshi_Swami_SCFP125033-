
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.environ["GROQ_API_KEY"])

SYSTEM_PROMPT = """
You convert raw consultation notes into a concise clinical summary.
Use only information present in the notes.
Do not invent symptoms or diagnoses.
If information is missing, write 'Not mentioned in notes'.
Always use these sections:
1. Symptoms
2. Diagnosis
3. Recommendation
Include only recommendations documented in the notes.
"""

user_prompt = """
Patient name: {patient_name}
Patient clinical notes: {clinical_notes}

Generate a summary using exactly these sections:

1. Symptoms:
2. Diagnosis:
3. Recommendation:
"""

patient_name = input("Please enter patient name: ")
clinical_notes = input("Please enter clinical notes: ")

user_message = user_prompt.format(
    patient_name=patient_name,
    clinical_notes=clinical_notes
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

response = chat_comp.choices[0].message.content

print("\n--- DOCTOR SUMMARY ---")
print("Patient Name:", patient_name)
print(response)
