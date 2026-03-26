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

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "Hello, Claude! This is my first API call."}
        ],
    )

    print(message.content[0].text)


if __name__ == "__main__":
    main()
