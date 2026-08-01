import subprocess
import os


APPLICATIONS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "command prompt": "cmd.exe",
    "powershell": "powershell.exe",
    "wordpad": "write.exe"
}


def open_application(app_name):
    """
    Open an application installed on the computer.
    """

    app = app_name.lower()

    try:

        if app == "vs code":
            os.system("code")
            return "Opening Visual Studio Code."

        elif app == "chrome":
            os.system("start chrome")
            return "Opening Google Chrome."

        elif app in APPLICATIONS:
            subprocess.Popen(APPLICATIONS[app])
            return f"Opening {app_name}."

        else:
            return f"Sorry, I don't know how to open {app_name}."

    except Exception as e:
        print(f"Application Error: {e}")
        return "Sorry, I couldn't open the application."