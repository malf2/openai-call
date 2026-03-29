from openai import OpenAI
from rich import print

client = OpenAI()

# response = client.responses.create(
#     model="gpt-4o-mini",
#     instructions="Talk like a pirate.",
#     input="Are semicolons optional in JavaScript?"
# )

# print(response.output_text)

response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {
            "role": "developer",
            "content": "Talk like a pirate."
        },
        {
            "role": "user",
            "content": "Are semicolons optional in JavaScript?"
        }
    ]
)

print(response.output_text)