from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-haiku-4-5"

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages, system=None, temperature=1.0):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature
    }
    
    if system:
        params["system"] = system

    with client.messages.stream(**params) as stream:
            for text in stream.text_stream:
                print(text, end="")

messages = []

# Add the initial user question
add_user_message(messages, "Write a 50 sentence description of a fake database.")

chat(messages, temperature=0.0)  # Low temperature - more predictable