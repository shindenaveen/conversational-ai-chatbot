Conversational AI Chatbot

This project is a simple Python-based chatbot API built using FastAPI. It uses a combination of FAQ matching for quick replies and OpenAI GPT (via the ChatCompletion API) for more flexible, AI-generated responses. The chatbot is designed for internal support and automation tasks.

---

Features

- FAQ-based quick answer matching from a JSON dataset
- Fallback to OpenAI GPT-3.5-turbo model for unanswered queries
- Simple REST API endpoint for chat interaction
- Easy to extend with more FAQs or more advanced AI functionality

---

Getting Started

Prerequisites

- Python 3.7 or higher
- OpenAI API key (set as environment variable OPENAI_API_KEY)

Installation

1. Clone the repository:

   git clone https://github.com/yourusername/conversational-ai-chatbot.git
   cd conversational-ai-chatbot

2. Install the required Python packages:

   pip install -r requirements.txt

3. Set your OpenAI API key:

- On Linux/macOS:
   
   export OPENAI_API_KEY="your_openai_api_key_here"

- On Windows CMD:
   
   set OPENAI_API_KEY="your_openai_api_key_here"

Running the Server

Start the FastAPI server:

   python chatbot.py

The server will run on http://localhost:8000.

---

Usage

Send a POST request to the /chat/ endpoint with JSON payload:

{
  "message": "Your question here"
}

Example using curl:

curl -X POST "http://localhost:8000/chat/" -H "Content-Type: application/json" -d '{"message":"What are your working hours?"}'

Sample response:

{
  "response": "Our working hours are 9 AM to 6 PM, Monday to Friday.",
  "source": "faq"
}

---

Project Structure

conversational-ai-chatbot/
|
├── chatbot.py               # FastAPI application code
├── sample_faq.json          # Sample FAQ dataset
├── requirements.txt         # Python package dependencies
├── output/
│   └── sample_chat_log.txt  # Example chat conversation log
└── README.txt               # This file

---

Sample FAQ Data (sample_faq.json)

[
  {
    "question": "What are your working hours?",
    "answer": "Our working hours are 9 AM to 6 PM, Monday to Friday."
  },
  {
    "question": "How to reset my password?",
    "answer": "Click 'Forgot Password' on the login page to reset your password."
  },
  {
    "question": "Where can I find the documentation?",
    "answer": "Project documentation is available in the internal knowledge base on Confluence."
  }
]

---

Example Chat Log (output/sample_chat_log.txt)

User: What are your working hours?
Bot: Our working hours are 9 AM to 6 PM, Monday to Friday. [faq]

User: Who is the CEO of the company?
Bot: As of August 2025, the CEO of the company is John Smith. [gpt]

---

Future Improvements

- Add frontend UI for easier chat interaction
- Implement more sophisticated RAG (Retrieval-Augmented Generation) capabilities
- Add integration with organizational platforms (Confluence, GitLab, etc.)
- Include vector search with FAISS or Pinecone for better knowledge retrieval

---

License

This project is licensed under the MIT License.
