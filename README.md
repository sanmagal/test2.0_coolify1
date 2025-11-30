# test2.0_coolify1

A voice AI agent built with LiveKit Agents.

## Configuration

- **LLM**: openai (gpt-4o-mini)
- **STT**: openai
- **TTS**: openai (alloy)

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and fill in your API keys:
```bash
cp .env.example .env
```

3. Run the agent:
```bash
python agent.py dev
```

## Docker Deployment

Build and run with Docker:

```bash
docker build -t test2.0_coolify1 .
docker run --env-file .env test2.0_coolify1
```

## Deploy to Coolify

1. Push this repository to GitHub/GitLab
2. In Coolify, create a new application
3. Select "Docker" as the build pack
4. Add environment variables from `.env.example`
5. Deploy!

## Learn More

- [LiveKit Agents Documentation](https://docs.livekit.io/agents/)
- [LiveKit Cloud](https://cloud.livekit.io/)
