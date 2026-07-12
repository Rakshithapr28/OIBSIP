import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


SYSTEM_PROMPT = """
You are an Intent Detection AI.

Your job is NOT to answer the user's question.

Your job is to identify the user's intent and return ONLY valid JSON.

Supported intents:

1. greeting
2. weather
3. reminder
4. send_email
5. search_web
6. general_question
7. exit

Examples:

User: Hello
Output:
{
    "intent":"greeting"
}

User: What's the weather in Bangalore?
Output:
{
    "intent":"weather",
    "city":"Bangalore"
}

User: Remind me after 15 minutes
Output:
{
    "intent":"reminder",
    "minutes":15
}

User: Search Python tutorials
Output:
{
    "intent":"search_web",
    "query":"Python tutorials"
}

User: Who is APJ Abdul Kalam?
Output:
{
    "intent":"general_question",
    "question":"Who is APJ Abdul Kalam?"
}

User: Exit
Output:
{
    "intent":"exit"
}

Return ONLY JSON.
"""


def detect_intent(user_input):

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=f"{SYSTEM_PROMPT}\n\nUser: {user_input}"
    )

    return json.loads(response.text)