from search_utils import *
from informed_search import h2_manhattan

def minimax(state, depth, is_max):
    if depth == 0 or state == GOAL_STATE:
        return -h2_manhattan(state)

    if is_max:
        best = -float('inf')
        for move in MOVES:
            if is_valid_move(blank_index(state), move):
                best = max(best,
                           minimax(apply_move(state, move),
                                   depth-1, False))
        return best
    else:
        best = float('inf')
        for move in MOVES:
            if is_valid_move(blank_index(state), move):
                best = min(best,
                           minimax(apply_move(state, move),
                                   depth-1, True))
        return best


def alphabeta(state, depth, alpha, beta, is_max):
    if depth == 0 or state == GOAL_STATE:
        return -h2_manhattan(state)

    if is_max:
        for move in MOVES:
            if is_valid_move(blank_index(state), move):
                alpha = max(alpha,
                            alphabeta(apply_move(state, move),
                                      depth-1, alpha, beta, False))
                if alpha >= beta:
                    break
        return alpha
    else:
        for move in MOVES:
            if is_valid_move(blank_index(state), move):
                beta = min(beta,
                           alphabeta(apply_move(state, move),
                                     depth-1, alpha, beta, True))
                if beta <= alpha:
                    break
        return beta
