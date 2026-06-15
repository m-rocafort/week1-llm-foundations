
from urllib import response
import anthropic
import anthropic

# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

load_dotenv(override=True)
client = anthropic.Anthropic()


MODEL = "claude-opus-4-8"
PROMPT = ""
SYSTEM_PROMPT="Check the temperature and convert it to different scale"

def main() -> None:

    while True:

        user_input = input("Input the temp: ").strip()

        if user_input.lower() in {"quit", "exit"}:
            print("Goodbye! 👋")
            break
        if not user_input:
            continue  # ignore empty lines, ask again


        response = client.messages.create(
            model=MODEL,
            max_tokens=100,
            system=SYSTEM_PROMPT,
            messages=[{"role":"user", "content": user_input}]
        )

        answer = "".join(b.text for b in response.content if b.type == "text")
        print(f"Claude: {answer}\n")




if __name__ == '__main__':
    main()    

