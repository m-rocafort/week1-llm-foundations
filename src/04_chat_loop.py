"""
Exercise 4 — A real chat loop (conversation MEMORY).

Run it:  python src/04_chat_loop.py
         (type your messages; type 'quit', 'exit', or press Ctrl+C to stop)

What you'll learn:
- WHY a conversation is a GROWING LIST of messages
- How an LLM "remembers" earlier turns (spoiler: YOU resend them every time)
- How to keep a friendly loop running and handle errors gracefully

THE BIG IDEA: The API is stateless. Claude does NOT remember anything on its own.
"Memory" is an illusion YOU create by sending the whole conversation back each turn.
"""

import os

import anthropic
from dotenv import load_dotenv

load_dotenv(override=True)
client = anthropic.Anthropic()

# A chat loop makes MANY calls, so we pick the cheap/fast model (model-choice
# instinct from exercise 3). Swap to "claude-opus-4-8" if you want deeper answers.
MODEL = "claude-haiku-4-5"

# The system prompt sets the persona ONCE for the whole conversation (exercise 2).
SYSTEM_PROMPT = (
    "You are a friendly mentor helping an RPA developer learn AI automation. "
    "Keep answers concise and practical."
)


def chat() -> None:
    print("=== Chat with Claude (type 'quit' to exit) ===\n")

    # THIS LIST is the conversation's memory. It starts empty and GROWS every turn.
    messages: list[dict] = []

    while True:  # loop forever until the user quits
        # 1) Get the user's message from the keyboard.
        user_input = input("You: ").strip()
        if user_input.lower() in {"quit", "exit"}:
            print("Goodbye! 👋")
            break
        if not user_input:
            continue  # ignore empty lines, ask again

        # 2) Append the user's turn to the conversation.
        messages.append({"role": "user", "content": user_input})

        # 3) Send the ENTIRE conversation so far. This is how Claude "remembers".
        try:
            response = client.messages.create(
                model=MODEL,
                max_tokens=500,
                system=SYSTEM_PROMPT,
                messages=messages,  # <-- the whole history, not just the latest line
            )
        except anthropic.AuthenticationError:
            print("⚠️  Auth failed — check ANTHROPIC_API_KEY in your .env file.")
            break
        except anthropic.RateLimitError:
            print("⚠️  Rate limited — wait a moment and try again.")
            messages.pop()  # drop the unanswered user turn so history stays clean
            continue

        # 4) Pull out Claude's text and show it.
        answer = "".join(b.text for b in response.content if b.type == "text")
        print(f"Claude: {answer}\n")

        # 5) Append Claude's reply to the history so the NEXT turn has full context.
        messages.append({"role": "assistant", "content": answer})


if __name__ == "__main__":
    try:
        chat()
    except KeyboardInterrupt:  # Ctrl+C is a normal way to quit
        print("\nGoodbye! 👋")

    # 🧪 TRY THIS:
    #  1. Tell Claude your name, then ask "what's my name?" two turns later.
    #     It remembers — because the whole list gets resent each time.
    #  2. Comment out step 5 (don't append the assistant reply). Now it FORGETS
    #     its own answers — proof that YOU are the one providing the memory.
    #  3. After a long chat, print len(messages) — every turn grows the list (and
    #     the input tokens/cost). This is why real apps eventually trim old turns.
