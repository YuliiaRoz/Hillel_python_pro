# 1. Рядки
from tabnanny import check


def string_length(text):
    return len(text)


def join_strings(text_one, text_two):
    return text_one + text_two


# 2. Числа


def square_number(number):
    return number**2


def sum_number(num1, num2):
    return num1 + num2


def divide_number(num1, num2):
    whole = num1 // num2
    remainder = num1 % num2
    return whole, remainder


# 3. Списки


def average_numbers(numbers):
    return sum(numbers) / len(numbers)


def common_lists(list1, list2):
    return list(set(list1) & set(list2))


# 4. Словники


def show_keys(dictionary):
    return list(dictionary.keys())


def merge_dicts(dict1, dict2):
    return dict1 | dict2


# 5. Множини


def union_sets(set1, set2):
    return set1 | set2


def is_subset(set1, set2):
    return set1.issubset(set2)


# 6. Умови та цикли


def even_or_add(number):
    if number % 2 == 0:
        return "Парне"
    return "Не парне"


def only_even(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result


# 7. Lambda функція

check_even = lambda number: "парне" if number % 2 == 0 else "не парне"

# Перевірка

print(string_length("Hello"))
print(join_strings("Hello", "World"))
print(square_number(6))
print(sum_number(3, 8))
print(divide_number(2, 9))
print(average_numbers([1, 3, 5, 7, 9]))
print(common_lists([1, 3, 5, 7, 9], [2, 4, 6, 8, 9]))
print(show_keys({"a": 1, "b": 2, "c": 3}))
print(merge_dicts({"a": 1, "b": 2, "c": 3}, {"d": 4, "e": 5}))
print(union_sets({1, 3, 5, 9}, {4, 6, 8, 9}))
print(is_subset({5, 7, 9}, {6, 8, 9}))
print(even_or_add(3))
print(only_even([1, 3, 6, 7, 8, 9]))
print(check_even(9))
