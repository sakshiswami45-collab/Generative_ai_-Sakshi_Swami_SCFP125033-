from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.environ["GROQ_API_KEY"])

SYSTEM_PROMPT = """
You are a professional language translator.
Translate the given sentence into the requested target language.
Follow the requested formality level.

Formal: Use respectful, professional language.
Informal: Use casual, friendly, everyday language.
Neutral: Use natural, standard language.

Preserve the original meaning.
Do not add explanations or extra information.
Return only the translated sentence.
"""

user_prompt = """
Sentence: {sentence}
Target language: {target_language}
Formality: {formality}

Translate the sentence according to the requested formality.
Return only the translated sentence.
"""

sentence = input("Enter sentence: ")
target_language = input("Enter target language: ")
formality = input("Enter formality (Formal/Informal/Neutral): ")

user_message = user_prompt.format(
    sentence=sentence,
    target_language=target_language,
    formality=formality
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

print("\n--- TRANSLATED SENTENCE ---")
print(response)
