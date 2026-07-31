from assistant.speak import speak


def handle_local_command(user_input):
    """
    Handle commands that don't need AI.
    Returns True if handled locally, otherwise False.
    """

    command = user_input.lower()

    # Greetings
    greetings = [
        "hello",
        "hi",
        "hey",
        "good morning",
        "how are you ",
        "good afternoon",
        "good evening"
    ]

    if any(greeting in command for greeting in greetings):
        speak("Hello Sagar! How can I help you today?")
        return True

    # Exit
    if command in ["exit", "quit", "bye"]:
        speak("Goodbye! Have a nice day.")
        return True

    return False