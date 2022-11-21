def is_isogram(text):
    return len(text) == len(set(text.lower()))


print(is_isogram("Algorism"),  '➞ True')
print(is_isogram("PasSword"),  '➞ False')  # Регистр не имеет значения.
print(is_isogram("Consecutive"),  '➞ False')
