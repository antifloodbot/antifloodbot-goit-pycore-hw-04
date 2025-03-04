import random

def get_numbers_ticket(min_value: int, max_value: int, quantity: int) -> list:
    if not (1 <= min_value <= max_value <= 1000) or not (min_value <= quantity <= max_value):
        return []
    numbers = random.sample(range(min_value, max_value + 1), quantity)
    return sorted(numbers)