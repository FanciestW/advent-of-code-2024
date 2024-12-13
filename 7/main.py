from itertools import product

def evaluate_expression(numbers, operators):
    """
    Evaluates a left-to-right mathematical expression formed by interleaving numbers and operators.

    :param numbers: List of numbers in the equation.
    :param operators: List of operators ("+", "*", or "||") to insert between the numbers.
    :return: The result of the left-to-right evaluation.
    """
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += numbers[i + 1]
        elif operators[i] == "*":
            result *= numbers[i + 1]
        elif operators[i] == "||":
            result = int(str(result) + str(numbers[i + 1]))
    return result

def is_equation_solvable(target, numbers, include_concatenation=False):
    """
    Determines if there is a combination of operators that can make the equation true.

    :param target: Target value of the equation.
    :param numbers: List of numbers in the equation.
    :param include_concatenation: Whether to include the concatenation operator ("||") in the evaluation.
    :return: True if the equation can be solved; otherwise False.
    """
    operators = ["+", "*"]
    if include_concatenation:
        operators.append("||")

    # Generate all possible combinations of operators between the numbers
    operator_combinations = product(operators, repeat=len(numbers) - 1)
    
    # Check each operator combination
    for operators in operator_combinations:
        if evaluate_expression(numbers, operators) == target:
            return True
    return False

def calculate_calibration_result(equations, include_concatenation=False):
    """
    Calculates the total calibration result by summing all test values of solvable equations.

    :param equations: List of tuples (test_value, [numbers]) representing the equations.
    :param include_concatenation: Whether to include the concatenation operator ("||") in the evaluation.
    :return: Total calibration result.
    """
    total = 0
    for target, numbers in equations:
        if is_equation_solvable(target, numbers, include_concatenation):
            total += target
    return total

def read_input_file(filename):
    """
    Reads the input file and parses the equations.

    :param filename: Path to the input file.
    :return: List of tuples (test_value, [numbers]) representing the equations.
    """
    equations = []
    with open(filename, "r") as file:
        for line in file:
            if ":" in line:
                target, nums = line.split(":")
                target = int(target.strip())
                numbers = list(map(int, nums.strip().split()))
                equations.append((target, numbers))
    return equations

# Read input data from the file
input_file = "7/input.txt"
input_data = read_input_file(input_file)

# Part 1: Calculate the result without concatenation
part1_result = calculate_calibration_result(input_data)
print("Part 1 Total Calibration Result:", part1_result)

# Part 2: Calculate the result with concatenation
part2_result = calculate_calibration_result(input_data, include_concatenation=True)
print("Part 2 Total Calibration Result:", part2_result)
