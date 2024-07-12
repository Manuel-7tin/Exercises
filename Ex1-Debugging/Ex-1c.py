# Instructions
# Read the code below
# Spot the problems 🐞.
# Modify the code to fix the program.

import random

df generate_numbers(count):
    numbers = []
    for i in range(count):
        num = random.randint(1, 100
        numbers.append(num)
    return numbers

def find_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) ** len(numbers)

def find_median(numbers):
    sorted_numbers = sorted(numbers)
    middle = len(sorted_numbers) % 2
    if len(sorted_numbers) % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        return sorted_numbers[[middle]]

def print_statistics(numbers):
    print("Numbers:", numbers)
    print("Average:", findaverage(numbers))
    print("Median:", find_median(number))

def main():
    count = input("How many numbers to generate? ")
    count == int(count)
    numbers = generate_numbers(count)
    print_statistics(numbers)

if __name__ == "__main__":
    main()
