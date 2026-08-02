# 🎙️ Advanced AI Voice Assistant

An intelligent voice assistant built with Python that combines AI-powered responses with local system automation. The assistant can understand voice commands, execute system tasks, fetch real-time information, and answer general questions using Google's Gemini AI.

---

## 🚀 Features

- 🎤 Voice Recognition
- 🤖 AI-powered conversations using Google Gemini
- 🌦️ Live Weather Information
- 📰 Latest News Updates
- 🌐 Web Search Support
- 📧 Send Emails
- 💻 Local System Commands
- 🗣️ Text-to-Speech Responses
- 🧠 Intent Detection using AI
- ⚡ Fast command routing
- ❌ Exit command support

---

## 🛠️ Technologies Used

### Programming Language
- Python 3.10+

### AI
- Google Gemini API

### Libraries
- SpeechRecognition
- PyAudio
- pyttsx3
- google-generativeai / google-genai
- requests
- python-dotenv
- wikipedia
- webbrowser
- os
- datetime

### APIs
- Google Gemini API
- OpenWeather API
- News API

---

## 📂 Project Structure

```
Rakshita_Task1_VoiceAssistant/
│
├── assistant/
│   ├── ai_service.py
│   ├── local_handler.py
│   ├── router.py
│   ├── speech.py
│   ├── speak.py
│   └── ...
│
├── assets/
├── .env
├── .gitignore
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Rakshithapr28/OIBSIP.git
```

Move into the project

```bash
cd Rakshita_Task1_VoiceAssistant
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file and add your API keys.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
WEATHER_API_KEY=YOUR_OPENWEATHER_API_KEY
NEWS_API_KEY=YOUR_NEWS_API_KEY
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## Example Commands

- Hello
- What's the weather today?
- Open YouTube
- Open Google
- Search Python tutorials
- Tell me today's news
- Send an email
- Exit

---

## Future Enhancements

- Face Recognition
- Desktop GUI
- WhatsApp Integration
- Calendar Management
- Task Scheduling
- Smart Home Automation
- Multi-language Support

---

## 👩‍💻 Developer

Rakshitha

---

## 📜 License

This project is developed for educational and internship purposes under **Oasis Infobyte (OIBSIP)**.