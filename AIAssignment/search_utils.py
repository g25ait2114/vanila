GOAL_STATE = (1,2,3,4,5,6,7,8,'B')

MOVES = {
    "UP": -3,
    "DOWN": 3,
    "LEFT": -1,
    "RIGHT": 1
}

def blank_index(state):
    return state.index('B')

def is_valid_move(blank, move):
    if move == "LEFT" and blank % 3 == 0: return False
    if move == "RIGHT" and blank % 3 == 2: return False
    if move == "UP" and blank < 3: return False
    if move == "DOWN" and blank > 5: return False
    return True

def apply_move(state, move):
    blank = blank_index(state)
    new_blank = blank + MOVES[move]
    new_state = list(state)
    new_state[blank], new_state[new_blank] = new_state[new_blank], new_state[blank]
    return tuple(new_state)

def parse_input(filename):
    with open(filename) as f:
        lines = f.readlines()
    start = tuple(int(x) if x != 'B' else 'B'
                  for x in lines[0].split()[1:])
    goal = tuple(int(x) if x != 'B' else 'B'
                 for x in lines[1].split()[1:])
    return start, goal
