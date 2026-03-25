adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while 
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# УВАГА! Перезаписуйте вміст змінної adwentures_of_tom_sawer у завданнях 01-03
print(adwentures_of_tom_sawer)
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print("------------------------------------------------")
print("Task 01:")
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
print("------------------------------------------------")
print("Task 02:")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print("------------------------------------------------")
print("Task 03:")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.strip()
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("   ", " ")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("  ", " ")
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скільки разів у тексті зустрічається літера "h"
"""
print("------------------------------------------------")
print("Task 04:")
print(adwentures_of_tom_sawer.count("h"))


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
підказка - порахувати кожну велику літеру алфавіту, .count("A") і їх сумму
"""
print("------------------------------------------------")
print("Task 05:")
capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
capital_word_count = sum(adwentures_of_tom_sawer.count(letter) for letter in capital_letters)
print(capital_word_count)   


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print("------------------------------------------------")
print("Task 06:")
print(adwentures_of_tom_sawer.find("Tom", adwentures_of_tom_sawer.find("Tom") + 1)) 


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
print("------------------------------------------------")
print("Task 07:")
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("------------------------------------------------")
print("Task 08:")
print(adwentures_of_tom_sawer_sentences[3].lower()) 


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("------------------------------------------------")
print("Task 09:")
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.strip().startswith("By the time"):
        print("Знайдено речення, яке починається з 'By the time':", sentence.strip())
        break
else:
    print("Речення, яке починається з 'By the time', не знайдено.")


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("------------------------------------------------")
print("Task 10:")
last_sentence = adwentures_of_tom_sawer_sentences[-1].strip()
word_count = len(last_sentence.split())
print("Кількість слів в останньому реченні:", word_count)   