from controller.game_controller import GameController
from ui.app import CaroApp

BOARD_SIZE = 15


def main():
    controller = GameController(BOARD_SIZE)
    app = CaroApp(controller)

    app.run()