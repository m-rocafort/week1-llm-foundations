"""
Exercise 3 — Model choice & cost intuition.

Run it:  python src/03_model_comparison.py

What you'll learn:
- The same prompt on a smart model (Opus) vs a fast/cheap model (Haiku)
- How to estimate the cost of a call from token usage
- The core 2026 hiring skill: picking the right model for the job

WHY THIS MATTERS: In real AI automation, you use cheap models (Haiku) for the
many simple steps and reserve the expensive model (Opus) for the hard reasoning.
Showing you think about cost is a strong signal to employers.
"""

from anthropic.types import beta_overloaded_error
from anthropic.types import beta_overloaded_error
import os

import anthropic
from dotenv import load_dotenv

load_dotenv(override=True)
client = anthropic.Anthropic()

# Approx published prices (USD per 1 MILLION tokens). Always confirm in the console.
PRICING = {
    "claude-opus-4-8":  {"input": 5.00, "output": 25.00},   # smartest, priciest
    "claude-haiku-4-5": {"input": 1.00, "output": 5.00},    # fast & cheap
}

PROMPT = "Classify this support message as BILLING, TECHNICAL, or OTHER. Reply with one word only:\n\n'My invoice shows double the amount I was quoted.'"


def estimate_cost(model: str, usage) -> float:
    p = PRICING[model]
    return (usage.input_tokens / 1_000_000) * p["input"] + (usage.output_tokens / 1_000_000) * p["output"]


def run(model: str) -> None:
    response = client.messages.create(
        model=model,
        max_tokens=20,  # a classification needs almost no output
        messages=[{"role": "user", "content": PROMPT}],
    )
    answer = "".join(b.text for b in response.content if b.type == "text").strip()
    cost = estimate_cost(model, response.usage)
    print(f"----- {model} -----")
    print(f"Answer: {answer!r}")
    print(f"Tokens: in={response.usage.input_tokens}, out={response.usage.output_tokens}")
    print(f"Est. cost this call: ${cost:.6f}")
    print(f"Est. cost for 100,000 such calls: ${cost * 100_000:,.2f}\n")


if __name__ == "__main__":
    print("########## SAME TASK, TWO MODELS ##########\n")
    for model in PRICING:
        run(model)

    print("Takeaway: for a simple, high-volume task like classification, Haiku gives")
    print("the same answer for a fraction of the cost. That's the model-choice instinct")
    print("employers want. Save Opus for genuinely hard reasoning.")

    # 🧪 TRY THIS:
    #  1. Swap in a HARD prompt (e.g. a tricky multi-step reasoning question) and
    #     see whether Haiku still matches Opus. This is how you learn where each fits.
