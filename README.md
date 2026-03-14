# EduPlanner AI Engine

An AI-powered learning plan generator built with FastAPI, LangChain, and Google Gemini.

---

## How It Works

1. User enters topic, time commitment, description, and level on the frontend
2. The AI engine searches the web for relevant info
3. Gemini turns the search results into a structured learning plan
4. Gemini adds time allocation to each module
5. The result is displayed on the result page

---

## Project Structure

```
project/
├── Backend/
│   ├── main.py                  # FastAPI server
│   ├── chain.py                 # Connects all nodes into one chain
│   ├── state.py                 # State dictionary
│   ├── llm_setup.py             # Gemini setup
│   ├── web_search_node.py       # Node 1 - web search
│   ├── structured_plan_node.py  # Node 2 - make plan
│   ├── time_allocation_node.py  # Node 3 - add time
│   └── requirements.txt
│
└── Frontend/
    ├── index.html               # Input form
    └── result.html              # Result page
```

---

## Setup

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Add your Gemini API key in .env file in the backend folder
```python

GOOGLE_API_KEY = "your_key_here"
```
Get a free key at [aistudio.google.com](https://aistudio.google.com)

**3. Start the AI engine**
```bash
python main.py
```

**4. Open the frontend**
```bash
cd Frontend
python -m http.server 5500
```
Then go to `http://localhost:5500/index.html`

---

## API Endpoint

`POST http://127.0.0.1:8001/generate-plan`

```json
{
  "topic": "Web Development",
  "time_commitment": "1 month",
  "description": "I want to build websites from scratch",
  "level": "beginner"
}
```

---

## Tech Stack

- **Frontend** — HTML, CSS, JavaScript
- **Backend** — FastAPI
- **AI / LLM** — Google Gemini via LangChain
- **Web Search** — DuckDuckGo (free, no API key needed)
