from model.game import Game
from view.game_view import GameView

class GameController:
    def __init__(self, model: Game, view: GameView):
        self.model = model
        self.view = view
        self.guess = ''

    def run_game(self):
        game_terminated = False
        self.model.get_word()
        self.model.split_word_list()
        while not game_terminated:
            self.view.display_board()
            self.guess = self.view.get_guess()
            self.model.get_guess(self.guess)
            self.model.compare_guess()
            self.view.display_rules()
            game_terminated = self.model.is_game_terminated()
