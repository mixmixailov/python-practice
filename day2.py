# День 2 – Работа со строками (строки, индексы, методы)

# 🔹 ЗАДАЧА 1: Переверни строку
def reverse_string(s):
    return s[::-1]

print("ЗАДАЧА 1:")
print(reverse_string("киберсамурай"))  # йарамусребик


# 🔹 ЗАДАЧА 2: Сделай первую букву заглавной
def capitalize_first(s):
    return s[0].upper() + s[1:]

print("\nЗАДАЧА 2:")
print(capitalize_first("python"))  # Python


# 🔹 ЗАДАЧА 3: Подсчёт гласных
def count_vowels(s):
    vowels = "аеёиоуыэюяAEIOUYaeiouy"
    return sum(1 for char in s if char in vowels)

print("\nЗАДАЧА 3:")
print(count_vowels("привет, кибервоин"))  # Пример: 6

# 🔹 ЗАДАЧА 4: Удаление пробелов
def remove_spaces(s):
    return s.replace(" ", "")

print("\nЗАДАЧА 4:")
print(remove_spaces("я иду домой"))  # Output: "яидудомой"

# 🔹 ЗАДАЧА 5: Палиндром
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print("\nЗАДАЧА 5:")
print(is_palindrome("Казак"))         # True
print(is_palindrome("А роза упала на лапу Азора"))  # True

# 🔹 ЗАДАЧА 6: Самая длинная строка
def longest_string(strings):
    return max(strings, key=len)

print("\nЗАДАЧА 6:")
print(longest_string(["кибер", "самурай", "Python", "интерпретатор"]))  # интерпретатор

