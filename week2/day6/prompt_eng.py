import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API error")
client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"

def llm_ans(prompt):
    message = {"role": "user", "content": prompt}
    messages = [message]
    response = client.chat.completions.create(model=model, messages=messages)
    ans = response.choices[0].message.content
    return ans


bad_prompt ="""
#role :
you are a support assistant at a mobile/laptop company

# task :
You have to classify the issue in cateogry
This is user complaint:
my laptop isnt working
#example
for instance if a user says he wants a refund then category is return

#fallback
if the issue is unrelated to given constraints answer should be other

#output format
your answer should be in one word only ,one word should be one of words in given constraints

# constranit
you have to classify the issue in one of 3 categories namely billing,tehnical,return
"""


print(llm_ans(bad_prompt))