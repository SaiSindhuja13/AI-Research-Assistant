import os
from openai import OpenAI

# Set your API key securely (recommended: use environment variable)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Call ChatCompletion with the new syntax
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Summarize the importance of topological data analysis in ML."}
    ]
)

# Print the response content
print(response.choices[0].message.content)
