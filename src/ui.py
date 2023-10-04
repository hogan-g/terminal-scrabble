import rulebook
import player
import tile
import board
import dictionary
import random
import os

class Ui():
    _instance = None
    rules = rulebook.Rulebook() # rulebook of the game
    dic = dictionary.dictionary() # dictionary of the game
    players = [] # list to contain player objects
    nPlayers = 0

    def __new__(self): # singleton pattern
        if self._instance is None:
            self._instance = super(Ui, self).__new__(self)
        
        return self._instance
    
    def reset(self): # reset all objects
        self.players = [] # empty the list
        self.nPlayers = 0
        del self.bag # delete board and bag
        del self.board

    def start_game(self): # to start the game make a board, and tilebag, then setup players
        self.bag = tile.TileBag()
        self.board = board.Board(self.players, board.board_default)
        self.setup_players()

    def options(self): # options to show players before starting game
        choice = input("Alright everything is set up, would you like to know the rules first? (Y/N): ")
        if choice.lower() == "y":
            print("Okay, here they are!")
            print("------------------------------------------------------------------")
            print(self.rules)
            print("------------------------------------------------------------------")
            
            input("Press Enter to continue...")
            print("------------------------------------------------------------------")
            print("Alright, let's get this game going then!!!")
            self.start_game()
        
        elif choice == 0:
            print("Alright, let's get this game going then!!!")
    
    def take_turn(self, player): # take a turn player
        os.system("clear")
        name = player.nickName
        print(self.board.pretty_print()) # print the board
        print("------------------------------------------------------------------")
        print(name + " it is your turn! Your Score is: " + str(player.score)) # show their name and score
        print("------------------------------------------------------------------")
        print("Your Rack:")
        print(player.rack.pretty_print()) # show their rack
        self.player_options(player) # show them the options they can choose
    
    def player_options(self, player): # options players can do each turn
        print("------------------------------------------------------------------")
        print("What would you like to do " + player.nickName + " ?")
        print("------------------------------------------------------------------")
        print("1. Sort Tiles")
        print("2. Shuffle Tiles")
        print("3. Swap-Out Tiles (Uses Turn)")
        print("4. Place Word")
        print("------------------------------------------------------------------")
        choice = input("Choice (1-4): ")
        if choice == "1": # switch case
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
        elif choice == "4": # place the word, make a copy of board to place word on, only update real board when done
            copy_board = self.board
            copy_board = player.place_word(copy_board, self.dic, self.bag)
            self.board = copy_board
        else:
            ("Please enter a number option")
            self.take_turn(player)   

    def setup_players(self): # for each player, make their rack
        for player in self.players:
            player.createRack(self.bag)
            print("Here is your rack " + player.nickName + ":")
            print(player.rack.pretty_print())

    def add_players(self): # first screen shown, where they are asked for their names
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

