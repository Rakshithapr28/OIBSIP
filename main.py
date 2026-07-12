from assistant.ai_service import detect_intent


def main():

    user_input = input("You: ")

    result = detect_intent(user_input)

    print("\nDetected Intent:\n")
    print(result)


if __name__ == "__main__":
    main()