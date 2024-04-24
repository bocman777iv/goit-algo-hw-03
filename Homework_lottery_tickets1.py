import random
def get_numbers_ticket(min_num, max_num, quantity):
    if not (1 <= min_num <= max_num <= 1000 and 1 <= quantity <= (max_num - min_num + 1)):
        return []
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min_num, max_num))
    return sorted(list(numbers))
lottery_numbers = get_numbers_ticket(7, 77, 7)
print("Your lottery numbers:", lottery_numbers)