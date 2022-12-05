# This is a sample Python script.
from typing import List
import logging
import argparse
import os

logger = logging.Logger


def load_file(file_name: str, folder_name: str = 'inputs') -> str:
    if folder_name:
        file_path = os.path.join(folder_name, file_name)
    else:
        file_path = file_name
    with open(file_path, 'r') as inputfile:
        result = inputfile.read()
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

def day1(file_path: str):
    delimiter = '\n'
    try:
        input_data = load_file(file_path).splitlines()
        list_of_numbers = get_list_of_numbers(input_data, delimiter)
        biggest_number = get_x_biggest(list_of_numbers, 3)
    except FileNotFoundError as fnf:
        logger.exception(f"Error: file {file_path} not found!")
    return biggest_number


def get_play_score(play: str) -> int:
    plays = {'X': 1, 'Y': 2, 'Z': 3}
    return plays[play]


def get_battle_score(battle: str) -> int:
    battles = {'A': {'X': 3, 'Y': 6, 'Z': 0},
               'B': {'X': 0, 'Y': 3, 'Z': 6},
               'C': {'X': 6, 'Y': 0, 'Z': 3}}
    their_play, my_play = battle.split(' ')
    battle_score = get_play_score(my_play) + battles[their_play][my_play]
    print(battle_score)
    return battle_score




def day2(file_path: str):
    input_data = load_file(file_path).splitlines()
    total_score = 0
    for line in input_data:
        total_score += get_battle_score(line)
    print(total_score)



if __name__ == '__main__':
    parser = argparse.ArgumentParser("AdventOfCode")
    parser.add_argument("input_path", help="Path to the file containing input data", nargs='?',
                        const="day2-a-input.txt", type=str, default="day2-a-input.txt")
    args = (parser.parse_args())
    day2(args.input_path)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
