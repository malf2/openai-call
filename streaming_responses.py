from openai import OpenAI
from rich import print

client = OpenAI()

stream = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {
            "role": "user",
            "content": "Say 'double bubble bath' ten times fast."
        }
    ],
    stream=True,
)

for event in stream:
    print(event)

