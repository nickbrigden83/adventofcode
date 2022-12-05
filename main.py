# This is a sample Python script.
from typing import List
import logging
import argparse

logger = logging.Logger


def load_file(file_path: str) -> List[str]:
    with open(file_path, 'r') as inputfile:
        result = inputfile.readlines()
    return result


def get_list_of_numbers(raw_data: List[str], delimiter: str) -> List[List[int]]:
    all_numbers = []
    individual_numbers = []
    for line in raw_data:
        if line == delimiter:
            all_numbers.append(individual_numbers)
            individual_numbers = []
        else:
            individual_numbers.append(int(line))
    return all_numbers


def sum_numbers(number_list: List[List[int]]) -> List[int]:
    result = []
    for numbers in number_list:
        result.append(sum(numbers))
    return result


def get_x_biggest(number_list: List[List[int]], number_required: int) -> int:
    totals = sum_numbers(number_list)
    sorted_list = sorted(totals, reverse=True)
    return sum(sorted_list[:number_required])

def start(file_path: str):
    delimiter = '\n'
    try:
        input_data = load_file(file_path)
        list_of_numbers = get_list_of_numbers(input_data, delimiter)
        biggest_number = get_x_biggest(list_of_numbers, 3)
    except FileNotFoundError as fnf:
        logger.exception(f"Error: file {file_path} not found!")
    return biggest_number



if __name__ == '__main__':
    parser = argparse.ArgumentParser("AdventOfCode")
    parser.add_argument("input_path", help="Path to the file containing input data", nargs='?',
                        const="day1-a-input.txt", type=str, default="day1-a-input.txt")
    args = (parser.parse_args())
    print(start(args.input_path))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
