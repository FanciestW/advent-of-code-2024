from itertools import product

def evaluate_expression(numbers, operators):
    """
    Evaluates a left-to-right mathematical expression formed by interleaving numbers and operators.

    :param numbers: List of numbers in the equation.
    :param operators: List of operators ("+" or "*") to insert between the numbers.
    :return: The result of the left-to-right evaluation.
    """
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += numbers[i + 1]
        elif operators[i] == "*":
            result *= numbers[i + 1]
    return result

def is_equation_solvable(target, numbers):
    """
    Determines if there is a combination of operators that can make the equation true.

    :param target: Target value of the equation.
    :param numbers: List of numbers in the equation.
    :return: True if the equation can be solved; otherwise False.
    """
    # Generate all possible combinations of + and * operators between the numbers
    operator_combinations = product(["+", "*"], repeat=len(numbers) - 1)
    
    # Check each operator combination
    for operators in operator_combinations:
        if evaluate_expression(numbers, operators) == target:
            return True
    return False

def calculate_calibration_result(equations):
    """
    Calculates the total calibration result by summing all test values of solvable equations.

    :param equations: List of tuples (test_value, [numbers]) representing the equations.
    :return: Total calibration result.
    """
    total = 0
    for target, numbers in equations:
        if is_equation_solvable(target, numbers):
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

# Calculate the result
result = calculate_calibration_result(input_data)
print("Total Calibration Result:", result)