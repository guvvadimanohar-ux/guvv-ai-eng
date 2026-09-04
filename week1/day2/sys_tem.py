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
propmt = "Suggest me a name coffe shop"
# system
message_system = {
    "role" : "system",
    "content": "You are a brand manager suggest me name for my food brand name should one word suggest only one name "
}
message = {
    "role": role,
      "content": propmt
      }
messages = [message]
response = client.chat.completions.create(model=model, messages = messages, temperature=2)
# print(response)

print("####################")
    
answer=response.choices[0].message.content
print(answer)