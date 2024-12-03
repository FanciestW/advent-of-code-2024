import re

def process_mul(mul: str) -> int:
    num1, num2 = re.findall(r"\d+", mul)
    return int(num1) * int(num2)

def part1():
    mul_regex = r'mul\(\d+,\d+\)'
    with open('3/input.txt', 'r') as file:
        list_of_mul = []
        mul_sum = 0
        for line in file:
            list_of_mul += re.findall(mul_regex, line.strip())
        for mul in list_of_mul:
            mul_sum += process_mul(mul)
        print(mul_sum)  

def part2():
    mul_regex = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"
    with open('3/input.txt', 'r') as file:
        raw_list_of_mul = []
        mul_sum = 0
        for line in file:
            raw_list_of_mul += re.findall(mul_regex, line.strip())
        filtered_list_of_mul = []
        is_do = True
        for mul in raw_list_of_mul:
            if mul == "don't()":
                is_do = False
            elif mul == "do()":
                is_do = True
            else:
                if is_do:
                    filtered_list_of_mul.append(mul)
        for mul in filtered_list_of_mul:
            mul_sum += process_mul(mul)
        print(mul_sum)

part1()
part2()
