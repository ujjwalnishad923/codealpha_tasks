# Basic Chatbot

print("Hello! I am a simple chatbot.")
print("You can type 'hello', 'how are you', 'name', or 'bye'.")

while True:

    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Bot: Hello! How can I help you?")

    elif user_input == "how are you":
        print("Bot: I am fine. Thank you!")

    elif user_input == "name":
        print("Bot: My name is Python Chatbot.")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")