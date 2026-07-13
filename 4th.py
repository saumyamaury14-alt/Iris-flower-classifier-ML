print("chatbot:hello,i am your chatbot Mimo!!")
while True:
    user = input("you:").lower()
    if user == "hello":
        print("chatbot:let's play a game(number guessing game)")
    print("guess number between 1 to 50:")
    number = 43
    while True:
        guess = int(input("Enter your guessed number"))
        if guess == number:
            print("congratulations,you guessed the right number🥳🥳")
            break
        elif number > guess:
            print("this number is too low")
        else:
            print("this number too high")
            print("chatbot:Thankyou for playing this game😊")    
    else:
        print("chatbot:sorry,i did not understand what you are saying:")
