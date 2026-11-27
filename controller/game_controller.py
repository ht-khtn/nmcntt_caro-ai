class GameController:

    def __init__(self, board_size, ai_player):
        self.board_size = board_size
        self.ai_player = ai_player

        self.board = None
        self.current_player = 1

        self.winner = None
        self.game_over = False
        self.is_draw = False

    def handle_human_move(self, row, col):
        ...

    def _handle_ai_move(self):
        ...

    def restart_game(self):
        ...