import ui
import os

game = ui.Ui()

def line():
    print("----------------------------------------------")

def setup():
    game.add_players() # asks for names
    os.system("clear")
    game.options()
    os.system("clear")
    game.start_game() # makes board, bag and racks for each player

def replay(): # asks if the players want to play again
    choice = input("Do you want to play again? (Y/N): ")
    if choice.lower() == "y":
        os.system("clear")
        game.reset() # resets all the objects within the game
        # calls the three game functions again
        setup()
        main()
        replay()
    else:
        exit

def main():
    while len(game.bag.contents) != 0: # taking turns loop
        for player in game.players:
            game.take_turn(player)
    print(game.board.pretty_print()) # prints board at end of game
    line()
    print("GAME OVER, BAG WAS EMPTY")
    line()
    for player in game.players: # lists scores of all players
        print(player.nickName + " your score was: " + str(player.score))
        line()

os.system("clear")
print('''
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |    _______   | || |     ______   | || |  _______     | || |      __      | || |   ______     | || |   ______     | || |   _____      | || |  _________   | |
| |   /  ___  |  | || |   .' ___  |  | || | |_   __ \    | || |     /  \     | || |  |_   _ \    | || |  |_   _ \    | || |  |_   _|     | || | |_   ___  |  | |
| |  |  (__ \_|  | || |  / .'   \_|  | || |   | |__) |   | || |    / /\ \    | || |    | |_) |   | || |    | |_) |   | || |    | |       | || |   | |_  \_|  | |
| |   '.___`-.   | || |  | |         | || |   |  __ /    | || |   / ____ \   | || |    |  __'.   | || |    |  __'.   | || |    | |   _   | || |   |  _|  _   | |
| |  |`\____) |  | || |  \ `.___.'\  | || |  _| |  \ \_  | || | _/ /    \ \_ | || |   _| |__) |  | || |   _| |__) |  | || |   _| |__/ |  | || |  _| |___/ |  | |
| |  |_______.'  | || |   `._____.'  | || | |____| |___| | || ||____|  |____|| || |  |_______/   | || |  |_______/   | || |  |________|  | || | |_________|  | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
''')
print(".------------------------.")
print("|  Welcome to Scrabble!  |")
print("'------------------------'")
setup()
main()
replay()