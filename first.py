# A simple dummy Python script
import random

def generate_numbers(count, start=1, end=100):
    """Generates a list of specified count of random numbers within a range."""
    numbers = []
    for _ in range(count):
        numbers.append(random.randint(start, end))
        print(f"looping nicely hre")
    return numbers

# Main part of the script
if __name__ == "__main__":
    num_list = generate_numbers(5)
    print(f"Generate numbers list: {num_list}")
    print(f"The first number is: {num_list[0]}")
