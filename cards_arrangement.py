import openai

# Set your OpenAI API key
openai.api_key = "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"

# Function to generate prompts based on user input
def generate_prompt(user_input):
    # Define the input prompt
    prompt = f"User: {user_input}\nBot:"

    # Use the completion API to generate a response
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        max_tokens=50
    )

    # Extract the generated text from the response
    generated_text = response["choices"][0]["text"]

    return generated_text

# Example usage
user_input = input("User: ")
generated_prompt = generate_prompt(user_input)
print("Bot:", generated_prompt)
