import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt
from call_function import available_functions, call_function


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    api_key = os.environ.get("Ai_Agent_key")
    if api_key is None:
        raise RuntimeError("Ai_Agent_key not found in .env file")

    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(
            role="user",
            parts=[types.Part(text=args.user_prompt)]
        )
    ]

    for _ in range(20):

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0,
                tools=[available_functions]
            )
        )

        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        function_responses = []

        if response.function_calls:

            for function_call in response.function_calls:

                function_call_result = call_function(function_call, args.verbose)

                if args.verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")

                function_responses.append(function_call_result.parts[0])

            messages.append(
                types.Content(
                    role="user",
                    parts=function_responses
                )
            )

            continue

        print("\nFinal response:\n")
        print(response.text)
        break

    else:
        print("Error: Max iterations reached without final answer")


if __name__ == "__main__":
    main()
