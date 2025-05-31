from openai import ChatCompletion
import openai
import json

openai.api_key = os.environ.get("OPENAI_API_KEY")

SYSTEM_PROMPT = """
You're ChatGPT pretending to be Ted from the movie Ted (2012). 
You're a sarcastic, foul-mouthed teddy bear with a Boston accent. 
You joke around, swear casually, and drop pop culture references. Stay in character 100%.
"""

messages = [{"role": "system", "content": SYSTEM_PROMPT}]

def handler(request, response):
    if request.method == "POST":
        try:
            body = request.json()
            user_input = body["message"]
            messages.append({"role": "user", "content": user_input})

            chat_response = ChatCompletion.create(
                model="gpt-4",
                messages=messages
            )

            reply = chat_response.choices[0].message.content
            messages.append({"role": "assistant", "content": reply})

            return response.status(200).json({"reply": reply})
        except Exception as e:
            return response.status(500).json({"error": str(e)})

    return response.status(405).send("Method not allowed")
