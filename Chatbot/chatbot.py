print("Welcome to Simple Chatbot")
print("Type 'bye' to stop chatting")

while True:

    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi!")

    elif user == "how are you":
        print("Bot: I am fine.")

    elif user == "what is your name":
        print("Bot: My name is Simple Bot.")
    elif user == "tell me a joke":
        print("Bot: Why did the computer go to sleep? Because it was tired!")

    elif user == "what can you do":
        print("Bot: I can chat with you using simple rules.")

    elif user == "who created you":
        print("Bot: I was created using Python.")
    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")