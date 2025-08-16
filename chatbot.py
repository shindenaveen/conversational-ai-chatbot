import nest_asyncio
import uvicorn
import threading
import time
import requests
import os
import json
from fastapi import FastAPI
from pydantic import BaseModel
import openai

# Apply the nest_asyncio patch for Jupyter compatibility
nest_asyncio.apply()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load FAQ data
faq_data = [
    {"question": "What are your working hours?", "answer": "Our working hours are 9 AM to 6 PM, Monday to Friday."},
    {"question": "How to reset my password?", "answer": "Click 'Forgot Password' on the login page to reset your password."},
    {"question": "Where can I find the documentation?", "answer": "Project documentation is available in the internal knowledge base on Confluence."}
]

def find_answer(user_question, faq_list):
    user_question_low = user_question.lower()
    for item in faq_list:
        if item["question"].lower() == user_question_low:
            return item["answer"]
    return None

def get_gpt_response(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful internal support assistant."},
            {"role": "user", "content": user_message}
        ]
    )
    return response['choices'][0]['message']['content']

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat/")
def chat_endpoint(request: ChatRequest):
    answer = find_answer(request.message, faq_data)
    if answer:
        return {"response": answer, "source": "faq"}
    else:
        gpt_reply = get_gpt_response(request.message)
        return {"response": gpt_reply, "source": "gpt"}

# Function to run the server in a thread
def run_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Start server in a separate thread
server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()

# Give the server a moment to start
time.sleep(2)

# Test the chatbot API using requests (Example)
test_message = {"message": "What are your working hours?"}
response = requests.post("http://127.0.0.1:8000/chat/", json=test_message)
print("Response status:", response.status_code)
print("Response data:", response.json())
