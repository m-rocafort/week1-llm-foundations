"""
Exercise 2 — System prompts + streaming.

Run it:  python src/02_prompt_experiments.py

What you'll learn:
- The SYSTEM PROMPT is the #1 lever for controlling behavior
- The same question yields different answers under different "personas"
- How to STREAM a response token-by-token (better UX, no timeouts)
"""

import os

import anthropic
from dotenv import load_dotenv


load_dotenv(override=True)

client = anthropic.Anthropic()
MODEL = "claude-opus-4-8"

QUESTION = "How should I approach automating an invoice-processing workflow?"

# A system prompt sets the role, rules, and tone. Try editing these.
PERSONAS = {
    "Terse expert": "You are a senior automation architect. Answer in at most 3 bullet points. No preamble.",
    "Friendly mentor": "You are a warm, encouraging mentor for someone new to AI. Explain simply and cheer them on.",
    "Skeptical reviewer": "You are a risk-focused reviewer. For any approach, lead with what could go wrong.",
    "Me as reviewer": "Im the owner. For any approach, do check the end to end approach, source and end point. have it itemized. and provide the best apprach required",
    
}


def compare_personas() -> None:
    print("########## SAME QUESTION, DIFFERENT SYSTEM PROMPTS ##########\n")
    for name, system_prompt in PERSONAS.items():
        response = client.messages.create(
            model=MODEL,
            max_tokens=400,
            system=system_prompt,  # <-- the lever
            messages=[{"role": "user", "content": QUESTION}],
        )
        answer = "".join(b.text for b in response.content if b.type == "text")
        print(f"----- {name} -----")
        print(answer)
        print()


def streaming_demo() -> None:
    print("########## STREAMING (watch it type) ##########\n")
    # Streaming yields text as it's generated. This is how chat UIs feel "live".
    with client.messages.stream(
        model=MODEL,
        max_tokens=400,
        system="You are a helpful assistant. Write one short paragraph.",
        messages=[{"role": "user", "content": "Why is automation experience valuable for an AI career?"}],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
    print("\n")

    # 🧪 TRY THIS:
    #  1. Add your own persona to the PERSONAS dict.
    #  2. Make a "JSON-only" persona: "Always respond with valid JSON, no prose."
    #     (This is a preview of Week 2's structured outputs.)


if __name__ == "__main__":
    compare_personas()
    streaming_demo()
