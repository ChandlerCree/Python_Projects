from view.board_view import BoardView

class BoardConsoleView(BoardView):
    def __init__(self, board):
        super().__init__(board)

    def display(self):
        print('-' * 30)