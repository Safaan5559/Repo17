import random
from hints import give_hint
from history import History

class Game:
    def __init__(self, min_number, max_number, player, ui):
        self.min = min_number
        self.max = max_number
        self.player = player
        self.ui = ui
        self.history = History()

    def start(self):
        self.number = random.randint(self.min, self.max)
        self.player.reset_attempts(10)
        self.ui.show_message(f"Guess a number between {self.min} and {self.max}")

        while self.player.attempts_left > 0:
            guess = self.ui.ask_guess()
            if guess == self.number:
                self.ui.show_message("Correct! You win!")
                self.player.score += 1
                break
            else:
                self.player.attempts_left -= 1
                hint = give_hint(guess, self.number)
                self.ui.show_message(f"Wrong! Hint: {hint}")
        else:
            self.ui.show_message(f"Game over! The number was {self.number}")
        self.history.record(self.player, self.number)