import time
from search_utils import parse_input
from bfs_dfs import bfs, dfs
from informed_search import astar, h2_manhattan
from csp_solver import backtrack, domains
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(BASE_DIR, "input.txt")

start, goal = parse_input("input.txt")

print("Running BFS...")
path, explored = bfs(start)
print("Path:", path)
print("States explored:", explored)

print("\nRunning A*...")
path, explored = astar(start, h2_manhattan)
print("Path:", path)
print("States explored:", explored)

print("\nRunning CSP...")
solution = backtrack({}, domains)
print("CSP Solution:", solution)
