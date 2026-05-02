print("CodSoft Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Bot: Hello! How can I Assist you today?")

    elif "your name" in user:
        print("Bot: I am a Rule-Based Chatbot.")

    elif "how are you" in user:
        print("Bot: I am fine. Thank you for asking!")

    elif "time" in user:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    elif "date" in user:
        from datetime import date
        today = date.today()
        print("Bot: Today's date is", today)

    elif user == "bye":
        print("Bot: Goodbye Have a Nice Day!")
        break

    else:
        print("Bot: Sorry, I am unable to understand that.")