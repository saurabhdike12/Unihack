import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

print("Checking available models for your API key...\n")
for model in client.models.list():
    if "generateContent" in model.supported_actions:
        print(model.name)