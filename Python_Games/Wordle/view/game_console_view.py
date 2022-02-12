from view.game_view import GameView

class GameConsoleView(GameView):
    def __init__(self, board_view):
        super().__init__(board_view)
        self.user_guess = ''

    def get_guess(self):
        self.user_guess = input('Enter your guess: ')
        #print(self.user_guess.lower())
        return self.user_guess.lower()

    def display_rules(self):
        print('\nLower case indicates the letter is in\nthe word but in the wrong location.')
        print('Upper case indicates the letter is in\nthe correct location within the word.')
