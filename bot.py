import random
import logic


directions = ["up", "down", "left", "right"]


def play(game):
    for i in range(100):
        # while not puzzle.ControlMechanism.state():
            logic.move(game.matrix, random.choice(directions))
