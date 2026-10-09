import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.environ["AZURE_OPENAI_BASE_URL"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
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