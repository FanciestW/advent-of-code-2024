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

def part2(matrix):
    match_count = 0
    word = 'MAS'
    word_regex = rf'({word}|{word[::-1]})'
    for y in range(len(matrix) - len(word) + 1):
        for x in range(len(matrix[y]) - len(word) + 1):
            sub_matrix = matrix[y:y+len(word), x:x+len(word)]
            diag_str = ''.join(list(sub_matrix.diagonal()))
            rev_diag_str = ''.join(list(np.fliplr(sub_matrix).diagonal()))
            is_diag_match = diag_str == word or diag_str == word[::-1]
            is_rev_diag_match = rev_diag_str == word or rev_diag_str == word[::-1]
            if is_diag_match and is_rev_diag_match:
                match_count += 1
    return match_count

matrix = read_input()
print(part1(matrix))
print(part2(matrix))