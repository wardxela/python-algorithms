def over_twenty_one(cards):
    total = 0
    for card in cards:
        if type(card) == int:
            total += card
        elif card in ['В', 'Д', 'К']:
            total += 10
        elif card == 'T':
            total += 1
    return total > 21


print(over_twenty_one([2, 8, "В"]))

print(over_twenty_one(["Т", "В", "К"]))

print(over_twenty_one([5, 5, 3, 9]))

print(over_twenty_one([2, 6, 4, 4, 5]))

print(over_twenty_one(["В", "Д", "К"]))
