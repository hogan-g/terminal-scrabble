#!/usr/bin/env python3

# tile module:
#
# Classes:
#
# Tile:
#   __init__
#   __str__
#   __eq__
#   __gt__
#   __lt__
#   pretty_print
# 
# TileBag:
#   __init__
#   __str__
#   add_tile
#   remove_tile
#   pop_tile
#   fill
#
# TileRack:
#   __init__
#
#
# Dicts:
#
# tile_info: 
#   key:    letter
#   value:  tuple: points, default count

import random

tile_default = {
        " ":(0, 2), "a":(1, 9), "b":(3, 2), "c":(3, 2), "d":(2, 4), "e":(1, 12), "f":(4, 2), "g":(2, 3), "h":(4, 2), "i":(1, 9), "j":(8, 1), "k":(5, 1), "l":(1, 4), "m":(3, 2), "n":(1, 6), "o":(1, 8), "p":(3, 2), "q":(10, 1), "r":(1, 6), "s":(1, 4), "t":(1, 6), "u":(1, 4), "v":(4, 2), "w":(4, 2), "x":(8, 1), "y":(4, 2), "z":(10, 1)
    }


class Tile():

    def __init__(self, letter):

        self.letter = letter
        self.value = tile_default[letter][0]

    def __str__(self):

        return f'|{self.letter.upper()} {self.value}|'

    def __eq__(self, other):

        return self.letter == other
    
    def __gt__(self, other):
        return self.letter > other
    
    def __lt__(self, other):
        return self.letter < other

    def pretty_print(self) -> str:

        return f'+-+\n|{self.letter.upper()}|\n+-{self.value}'


class TileBag():

    def __init__(self):
        
        self.contents = []

        self.fill()

    def __str__(self):
        
        return f'TileBag object, Tile count: {len(self.contents)}\nTiles:\n{", ".join(map(str, self.contents))}'

    def add_tile(self, letter):

        self.contents.append(Tile(letter))

    def remove_tile(self, letter):

        self.contents.remove(letter)

    def push_tile(self, tile):
        self.contents.append(tile)
        return

    def pop_tile(self):

        return self.contents.pop(random.randint(0, len(self.contents) - 1))

    def fill(self):

        for letter in tile_default.keys():
            for j in range(tile_default[letter][1]): # value tuple index 1: amount of tiles of this letter in default distribution
                self.add_tile(letter)

class TileRack():

    def __init__(self):
        
        self.contents = []

    def __str__(self):
        
        return f'TileBag object\nTiles: {", ".join(map(str, self.contents))}'

    def refill(self, bag):

        while len(self.contents) < 7:
            if len(bag.contents) != 0:
                self.contents.append(bag.pop_tile())
            else:
                break
        
        print("Rack Filled")
    
    def takeout(self, letter):
        for tile in self.contents:
            if tile.letter == letter:
                self.contents.remove(tile)
                break

    
    def shuffle(self):
        random.shuffle(self.contents)
        
        print("Tiles Shuffled")
    
    def swap_out(self, bag):
        while len(self.contents) > 0:
            bag.push_tile(self.contents[0])
            self.contents.remove(self.contents[0])
            
        self.refill(bag)
        return
    
    def sort(self):
        self.contents.sort()
        
        print("Tiles Sorted")

    def pretty_print(self) -> str:

        if len(self.contents) <= 0:
            print("Empty!")
            return

        outstr = (" +-+ " * len(self.contents)) + "\n"
        for t in self.contents:
            outstr += f' |{t.letter.upper()}| '
        outstr += "\n"
        for t in self.contents:
            outstr += f' +-{t.value} '

        return outstr