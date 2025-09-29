class UI:
    def show_welcome(self):
        print("Welcome to the Number Guessing Game!")

    def show_goodbye(self):
        print("Thanks for playing!")

    def show_message(self, msg):
        print(msg)

    def ask_guess(self):
        while True:
            try:
                return int(input("Your guess: "))
            except ValueError:
                print("Enter a valid number!")

    def ask_play_again(self):
        answer = input("Play again? (y/n): ").lower()
        return answer == "y"