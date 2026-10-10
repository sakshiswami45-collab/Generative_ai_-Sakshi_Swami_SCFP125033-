from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.environ["GROQ_API_KEY"])

SYSTEM_PROMPT = """
You are a content editor.
Revise the given draft to fix only the specified issue.
Preserve the original meaning and important information.
Do not introduce unrelated changes.
Return only the revised draft.
"""

user_prompt = """
Original draft:
{draft_text}

Issue to fix:
{issue_to_fix}

This is revision round {round_number} of 3.

Fix the specified issue while preserving the original meaning.
Improve the draft based on the same issue in each round.
Return only the revised draft.
"""

draft_text = input("Enter your draft text: ")
issue_to_fix = input("Enter the specific issue to fix: ")

for round_number in range(1, 4):
    user_message = user_prompt.format(
        draft_text=draft_text,
        issue_to_fix=issue_to_fix,
        round_number=round_number
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

    draft_text = chat_comp.choices[0].message.content.strip()

    print(f"\n--- ROUND {round_number} ---")
    print(draft_text)

print("\n--- FINAL REVISED DRAFT ---")
print(draft_text)
