from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.environ["GROQ_API_KEY"])

SYSTEM_PROMPT = """
You classify customer reviews into one category.
Use only these categories: Positive, Negative, Neutral.

Positive: The customer is satisfied or praises the product or service.
Negative: The customer complains or expresses dissatisfaction.
Neutral: The review is factual or has no clear positive or negative opinion.

Return only one category label.
Do not explain your answer.
"""

user_prompt = """
Customer review: {review_text}

Classify this review.
Return only one label: Positive, Negative, or Neutral.
"""

review_text = input("Please enter customer review: ")

user_message = user_prompt.format(
    review_text=review_text
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

print("\n--- REVIEW CLASSIFICATION ---")
print(response)
