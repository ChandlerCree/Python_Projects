from re import L
import numpy as np
from model.player import Player

class Game:
    def __init__(self, board_size):
        self.board = np.zeros((board_size, board_size), dtype=np.int)
        self.curr_player = Player.X
    
    def is_legal_move(self, row, col):
        if row < 0 or row >= len(self.board):
            return False
        if col < 0 or col >= len(self.board):
            return False
        if self.board[row, col] != 0:
            return False
        return True

    def make_move(self, row, col):
        self.board[row, col] = int(self.curr_player)

    def is_game_temrminated(self):
        return self.has_player_won() or self.is_board_full()

    def has_player_won(self):
        player = int(self.curr_player)
        if np.any(np.all(self.board == player, axis=0)):
            return True
        if np.any(np.all(self.board == player, axis=1)):
            return True
        main_diag = np.diag_indices(len(self.board))
        secondary_diag = (main_diag[0], main_diag[1][::-1])
        if np.all(self.board[main_diag] == player):
            return True
        if np.all(self.board[secondary_diag] == player):
            return True
        return False
    
    def is_board_full(self):
        return not np.any(self.board == 0)

    def change_turn(self):
        #changes 1 to 2 and 2 to 1 for player
        self.curr_player = Player(len(Player) + 1 - self.curr_player)

    def get_winner(self):
        if self.has_player_won():
            return self.curr_player
        else:
            return 0 #TIE