from openai import OpenAI

# Initialize client with your API key
client = OpenAI(api_key="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")

# Ask something to the model

response = client.chat.completions.create(
        model="gpt-4o-mini",   # you can also use "gpt-4.1" or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "."}
        ]
    )

    # Print the model’s reply
print(response.choices[0].message.content)