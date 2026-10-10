import os
from typing import Literal
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

client = OpenAI(
    base_url=os.environ["AZURE_OPENAI_BASE_URL"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)


class ReviewAnalysis(BaseModel):
    sentiment: Literal["positive", "negative", "mixed"]
    topic: str
    escalate: bool
    reply: str

INSTRUCTIONS = ("You analyze product reviews for a retailer. "
                "Set escalate to true only if the customer reports a defect, safety issue, "
                "or asks for a refund. "
                "Keep reply to one friendly sentence addressed to the customer.")

review = input("Paste a review: ")

response = client.responses.parse(
    model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
    input=review,
    instructions=INSTRUCTIONS,
    text_format=ReviewAnalysis,
)

result = response.output_parsed
print(result)
print(result.sentiment, result.escalate)