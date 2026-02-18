import random
import math
from search_utils import *

def ida_star(start, heuristic):
    threshold = heuristic(start)

    def dfs(state, g, threshold, path):
        f = g + heuristic(state)
        if f > threshold:
            return f
        if state == GOAL_STATE:
            return path

        min_excess = float('inf')
        for move in MOVES:
            if is_valid_move(blank_index(state), move):
                next_state = apply_move(state, move)
                if next_state not in path:
                    result = dfs(next_state, g+1, threshold, path+[move])
                    if isinstance(result, list):
                        return result
                    min_excess = min(min_excess, result)
        return min_excess

    while True:
        result = dfs(start, 0, threshold, [])
        if isinstance(result, list):
            return result
        threshold = result


def simulated_annealing(start, heuristic,
                        T=1000, cooling=0.003):

    current = start

    while T > 1:
        if current == GOAL_STATE:
            return current

        move = random.choice(list(MOVES.keys()))
        if is_valid_move(blank_index(current), move):
            next_state = apply_move(current, move)
            delta = heuristic(next_state) - heuristic(current)

            if delta < 0 or random.random() < math.exp(-delta/T):
                current = next_state

        T *= (1 - cooling)

    return current
