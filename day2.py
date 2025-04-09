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