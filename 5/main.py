from collections import defaultdict

rules = []
page_rule_map = defaultdict(list)
updates_list = []

with open('5/input.txt', 'r') as file:
    for line in file:
        if '|' in line.strip():
            page, page_rule = line.strip().split('|')
            page_rule_map[page].append(page_rule)
            rules.append(tuple(line.strip().split('|')))
        
        if ',' in line.strip():
            updates_list.append(line.strip().split(','))

good_sum = 0

# Part 1
bad_list = []
for update in updates_list:
    is_bad_update = False
    for pos, page in enumerate(update):
        pages_before = update[:pos]
        if any(pg in pages_before for pg in page_rule_map[page]):
            is_bad_update = True
            break
    if not is_bad_update:
        mid_num = int(update[(len(update) - 1)//2])
        good_sum += mid_num
    else:
        bad_list.append(update)

print(good_sum)

# Part 2
for update in bad_list:
    for pos, page in enumerate(update):
        pages_before = update[:pos]

def arrange_update(update):
    position = {num: 0 for num in update}
    for a, b in rules:
        if a in position and b in position:
            position[b] += 1

    return sorted(update, key=lambda x: position[x])

# Example usage
bad_sum = 0
for update in bad_list:
    good_update = arrange_update(update)
    bad_sum += int(good_update[(len(good_update)-1)//2])
print(bad_sum)