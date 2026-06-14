"""
Exercise 1 — Your first LLM API call.

Run it:  python src/01_first_call.py

What you'll learn:
- How to authenticate and send a single message
- The shape of a request (model, max_tokens, messages)
- How to read the response and its token usage
"""

import os

import anthropic
from dotenv import load_dotenv

# Loads ANTHROPIC_API_KEY from your .env file into the environment.
# override=True makes .env the source of truth even if a stale ANTHROPIC_API_KEY
# is already set in your OS environment (a common cause of 401 invalid x-api-key).
load_dotenv(override=True)

# The client reads ANTHROPIC_API_KEY from the environment automatically.
client = anthropic.Anthropic()

# A "model" is the brain you're talking to. claude-opus-4-8 is the most capable;
# we'll meet the cheaper claude-haiku-4-5 in exercise 3.
MODEL = "claude-opus-4-8"


def main() -> None:
    response = client.messages.create(
        model=MODEL,
        max_tokens=100,  # cap on the RESPONSE length (in tokens)
        messages=[
            # A conversation is a list of turns. You start as "user".
            {"role": "user", "content": "In 3 sentences, explain what an LLM is to an RPA developer."}
        ],
    )

    # response.content is a LIST of blocks. For plain text, grab the text blocks.
    answer = "".join(block.text for block in response.content if block.type == "text")
    print("=== Claude says ===")
    print(answer)

    # Every response tells you how many tokens it used. This is what you pay for.
    print("\n=== Token usage ===")
    print(f"Input tokens:  {response.usage.input_tokens}")
    print(f"Output tokens: {response.usage.output_tokens}")
    print(f"Stop reason:   {response.stop_reason}")  # 'end_turn' = finished naturally

    # 🧪 TRY THIS:
    #  1. Change the question above and re-run.
    #  2. Set max_tokens=20 and watch the answer get cut off (stop_reason='max_tokens').
    #  3. Ask it to "respond as a pirate" and see how it changes.


if __name__ == "__main__":
    main()
