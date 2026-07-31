import webbrowser


WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "gmail": "https://mail.google.com",
    "github": "https://github.com",
    "chatgpt": "https://chat.openai.com",
    "linkedin": "https://www.linkedin.com",
    "instagram": "https://www.instagram.com",
    "facebook": "https://www.facebook.com",
    "twitter": "https://twitter.com"
}


def open_website(website_name):
    """
    Open a website in the default browser.
    """

    website = website_name.lower()

    if website in WEBSITES:
        webbrowser.open(WEBSITES[website])
        return f"Opening {website_name}."
    else:
        return f"Sorry, I don't know the website {website_name}."