# Лабораторна робота: Основи Python
import sys
from random import randint

print("=== i. Типи даних ===")
a = "змінна з текстом"
a1 = 'a'
b = 1  # числова змінна
b1 = 1.1
c = ["a", 1, 1.25, "Слово", a]  # List
d = {"a": "Слово", "b": 1, a: b}  # Dict
e = ("a", a)  # Tuple
f = {"ss", a + a1}  # Set
for name, value in [("a", a), ("a1", a1), ("b", b), ("b1", b1),
                    ("c", c), ("d", d), ("e", e)]:
    print(name, "=", value, "->", type(value).__name__)
print("f =", sorted(f), "->", type(f).__name__)

print("\n=== ii. Константи та зарезервовані слова ===")
print("Перша константа: ", True)
print("Друга константа: ", None)
print(f"Як можна так робити вивід? {True}")
print("Версія Python:", sys.version.split()[0])
help("keywords")

print("\n=== iii. Вбудовані функції ===")
print(abs(-12.5), f"є рівним {abs(12.5)}", "і якщо порівняти то: ", abs(-12.5) == abs(12.5))
print("len:", len("Python"), "| max:", max([3, 9, 4]), "| sum:", sum(range(1, 11)))
print("round:", round(3.14159, 2), "| sorted:", sorted([5, 2, 8, 1]))

print("\n=== iv. Цикли ===")
fruits = ["яблуко", "груша", "слива"]
for i in range(len(fruits)):
    print(f"На позиції {i} знаходиться {fruits[i]}")
else:
    print("Цикл for завершився без break")
n = 3
while n > 0:
    print("while: залишилось", n)
    n -= 1

print("\n=== v. Розгалуження ===")
A = randint(0, 1)
print(f"Значить A={A}" if A else "Але може бути що A={}".format(A))
score = 78
if score >= 90:
    print("Оцінка: відмінно")
elif score >= 70:
    print("Оцінка: добре")
else:
    print("Оцінка: потрібно підтягнути")

print("\n=== vi. try -> except -> finally ===")
x = 0
try:
    print("Що буде якщо", 10 / x, "?")
except ZeroDivisionError as err:
    print("Помилка ділення на нуль > ", err)
finally:
    print("Блок finally виконується завжди!")
try:
    int("abc")
except ValueError as err:
    print("Помилка перетворення > ", err)

print("\n=== vii. Контекстний менеджер with ===")
with open("notes.txt", "w", encoding="utf-8") as fw:
    fw.write("Перший рядок\nДругий рядок\nТретій рядок\n")
with open("notes.txt", "r", encoding="utf-8") as fr:
    for num, line in enumerate(fr):
        print(f"{num})> ", line.strip())

print("\n=== viii. Лямбда-функції ===")
def square(x):
    return x * x
square_l = lambda x: x * x
print("Звичайна функція:", square(7), "| лямбда:", square_l(7))
people = [("Оля", 20), ("Іван", 17), ("Марта", 25)]
print("Сортування за віком:", sorted(people, key=lambda p: p[1]))
greet = lambda first, age: f"Мене звати {first}, мені {age:d} років"
print(greet("Єгор", 20))
