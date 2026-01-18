from google import genai

client = genai.Client(api_key="AIzaSyC-2Fd1G667b7WTWbyGP1CFKf9xgkQtDlM")

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)