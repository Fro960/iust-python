from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    input = "what's cs50?",
    model = "gpt-5-nano"
)
print(response.output_text)