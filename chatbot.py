import random

def chatbot():
    print("Bot: Hello! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        # Greetings
        if user_input in ["hello", "hi", "hey"]:
            responses = ["Hi!", "Hello there!", "Hey!"]
            print("Bot:", random.choice(responses))

        # Asking about bot
        elif user_input in ["how are you", "how are you?"]:
            responses = [
                "I'm fine, thanks!",
                "Doing great! How about you?",
                "All good here!"
            ]
            print("Bot:", random.choice(responses))

        # Help
        elif "help" in user_input:
            print("Bot: I can respond to greetings, 'how are you', and 'bye'.")

        # Name question
        elif "your name" in user_input:
            print("Bot: I am a simple rule-based chatbot.")

        # Time (basic example)
        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print("Bot: Current time is", current_time)

        # Exit
        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break

        # Fallback
        else:
            responses = [
                "Sorry, I don't understand.",
                "Can you rephrase that?",
                "I'm not sure about that."
            ]
            print("Bot:", random.choice(responses))


# Run chatbot
chatbot()