import numpy as np
from typing import Tuple

guard_chars = ['^', '>', 'v', '<']
obstruction_char = '#'

def find_guard(matrix) -> Tuple[bool, tuple]:
    guards = np.argwhere(np.isin(matrix, guard_chars))
    if guards.size > 0:
        return True, guards[0]
    else:
        return False, [0, 0]
    
def mark_full_path(full_path, guard):
    guard_turn_map = {
        '^': '>',
        '>': 'v',
        'v': '<',
        '<': '^',
    }
    if obstruction_char not in full_path:
        full_path[:] = 'X'
    else:
        obstruction_index = np.argmax(full_path == obstruction_char)
        full_path[:obstruction_index] = 'X'
        full_path[obstruction_index-1] = guard_turn_map[guard]
    return full_path

def move(matrix):
    has_guard, guard_pos = find_guard(matrix)
    if not has_guard:
        return matrix

    guard_x, guard_y = guard_pos
    guard = matrix[guard_x, guard_y]

    if guard == '^':
        full_path = matrix[:guard_x+1,guard_y][::-1]
        marked_full_path = mark_full_path(full_path, guard)
        matrix[:guard_x+1,guard_y] = marked_full_path[::-1]
    elif guard == '>':
        full_path = matrix[guard_x,guard_y:]
        marked_full_path = mark_full_path(full_path, guard)
        matrix[guard_x,guard_y:] = marked_full_path
    elif guard == 'v':
        full_path = matrix[guard_x:,guard_y]
        marked_full_path = mark_full_path(full_path, guard)
        matrix[guard_x:,guard_y] = marked_full_path
    elif guard == '<':
        full_path = matrix[guard_x,:guard_y+1][::-1]
        marked_full_path = mark_full_path(full_path, guard)
        matrix[guard_x,:guard_y+1] = marked_full_path[::-1]
    return move(matrix)

def part1():
    with open('6/input.txt', 'r') as file:
        matrix = np.array([list(line.strip()) for line in file])        
        moved_matrix = move(matrix)
        print(np.count_nonzero(moved_matrix == 'X'))

part1()