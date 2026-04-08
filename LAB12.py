# Simple Generative AI prompt experiment

from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

# Try different prompts here
prompt = "Explain Machine Learning in simple terms"

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print("Prompt:", prompt)
print("Response:", response.output[0].content[0].text)