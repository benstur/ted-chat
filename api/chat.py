import json
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"  # replace with your key or set in Vercel

SYSTEM_PROMPT = """
You're ChatGPT pretending to be Ted from the movie Ted (2012).
You're a sarcastic, foul-mouthed teddy bear with a Boston accent.
You joke around, swear casually, and drop pop culture references. Stay in character 100%.
"""

messages = [{"role": "system", "content": SYSTEM_PROMPT}]

def handler(request):
    body = request.json()
    user_input = body["message"]

    messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"reply": reply})
    }
