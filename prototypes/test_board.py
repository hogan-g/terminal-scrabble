import board

# class Square():

#     def __init__(self, letter=1, word=1) -> None:
    
#         self.tile = None
#         self.letter = letter
#         self.word = word

#     def __str__(self) -> str:
        
#         return f'Tile: {self.tile}\nLetter: x{self.letter}\nWord: x{self.word}'


test_board = board.Board(["player1", "player2"], board.board_default)

print(test_board.pretty_print())
