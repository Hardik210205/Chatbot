import json

# Load responses from JSON file
with open("responses.json") as file:
    responses = json.load(file)

def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    return responses.get(user_input, "Sorry, I don't understand that yet.")

# Run chatbot
print("i am ready to talk! Type 'bye' to exit.")

while True:
    user_text = input("You: ")
    response = chatbot_response(user_text)
    print("Bot:", response)
    if user_text.lower() == "bye":
        break
