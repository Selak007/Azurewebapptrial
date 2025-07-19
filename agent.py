import os
from openai import AzureOpenAI
from flask import Flask, request, jsonify
from flask_cors import CORS

endpoint = "https://aihub0012034742062.openai.azure.com/"
model_name = "gpt-35-turbo"
deployment = "gpt-35-turbo"
subscription_key = "EY3z5eTUiFnr2s63t2aohykHWhhavdObJFKI9svE0EONuGAsJz9XJQQJ99BFACHYHv6XJ3w3AAAAACOGXAew"
api_version = "2024-12-01-preview"

app = Flask(__name__)
CORS(app)

client = AzureOpenAI(
    api_key=subscription_key,
    api_version=api_version,
    azure_endpoint=endpoint
)

@app.route('/ask', methods=['POST'])
def ask_agent():
    data = request.json
    user_input = data.get('question', '')
    prompt = f"Answer the following in a simple paragraph of about 30 words:\n{user_input}"
    
    response = client.chat.completions.create(
        model=deployment,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    answer = response.choices[0].message.content.strip()
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
