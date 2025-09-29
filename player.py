class Player:
    def __init__(self):
        self.name = ""
        self.score = 0
        self.attempts_left = 0

    def reset_attempts(self, max_attempts):
        self.attempts_left = max_attempts