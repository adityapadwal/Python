responses = {
  "what's your name": "My name is Chatbot.",
  "what can you do": "I can answer questions and have conversations with you.",
  "what's the weather like": "I'm sorry, I don't have the current weather information.",
  "default": "I'm sorry, I don't understand what you're saying."
}

print("Hi, I'm Chatbot. How can I help you today?")

while True:
  user_input = input("You: ").lower()

  if user_input in responses:
    print("Chatbot: " + responses[user_input])
  elif user_input in ['bye', 'quit', 'exit']:
    print("Chatbot: Bye! Have a great day!")
    break
  else:
    print("Chatbot: " + responses["default"])
    