def duplicate_count(text):
    letter_count = {}
    total = 0
    for letter in text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    for i in letter_count:
        if letter_count[i] > 1:
            total += 1
    return total


print(duplicate_count("abcde"))
print(duplicate_count("aabbcde"))
print(duplicate_count("Indivisibilities"))
print(duplicate_count("Aa"))
