import re
import numpy as np

word_to_find = 'XMAS'
xmas_reg = rf'(?=({word_to_find}|{word_to_find[::-1]}))'

def read_input():
    with open('4/input.txt', 'r') as file:
        matrix = []
        for line in file:
            matrix.append(list(line.strip()))
    return np.array(matrix)

def part1(matrix) -> int:
    word_count = 0

    height, width = matrix.shape
    cols = [matrix[:,i].tolist() for i in range(width)]
    rows = [matrix[i, :].tolist() for i in range(height)]
    diags = []

    for d in range(-(height - 1), width):
        diags.append(matrix.diagonal(offset=d).tolist())
    
    flipped_matrix = np.fliplr(matrix)
    for d in range(-(height - 1), width):
        diags.append(flipped_matrix.diagonal(offset=d).tolist())

    for i, col in enumerate(cols):
        col_str = ''.join(str(c) for c in col)
        found_words = re.findall(xmas_reg, col_str)
        found_words_count = len(found_words)
        word_count += found_words_count

    for i, row in enumerate(rows):
        row_str = ''.join(str(r) for r in row)
        found_words = re.findall(xmas_reg, row_str)
        found_words_count = len(found_words)
        word_count += found_words_count

    for diag in diags:
        if len(diag) < len(word_to_find):
            continue
        diag_str = ''.join(str(d) for d in diag)
        found_words = re.findall(xmas_reg, diag_str)
        found_words_count = len(found_words)
        word_count += found_words_count

    return word_count

matrix = read_input()
print(part1(matrix))