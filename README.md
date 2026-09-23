# Pravin_GENai

A FastAPI service that provides a Marcus Aurelius persona chat endpoint using
LangChain and an OpenRouter-compatible model.

## Setup

Create and activate a virtual environment, then install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Set an OpenRouter API key:

```bash
export OPENROUTER_API_KEY="your-api-key"
```

## Run

```bash
python main.py
```

The API is available at `http://127.0.0.1:8000`.
Interactive documentation is available at
`http://127.0.0.1:8000/docs`.

## Endpoint

Send a `POST` request to `/chat`:

```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id":"demo","message":"How should I handle a difficult day?"}'
```