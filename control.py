import puzzle as game
import logic

def state():
    print(logic.game_state(game.game_grid.matrix))
    return logic.game_state(game.game_grid.matrix)