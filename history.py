class History:
    def __init__(self):
        self.games = []

    def record(self, player, number):
        self.games.append({
            "player": player.name,
            "score": player.score,
            "number": number
        })

    def show_history(self):
        for game in self.games:
            print(game)