import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2024-10-21",
)

review = input("Paste a review: ")

response = client.chat.completions.create(
    model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
    messages=[
        {"role": "system", "content": "You analyze product reviews. Say whether the sentiment is positive, negative, or mixed, in one sentence."},
        {"role": "user", "content": review},
    ],
)

print(response.choices[0].message.content)