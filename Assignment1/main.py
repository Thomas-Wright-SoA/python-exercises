from io_helpers import ask
from player import Player
from game import play_round

def main():
    if ask("Wanna play a game?") == 'no': exit()

    # initialise player
    name = input("Please enter your name: ").strip()
    player = Player(name)

    # start game
    while True:
        play_round(player)
        if ask("Play another round?") == 'no': exit()

if __name__ == '__main__':
    main()