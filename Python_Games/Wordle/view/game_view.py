from abc import ABC, abstractmethod

class GameView(ABC):
    def __init__(self, board_view):
        self.board_view = board_view

    def display_board(self):
        self.board_view.display()

    @abstractmethod
    def get_guess(self):
        pass

    @abstractmethod
    def display_rules(self):
        pass
