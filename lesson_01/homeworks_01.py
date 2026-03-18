# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02  == Виправте назви змінних, щоб текст виводався
hello = "Hello"
world = "world"
print(f"{hello} {world}!")

# task 03 == Зробіть так, щоб кількість бананів була
# завжди на чотири штуки більша, ніж яблук
apples = 2
banana = apples + 4


# task 04 == виправте назви змінних
side1 = 1
side2 = 2
side3 = 3
side4 = 4

# task 05 == Порахуйте периметр фігури з task 04
# та виведіть його для користувача
perimeter = side1 + side2 + side3 + side4
print(perimeter)


"""
    # Задачі 06 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""

# task 06
"""
У Оксани було 20 марок із серії «Мистецтво» 
і 7 марок із серії «Звірі».
5 марок із серії «Мистецтво» та
1 марку із серії «Звірі» вона подарувала подружці. 
Скільки марок лишилось у Оксани?
"""
stamp_art=20
stamp_animals=7
gift_art=5
gift_animals=1
left_art=stamp_art-gift_art
left_animals=stamp_animals-gift_animals
total_left=left_art+left_animals
print(f"У Оксани залишилось {total_left} марок")


# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
number_apple=4
number_pear=number_apple+5
number_plum=number_apple-2
total_trees=number_apple+number_pear+number_plum
print(f"У саду посадили {total_trees} дерев")


# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""

tempterature_before_lunch=5
temperature_after_lunch=tempterature_before_lunch-10
temperature_in_the_evening=temperature_after_lunch+4
print(f"Температура надвечір була {temperature_in_the_evening} градус

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
number_boys=24
number_girls=number_boys/2
sick_boy=1
absent_girls=2
present_boys=number_boys-sick_boy
present_girls=number_girls-absent_girls
total_present=present_boys+present_girls
print(f"Сьогодні у театральному гуртку {total_present} дітей")


# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
price_first=8
price_second=price_first+2
price_third=(price_first+price_second)/2
total_cost=price_first+price_second+price_third
print(f"Усі книги будуть коштувати {total_cost} грн.")