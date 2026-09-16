import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

client = OpenAI(
    api_key=os.environ["MY_API_KEY"],
    base_url=os.environ["MY_BASE_URL"],
)

response = client.chat.completions.create(
    model="glm-5.2",
    messages=[
       #  {"role": "user", "content": "What does the df command show?"}
          {"role": "user", "content": sys.argv[1]}
    ],
)

print(response.choices[0].message.content)


