# https://github.com/fayrose/Scrabble/blob/master/scrabble.py
# https://note.nkmk.me/en/python-dict-keys-values-items/
# https://pynative.com/python-random-shuffle/
import random
import tile
import os
import board
import dictionary

class Player:
    def __init__(self, nickName):
        self.nickName = nickName
        self.score = 0
    
    def createRack(self, bag): # creates this players rack
        self.rack = tile.TileRack()
        self.rack.refill(bag)
    
    def place_word(self, board, dic, bag):
        coords = []
        word = input("What word do you want to place: ").lower()
        
        if not(dic.check_word(word)): # uses the dictionary to check if the word is valid
            print("That is not a valid word")
            self.place_word(board, dic, bag)
        
        for letter in word: # place the word letter by letter
            check = False
            print(board.pretty_print())
            print("----------------------------------------------")
            print("Where will the " + letter.upper() + " be? X, Y Coords")
            while not check: # take in coordinates for the letter
                x = int(input("X = ")) - 1
                y = int(input("Y = ")) - 1
                y = board.translate(y)

                if coords:
                    check = board.adjacent(x, y, coords[-1]) # check it is next to last placed tile
                    if not check:
                        print("That isn't next to your last placed letter!")
                        print(x, y, coords[-1])
                else:
                    check = True

            if board.placed_tiles[y][x][0] == None: # if the space is empty, place tile and remove from board
                board.placed_tiles[y][x][0] = tile.Tile(letter)
                coords.append((x,y))
                self.rack.takeout(letter)
                print("Placing letter")
            elif board.placed_tiles[y][x][0] != tile.Tile(letter): # if space if full, i.e. using a letter already placed
                print("There is already a letter there")
                self.place_word(board)
            else:
                coords.append((x,y))

        self.rack.refill(bag) # refull after placing down a word
        self.score += board.calc_score(coords)
        return board
