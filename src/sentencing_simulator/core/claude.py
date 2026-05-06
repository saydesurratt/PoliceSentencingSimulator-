import os
import json
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key="Your own API KEY")

def call_claude(system_prompt, user_input):
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=800,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": json.dumps(user_input)
            }
        ]
    )
    return response.to_dict()