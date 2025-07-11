from google import genai
from google.genai import types
from env import GOOGLE_API_KEY

client = genai.Client(api_key=GOOGLE_API_KEY)

class Gemini:
    def __init__(self, system_instruction):
        self.system_instruction = system_instruction

    def request(self, contents):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_budget=0),
                system_instruction=self.system_instruction,
            ),
            contents=contents,
        )
        return response.text