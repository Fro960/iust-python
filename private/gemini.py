import sys
from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyC-2Fd1G667b7WTWbyGP1CFKf9xgkQtDlM")

if len(sys.argv) == 2:
    res = sys.argv[1]
else:
    res = input("ask: ")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    config=types.GenerateContentConfig(
    system_instruction="answer in one sentence"),
    contents= res
)
print(response.text)