import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

def main():
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    
    try:
        user_prompt = sys.argv[1]
    except:
        print("Please provide a prompt as an argument after the run command")
        sys.exit(1)

    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

    client = genai.Client(api_key = api_key)
    response = client.models.generate_content(
        model = 'gemini-2.0-flash-001', 
        contents = messages
        )

    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count }")

if __name__ == "__main__":
    main()
