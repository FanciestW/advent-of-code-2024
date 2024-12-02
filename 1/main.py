def parse_input():
    with open('1/input.txt', 'r') as file:
        list1 = []
        list2 = []
        for line in file:
            num1, num2 = line.strip().split()
            list1.append(int(num1))
            list2.append(int(num2))
        return list1, list2


def part1(list1, list2):
    list1.sort()
    list2.sort()

    total_distance = 0
    for i in range(len(list1)):
        total_distance += abs(list1[i] - list2[i])

    return total_distance

def part2(list1, list2):
    similarity_score = 0
    for number in list1:
        similarity_score += number * list2.count(number)
    return similarity_score

list1, list2 = parse_input()
print(part1(list1, list2))
print(part2(list1, list2))