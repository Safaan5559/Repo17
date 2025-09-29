from settings import MIN_NUMBER, MAX_NUMBER
from game import Game
from player import Player
from ui import UI

def main():
    player = Player()
    ui = UI()
    game = Game(MIN_NUMBER, MAX_NUMBER, player, ui)

    ui.show_welcome()
    while True:
        game.start()
        if not ui.ask_play_again():
            break

    ui.show_goodbye()

if __name__ == "__main__":
    main()