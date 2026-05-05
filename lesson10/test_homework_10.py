"""
Тести для файлу tasks.py
Запуск: pytest test_tasks.py
"""
from functions_for_test import *

"""
📝 Завдання 1. Перевірка додавання чисел 
Напиши тест на функцію add(a, b), яка повертає суму двох чисел. 
Створи тест, який перевіряє кілька випадків: додавання додатних, від’ємних і нуля.
"""
def test_add():
    # TODO: додай тести для функції add
   
    assert add(2,3) == 5
    assert add(-1,-5) == -6
    assert add(0,5) == 5
    assert add(0,0) == 0


"""
📝 Завдання 2. Перевірка парності 
Функція is_even(n) повертає True, якщо число парне, інакше False. 
Напиши тести для кількох чисел: парних, непарних, від’ємних.
"""
def test_is_even():
    # TODO: додай тести для функції is_even
    assert is_even(2)==True
    assert is_even(3)==False
    assert is_even(-3)==False
    assert is_even(-8)==True


"""
📝 Завдання 3. Розворот рядка 
Функція reverse_string(s) повинна повертати рядок у зворотному порядку. 
Перевір: звичайний рядок, порожній рядок, рядок з одним символом.
"""
def test_reverse_string():
    # TODO: додай тести для функції reverse_string
    assert reverse_string("abc")=="cba"
    assert reverse_string("")==""
    assert reverse_string("a")=="a"

"""
📝 Завдання 4. Мінімум у списку 
Функція find_min(nums) повертає найменший елемент списку. 
Протестуй для: звичайного списку, списку з одним елементом, списку з від’ємними числами.
"""
def test_find_min():
    # TODO: додай тести для функції find_min
    assert find_min([1, 4, 5])==1
    assert find_min([4])==4
    assert find_min([-1, -4, -5])==-5


"""
📝 Завдання 5. Перевірка підрядка 
Функція contains_substring(s, sub) повертає True, якщо sub є в s. 
Протестуй випадки: підрядок є, підрядка нема, порожній підрядок.
"""
def test_contains_substring():
    # TODO: додай тести для функції contains_substring
    assert contains_substring("safdh", "a")== True
    assert contains_substring("sgfhfg", "adfg")== False
    assert contains_substring("", "s")== False


"""
📝 Завдання 6. Факторіал 
Функція factorial(n) обчислює факторіал числа n. 
Протестуй: factorial(0), factorial(1), factorial(5).
"""
def test_factorial():
    # TODO: додай тести для функції factorial
    assert factorial(0)==1
    assert factorial(1)==1
    assert factorial(5)==120


import pytest
from functions_for_test import divide

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (9, 3, 3),
    (10, -2, -5),
    (-10, -2, 5),
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected

"""
📝 Завдання 7. Ділення з винятком 
Функція divide(a, b) ділить a на b. 
Перевір: звичайне ділення, ділення на від’ємне число, ділення на нуль (очікуваний ZeroDivisionError).
"""
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (9, 3, 3),
    (10, -2, -5),
    (-10, -2, 5),
])

def test_divide(a, b, expected):
    # TODO: додай тести для функції divide
    assert divide(a, b) == expected


"""
📝 Завдання 8. Паліндром 
Функція is_palindrome(s) перевіряє, чи є рядок паліндромом. 
Протестуй: паліндром, непаліндром, порожній рядок.
"""

@pytest.mark.parametrize("a, expected", [
    ("aaa", True),
    ("ab", False),
])

def test_is_palindrome(a, expected):
    # TODO: додай тести для функції is_palindrome
    assert is_palindrome(a) == expected



"""
📝 Завдання 9. Сума елементів списку 
Функція sum_list(nums) повертає суму всіх чисел у списку. 
Протестуй: звичайний список, порожній список, список з від’ємними числами.
"""
@pytest.mark.parametrize("a, expected", [
    ([4, 7, 3], 14),
    ([-4, -7, -3], -14),
])

def test_sum_list(a, expected):
    # TODO: додай тести для функції sum_list
    assert sum_list(a) == expected


"""
📝 Завдання 10. Конвертація в верхній регістр 
Функція to_upper(s) повертає рядок у верхньому регістрі. 
Протестуй: звичайний рядок, вже великими літерами, порожній рядок.
"""
@pytest.mark.parametrize("a, expected", [
    ("aaa", "AAA"),
    ("ab", "AB"),
    ("AB", "AB"),
    ("", ""),
])

def test_to_upper(a, expected):
    # TODO: додай тести для функції to_upper
    assert to_upper(a) == expected
