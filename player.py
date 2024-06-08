import math
import random
# from game import *

class Player:
  def __init__(self, letter) -> None:
    #letter is x or o
    self.letter = letter
  
  def get_move(self, game):
    pass


class RandomComputerPlayer(Player):
  def __init__(self, letter) -> None:
    super().__init__(letter)

  def get_move(self, game):
    square = random.choice(game.available_moves())
    return square
  

class HumanPlayer(Player):
  def __init__(self, letter) -> None:
    super().__init__(letter)
  
  def get_move(self, game):
    vaild_square = False
    val = None
    while not vaild_square:
      square = input(self.letter + '\'s turn. Input move (0-8): ')
     # let's check that this is a correct value by trying to cast
     # it to an integer, and if it's not, then we say its invalid
     # if that spot is not available on the board, we also say its invalid
      try:
        #user might put not an iteger
        val = int(square)
        if val not in game.available_moves():
          raise ValueError
        vaild_square = True
      except ValueError:
        print('Invalid square. Try again.')

    return val