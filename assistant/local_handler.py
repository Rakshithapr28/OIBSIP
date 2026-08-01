import re


def handle_local_command(user_input):
    """
    Detect commands that can be handled locally.
    Returns intent_data if matched, otherwise None.
    """

    text = user_input.lower().strip()

    # ---------------------------------
    # Exit
    # ---------------------------------
    if text in ["exit", "quit", "bye", "goodbye"]:
        return {
            "intent": "exit"
        }

    # ---------------------------------
    # Time
    # ---------------------------------
    if any(word in text for word in [
        "time",
        "current time",
        "what time",
        "tell me the time"
    ]):
        return {
            "intent": "time"
        }

    # ---------------------------------
    # Date
    # ---------------------------------
    if any(word in text for word in [
        "date",
        "today's date",
        "current date",
        "what is today's date"
    ]):
        return {
            "intent": "date"
        }

    # ---------------------------------
    # Open Website
    # ---------------------------------
    websites = [
        "youtube",
        "google",
        "github",
        "gmail",
        "linkedin"
    ]

    for site in websites:
        if "open" in text and site in text:
            return {
                "intent": "open_website",
                "website": site
            }

    # ---------------------------------
    # Open Application
    # ---------------------------------
    apps = {
        "notepad": "notepad",
        "calculator": "calculator",
        "paint": "paint",
        "chrome": "chrome",
        "vs code": "vs code",
        "visual studio code": "vs code",
        "command prompt": "command prompt",
        "cmd": "command prompt",
        "powershell": "powershell"
    }

    for key, value in apps.items():
        if "open" in text and key in text:
            return {
                "intent": "open_application",
                "application": value
            }

    # ---------------------------------
    # Weather
    # ---------------------------------
    if "weather" in text:

        match = re.search(r"weather (?:in|at)?\s*(.*)", text)

        if match:
            city = match.group(1).strip()

            if city:
                return {
                    "intent": "weather",
                    "city": city.title()
                }

    # ---------------------------------
    # Reminder
    # ---------------------------------
    match = re.search(r"(\d+)\s*minute", text)

    if "remind" in text and match:
        return {
            "intent": "reminder",
            "minutes": int(match.group(1))
        }

    # ---------------------------------
    # Search Web
    # ---------------------------------
    if text.startswith("search "):
        return {
            "intent": "search_web",
            "query": text.replace("search", "", 1).strip()
        }

    # Not handled locally
    return None