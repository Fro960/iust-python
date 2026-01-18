import sys
from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyC-2Fd1G667b7WTWbyGP1CFKf9xgkQtDlM")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    config=types.GenerateContentConfig(
    system_instruction="answer in one sentence"),
    contents= sys.argv[1]
)
print(response.text)