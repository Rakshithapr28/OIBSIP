import threading
import time

from assistant.speak import speak


def reminder_timer(minutes):
    """
    Wait for the specified time and then remind the user.
    """

    time.sleep(minutes * 60)

    speak(f"Reminder! Sagar, your {minutes} minute reminder is complete.")


def set_reminder(minutes):
    """
    Start a reminder in a separate thread.
    """

    reminder_thread = threading.Thread(
        target=reminder_timer,
        args=(minutes,),
        daemon=True
    )

    reminder_thread.start()

    return f"Okay Rakshitha. I will remind you in {minutes} minute{'s' if minutes > 1 else ''}."