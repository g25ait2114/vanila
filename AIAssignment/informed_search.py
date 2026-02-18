import heapq
from search_utils import *

def h1_misplaced(state):
    return sum(1 for i in range(9)
               if state[i] != GOAL_STATE[i] and state[i] != 'B')

def h2_manhattan(state):
    dist = 0
    for i in range(9):
        if state[i] != 'B':
            goal_i = GOAL_STATE.index(state[i])
            dist += abs(i//3 - goal_i//3) + abs(i%3 - goal_i%3)
    return dist


def greedy_best_first(start, heuristic):
    pq = []
    visited = set()
    counter = 0  # tie-breaker

    heapq.heappush(pq, (heuristic(start), counter, start, []))
    counter += 1

    while pq:
        _, _, state, path = heapq.heappop(pq)

        if state == GOAL_STATE:
            return path, len(visited)

        if state in visited:
            continue

        visited.add(state)

        for move in MOVES:
            if is_valid_move(blank_index(state), move):
                next_state = apply_move(state, move)
                heapq.heappush(
                    pq,
                    (heuristic(next_state),
                     counter,
                     next_state,
                     path + [move])
                )
                counter += 1

    return None, len(visited)


def astar(start, heuristic):
    pq = []
    visited = set()
    counter = 0   # tie-breaker

    heapq.heappush(pq, (heuristic(start), 0, counter, start, []))
    counter += 1

    while pq:
        f, g, _, state, path = heapq.heappop(pq)

        if state == GOAL_STATE:
            return path, len(visited)

        if state in visited:
            continue

        visited.add(state)

        for move in MOVES:
            if is_valid_move(blank_index(state), move):
                next_state = apply_move(state, move)
                heapq.heappush(
                    pq,
                    (g + 1 + heuristic(next_state),
                     g + 1,
                     counter,
                     next_state,
                     path + [move])
                )
                counter += 1

    return None, len(visited)