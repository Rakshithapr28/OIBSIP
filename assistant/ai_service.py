import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

SYSTEM_PROMPT = """
You are the AI Brain of a Voice Assistant.

Your task is to understand the user's request and return ONLY valid JSON.

There are two types of requests:

-------------------------------------------------
1. Conversation
-------------------------------------------------

If the user is chatting, greeting, introducing themselves,
sharing feelings, celebrating something, thanking you,
or asking a general question that doesn't require a Python module,
respond like this:

{
    "intent":"conversation",
    "response":"Your natural conversational response."
}

Examples:

User: Hello

{
    "intent":"conversation",
    "response":"Hello Sagar! How can I help you today?"
}

User: Good Morning

{
    "intent":"conversation",
    "response":"Good morning Sagar! I hope you have a wonderful day."
}

User: Today is my birthday

{
    "intent":"conversation",
    "response":"Happy Birthday, Sagar! 🎉 I hope you have an amazing day filled with happiness."
}

User: Thank you

{
    "intent":"conversation",
    "response":"You're most welcome, Sagar!"
}

User: Who are you?

{
    "intent":"conversation",
    "response":"I am your AI Voice Assistant. I'm here to help you with information, tasks, and conversations."
}

-------------------------------------------------
2. Action Requests
-------------------------------------------------

If the user wants you to perform an action,
return ONLY the required parameters.

Weather

{
    "intent":"weather",
    "city":"Bangalore"
}

Reminder

{
    "intent":"reminder",
    "minutes":15
}

Send Email

{
    "intent":"send_email",
    "recipient":"Rahul",
    "message":"I'll be late."
}

Search Web

{
    "intent":"search_web",
    "query":"Python tutorials"
}

Exit

{
    "intent":"exit"
}

Rules:

1. Always return valid JSON.
2. Never return Markdown.
3. Never return explanations.
4. Never return code blocks.
5. Return ONLY JSON.
"""


def detect_intent(user_input):
    """
    Detect the user's intent using Gemini AI.
    """

    try:

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=f"{SYSTEM_PROMPT}\n\nUser: {user_input}"
        )

        text = response.text.strip()

        # Remove markdown code blocks if Gemini returns them
        if text.startswith("```"):
            text = text.replace("```json", "").replace("```", "").strip()

        return json.loads(text)

    except json.JSONDecodeError:
        print("JSON Parsing Error")

        return {
            "intent": "conversation",
            "response": "Sorry Sagar, I received an invalid response from my AI service."
        }

    except Exception as e:
        print(f"Gemini Error: {e}")

        return {
            "intent": "conversation",
            "response": "Sorry Sagar, I'm unable to contact my AI service right now. Please try again in a few moments."
        }