import asyncio
import os
import base64
from livekit import agents
from livekit.agents import JobContext, WorkerOptions, cli
from livekit.plugins import openai
from livekit.plugins import openai
from livekit.plugins import openai




async def entrypoint(ctx: JobContext):
    """Main entrypoint for the agent."""
    
    # Initialize the agent session
    initial_ctx = agents.llm.ChatContext().append(
        role="system",
        text="""You are a helpful AI assistant."""
    )
    
    # Connect to the room
    await ctx.connect()
    
    # Create the voice agent
    agent = agents.VoiceAgent(
        llm=openai.LLM(model="gpt-4o-mini", temperature=0.7),
        stt=openai.STT(model="nova-2"),
        tts=openai.TTS(voice="alloy", speed=1),
        chat_ctx=initial_ctx,
        turn_detection=agents.TurnDetection(threshold=0.5),
        allow_interruptions=True,
        vad_threshold=0.5
    )
    
    # Start the agent
    agent.start(ctx.room)
    
    # Keep the agent running
    await agent.say("Hello! How can I help you today?", allow_interruptions=True)


if __name__ == "__main__":
    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=entrypoint,
        )
    )
