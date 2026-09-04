import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API error")
client = Groq (api_key = my_api_key)
model = "openai/gpt-oss-120b"
role = "user"
# 3 prompts
propmt1 = "hi !"
propmt2 = "explain about time travel in detail"
propmt3 = "write a 1000 word essay on machine learning under 100 tokens"

prompts = [propmt1, propmt2, propmt3]

for propmt in prompts:
    message = {
        "role": role,
          "content": propmt

          }

messages = [message]
response = client.chat.completions.create(model=model, messages = messages , max_tokens=500)
usage = response.usage
print(f"Prompt: {propmt} -- > ur toeksn {usage.prompt_tokens} | completion tokens: {usage.completion_tokens} | total tokens: {usage.total_tokens} Finish response : {response.choices[0].finish_reason}")
