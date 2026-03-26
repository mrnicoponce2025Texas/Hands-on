import os
import anthropic
from dotenv import load_dotenv


def main():
    load_dotenv()
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "ANTHROPIC_API_KEY is not set. "
            "Copy .env.example to .env and add your key, or export the variable."
        )

    client = anthropic.Anthropic(api_key=api_key)

    conversation_history = []

    print("Multi-turn conversation with Claude (type 'quit' to exit)\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("quit", "exit"):
            break
        if not user_input:
            continue

        conversation_history.append({"role": "user", "content": user_input})

        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            messages=conversation_history,
        )

        assistant_message = response.content[0].text
        conversation_history.append({"role": "assistant", "content": assistant_message})

        print(f"Claude: {assistant_message}\n")


if __name__ == "__main__":
    main()
