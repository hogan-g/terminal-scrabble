#!/usr/bin/env python3

# board module:
#
#
# Lists:
#
# board_default:
#   rows:
#       Placed tile, Letter multiplier, Word Multiplier


from tile import TileBag
import dictionary
import player

s = [None, 1, 1]
dl = [None, 2, 1]
tl = [None, 3, 1]
dw = [None, 1, 2]
tw = [None, 1, 3]

# sorry
board_default = [
        [[None, 1, 3], [None, 1, 1], [None, 1, 1], [None, 2, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 1, 3], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 2, 1], [None, 1, 1], [None, 1, 1], [None, 1, 3]],
        [[None, 1, 1], [None, 1, 2], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 3, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 3, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 1, 2], [None, 1, 1]],
        [[None, 1, 1], [None, 1, 1], [None, 1, 2], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 2, 1], [None, 1, 1], [None, 2, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 1, 2], [None, 1, 1], [None, 1, 1]],
        [[None, 2, 1], [None, 1, 1], [None, 1, 1], [None, 1, 2], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 2, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 1, 2], [None, 1, 1], [None, 1, 1], [None, 2, 1]],
        [[None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 1, 2], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 1, 2], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1]],
        [[None, 1, 1], [None, 3, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 3, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 3, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 3, 1], [None, 1, 1]],
        [[None, 1, 1], [None, 1, 1], [None, 2, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 2, 1], [None, 1, 1], [None, 2, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 2, 1], [None, 1, 1], [None, 1, 1]],
        [[None, 1, 3], [None, 1, 1], [None, 1, 1], [None, 2, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 2, 1], [None, 1, 1], [None, 1, 1], [None, 1, 3]],
        [[None, 1, 1], [None, 1, 1], [None, 2, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 2, 1], [None, 1, 1], [None, 2, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 2, 1], [None, 1, 1], [None, 1, 1]],
        [[None, 1, 1], [None, 3, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 3, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 3, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 3, 1], [None, 1, 1]],
        [[None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 1, 2], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 1, 2], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1]],
        [[None, 2, 1], [None, 1, 1], [None, 1, 1], [None, 1, 2], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 2, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 1, 2], [None, 1, 1], [None, 1, 1], [None, 2, 1]],
        [[None, 1, 1], [None, 1, 1], [None, 1, 2], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 2, 1], [None, 1, 1], [None, 2, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 1, 2], [None, 1, 1], [None, 1, 1]],
        [[None, 1, 1], [None, 1, 2], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 3, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 3, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 1, 2], [None, 1, 1]],
        [[None, 1, 3], [None, 1, 1], [None, 1, 1], [None, 2, 1], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 1, 3], [None, 1, 1], [None, 1, 1], [None, 1, 1], [None, 2, 1], [None, 1, 1], [None, 1, 1], [None, 1, 3]],
    ]


class Board():

    def __init__(self, players, layout) -> None:

        self.players = players
        self.placed_tiles = layout
        self.turn = 0


    def __str__(self) -> str:
        
        a = "\n"
        return f'Board Object\nPlayers: {", ".join(map(str, self.players))}\nBoard: {a.join(map(str, self.placed_tiles))}'

    def translate(self, y) -> int: # Cartesian grid starts bottom left, matrix 0,0 is at top left
        y = 14 - y
        return y

    def adjacent(self, X, Y, tup):
        X1, Y1 = tup
        if X == X1:
            if (Y == Y1 + 1) or (Y == Y1 - 1):
                return True
        elif Y == Y1:  
            if (X == X1 + 1) or (X == X1 - 1):
                return True           
        else: 
            return False

    def calc_score(self, coords) -> int:
        score = 0
        word_mult = 1
        for tup in coords:
            x, y = tup
            value = self.placed_tiles[y][x][0].value
            letter_mult = self.placed_tiles[y][x][1]
            word_mult = word_mult * self.placed_tiles[y][x][2]

            score += value * letter_mult
        score = score * word_mult
        return score

    
    def pretty_print(self) -> str:

        outstr = ""

        for row in self.placed_tiles:
            for square in row:
                l = f'{square[1]}l' if square[1] > 1 else '+-'
                w = f'{square[2]}w' if square[2] > 1 else '-+'
                outstr += f'{l}-{w} '
            outstr += '\n'

            for square in row:
                if square[0]:
                    outstr += f'|{square[0].letter.upper()}{square[0].value:2}| '
                else:
                    outstr += '|   | '
            outstr += '\n'
            
            for square in row:
                outstr += '+---+ '
            outstr += '\n'

        return outstr