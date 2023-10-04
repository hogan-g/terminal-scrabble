import rulebook
import player
import tile
import board
import dictionary
import random
import os

class Ui():
    _instance = None
    rules = rulebook.Rulebook()
    dic = dictionary.dictionary()
    players = []
    nPlayers = 0

    def __new__(self):
        if self._instance is None:
            self._instance = super(Ui, self).__new__(self)
        
        return self._instance
    
    def reset(self):
        self.players = []
        self.nPlayers = 0
        del self.bag
        del self.board

    def start_game(self):
        self.bag = tile.TileBag()
        self.board = board.Board(self.players, board.board_default)
        self.setup_players()

    def options(self):
        choice = input("Alright everything is set up, would you like to know the rules first? (Y/N): ")
        if choice.lower() == "y":
            print("Okay, here they are!")
            print("------------------------------------------------------------------")
            print(self.rules)
            print("------------------------------------------------------------------")
            
            input("Press Enter to continue...")
            print("------------------------------------------------------------------")
            print("Alright, let's get this game going then!!!")
            self.start_game
        
        elif choice == 0:
            print("Alright, let's get this game going then!!!")
    
    def take_turn(self, player):
        os.system("clear")
        name = player.nickName
        print(self.board.pretty_print())
        print("------------------------------------------------------------------")
        print(name + " it is your turn! Your Score is: " + str(player.score))
        print("------------------------------------------------------------------")
        print("Your Rack:")
        print(player.rack.pretty_print())
        self.player_options(player)
    
    def player_options(self, player):
        print("------------------------------------------------------------------")
        print("What would you like to do " + player.nickName + " ?")
        print("------------------------------------------------------------------")
        print("1. Sort Tiles")
        print("2. Shuffle Tiles")
        print("3. Swap-Out Tiles (Uses Turn)")
        print("4. Place Word")
        print("------------------------------------------------------------------")
        choice = input("Choice (1-4): ")
        if choice == "1":
            player.rack.sort()
            self.take_turn(player)
        elif choice == "2":
            player.rack.shuffle()
            self.take_turn(player)
        elif choice == "3":
            player.rack.swap_out(self.bag)
            print("Here is your new rack:")
            print(player.rack.pretty_print())
            input("Press Enter to pass turn to next player...")
        elif choice == "4":
            copy_board = self.board
            copy_board = player.place_word(copy_board, self.dic, self.bag)
            self.board = copy_board
        elif choice == "5":
            for i in range(1,85):
                self.bag.contents.pop(random.randint(0, len(self.bag.contents) - 1))
            print(self.bag)
            input("Here is the bag, press enter to continue...")
        else:
            ("Please enter a number option")
            self.take_turn(player)

               

    def setup_players(self):
        for player in self.players:
            player.createRack(self.bag)
            print("Here is your rack " + player.nickName + ":")
            print(player.rack.pretty_print())

    def add_players(self):
        while self.nPlayers != 4:
            name = input("Please enter nickname for Player " + str(self.nPlayers + 1) + ": ")
            newPlayer = player.Player(name)
            
            self.players.append(newPlayer)
            self.nPlayers = len(self.players)
            
            if self.nPlayers >= 2 and self.nPlayers != 4:
                choice = input("Want to add another player? (Y/N): ")
                if choice.lower() == "n":
                    break
        return

    def change_dict():
        pass

    def import_dict():
        pass

    def check_rules(self, num=-1):
        if num == -1:
            print(self.rules)
        elif num > 0 and num < 11:
            self.rules.retrieve(num)

    def quit():
        exit 

