# main.py

import time
import os

# Import search modules
from search_utils import parse_input
from bfs_dfs import bfs, dfs
from informed_search import astar, greedy_best_first, h1_misplaced, h2_manhattan
from advanced_search import ida_star, simulated_annealing
from adversarial_search import minimax, alphabeta
from csp_solver import backtrack, domains


# ---------------------------
# Load input safely
# ---------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(BASE_DIR, "input.txt")

start, goal = parse_input(input_path)


# ---------------------------
# Helper function for display
# ---------------------------
def run_search(name, func, *args):
    print(f"\nRunning {name}...")
    start_time = time.time()

    result = func(*args)

    end_time = time.time()
    duration = round(end_time - start_time, 4)

    if isinstance(result, tuple):
        path, explored = result
        print("Status:", "SUCCESS" if path else "FAILURE")
        print("Path:", path)
        print("Moves:", len(path) if path else 0)
        print("States explored:", explored)
    else:
        print("Result:", result)

    print("Time taken:", duration, "seconds")


# ===========================
# RUN ALL SEARCH ALGORITHMS
# ===========================

# --- Uninformed Search ---
run_search("BFS", bfs, start)
run_search("DFS (Depth Limit = 20)", dfs, start, 20)

# --- Informed Search ---
run_search("Greedy (Misplaced Tiles)", greedy_best_first, start, h1_misplaced)
run_search("Greedy (Manhattan)", greedy_best_first, start, h2_manhattan)
run_search("A* (Misplaced Tiles)", astar, start, h1_misplaced)
run_search("A* (Manhattan)", astar, start, h2_manhattan)

# --- Memory Bounded ---
run_search("IDA* (Manhattan)", ida_star, start, h2_manhattan)
run_search("Simulated Annealing (Manhattan)", simulated_annealing, start, h2_manhattan)

# --- Adversarial Search ---
print("\nRunning Minimax (Depth=3)...")
print("Minimax value:", minimax(start, 3, True))

print("\nRunning Alpha-Beta (Depth=3)...")
print("Alpha-Beta value:", alphabeta(start, 3, float('-inf'), float('inf'), True))


# ===========================
# RUN CSP
# ===========================

print("\nRunning CSP Solver (MRV + Forward Checking)...")
start_time = time.time()

solution = backtrack({}, domains)

end_time = time.time()

print("Status:", "SUCCESS" if solution else "FAILURE")
print("Final Assignment:", solution)
print("Time Taken:", round(end_time - start_time, 4), "seconds")
