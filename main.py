import argparse
import json
import os
import sys
from toolsArray import toolsAr
from openai import OpenAI

API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("OPENROUTER_BASE_URL", default="https://openrouter.ai/api/v1")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("-p", required=True)
    args = p.parse_args()

    messages = [{"role": "user", "content": args.p}]

    if not API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY is not set")

    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

    while True:

        # noinspection PyTypeChecker
        chat = client.chat.completions.create(
            model="anthropic/claude-haiku-4.5",
            messages=messages,
            tools=toolsAr
        )

        if not chat.choices or len(chat.choices) == 0:
            raise RuntimeError("no choices in response")

        # Print statements for debugging
        print("Logs from the program will appear here!", file=sys.stderr)

        chMessage = chat.choices[0].message
        messages.append(chMessage)

        if not chMessage.tool_calls :
            print(chMessage.content)
            break

        for tool_call in chMessage.tool_calls:
            name = tool_call.function.name
            funArgs = tool_call.function.arguments

            if name == "Read":
                jsonArgs = json.loads(funArgs)
                with open(jsonArgs["file_path"]) as file:
                    contents = file.read()

            elif name == "Write":
                with open(jsonArgs["file_path"], "w") as file:
                    file.write(jsonArgs["content"])

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": contents
            })

if __name__ == "__main__":
    main()
