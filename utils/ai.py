from google import genai
from google.genai import types
from env import GOOGLE_API_KEY

client = genai.Client(api_key=GOOGLE_API_KEY)

def gemini(system_instruction, contents):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            system_instruction=system_instruction,
        ),
        contents=contents,
    )
    return response