from collections import deque
from search_utils import *

def bfs(start):
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        state, path = queue.popleft()
        if state == GOAL_STATE:
            return path, len(visited)

        for move in MOVES:
            if is_valid_move(blank_index(state), move):
                next_state = apply_move(state, move)
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, path + [move]))

    return None, len(visited)


def dfs(start, depth_limit=20):
    stack = [(start, [], 0)]
    visited = set([start])

    while stack:
        state, path, depth = stack.pop()

        if state == GOAL_STATE:
            return path, len(visited)

        if depth < depth_limit:
            for move in MOVES:
                if is_valid_move(blank_index(state), move):
                    next_state = apply_move(state, move)
                    if next_state not in visited:
                        visited.add(next_state)
                        stack.append((next_state, path + [move], depth+1))

    return None, len(visited)
