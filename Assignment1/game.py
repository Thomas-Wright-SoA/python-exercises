import random
from game_settings import MAX_NUMBERS, BASE_PRIZE, BONUS_MULTIPLIER, NUMBER_RANGE
from io_helpers import get_int_in_range

# gets [n] unique numbers within [number_range] from user
# returns a list of inputted numbers
def get_numbers(n, num_range):
    numbers = []
    for i in range(n):
        number = None
        while True:
            number = get_int_in_range(f"{i + 1}: ", num_range)
            if number in numbers:
                print("You've already chose that one")
                continue
            break
        numbers.append(number)
    return numbers

# returns a list of [n] unique random numbers that are within [number_range]
def generate_numbers(n, number_range):
    numbers = []
    for i in range(n):
        number = None
        while (not number) or (number in numbers):
            number = random.randint(min(number_range), max(number_range))
        numbers.append(number)
    return numbers

# compares two lists returning the number of matching values
def check_matches(list_1, list_2):
    count = 0
    for number in list_1:
        if number in list_2:
            count += 1
    return count

# calculate the prize, apply MULTIPLIER's effect per increase in percentage of matches
def calculate_prize(matches):
        base_prize = matches * BASE_PRIZE

        percentage_correct = matches / MAX_NUMBERS

        multiplier = 1 + percentage_correct * (BONUS_MULTIPLIER - 1)

        prize = base_prize * multiplier

        return prize

# I think this one is self explanatory?
def play_round(player):
        print(f"Enter {MAX_NUMBERS} unique numbers")

        players_numbers = get_numbers(MAX_NUMBERS, NUMBER_RANGE)

        computers_numbers = generate_numbers(MAX_NUMBERS, NUMBER_RANGE)

        matches = check_matches(players_numbers, computers_numbers)

        print(f"You got {matches} out of {MAX_NUMBERS} correct")
        
        if matches:
            prize = calculate_prize(matches)

            player.balance += prize

            print(f"You win £{prize:.2f}")

            player.add_xp(matches)
        else:
            print("Better luck next time...")

        print(player.stats())