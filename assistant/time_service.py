from datetime import datetime


def get_current_time():
    """
    Returns the current time.
    """

    current_time = datetime.now().strftime("%I:%M %p")

    return f"The current time is {current_time}."


def get_current_date():
    """
    Returns today's date.
    """

    current_date = datetime.now().strftime("%A, %d %B %Y")

    return f"Today is {current_date}."