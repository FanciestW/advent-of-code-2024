def parse_input():
    lines = []
    with open('2/input.txt', 'r') as file:
        for line in file:
            lines.append(line)
        return lines
    
def is_level_safe(level) -> bool:
    is_safe = True
    isIncreasing = level[0] < level[-1]
    if level[0] == level[-1]:
        return False
    lastNum = level[0]
    is_safe = True
    for num in level[1:]:
        diff = abs(num - lastNum)
        if not (diff > 0 and diff <= 3):
            is_safe = False
            break
        if isIncreasing and lastNum >= num:
            is_safe = False
            break
        elif not isIncreasing and lastNum <= num:
            is_safe = False
            break
        lastNum = num
    return is_safe

def part1(lines):
    safe_count = 0
    for line in lines:
        level = [int(num) for num in line.split()]
        is_safe = is_level_safe(level)
        # print(f'{level}: isSafe: {is_safe}')
        if is_safe:
            safe_count += 1
    return safe_count

def part2(lines):
    safe_count = 0
    for line in lines:
        level = [int(num) for num in line.split()]
        is_safe = False
        if is_level_safe(level):
            safe_count += 1
            continue
        else:
            for i in range(len(level)):
                new_level = level[:i] + level[i+1:]
                if is_level_safe(new_level):
                    safe_count += 1
                    break
            
        # print(f'{level}: isSafe: {is_safe}')
        if is_safe:
            safe_count += 1
    return safe_count

lines = parse_input()
print(part1(lines))
print(part2(lines))