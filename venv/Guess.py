# Это игра угадай число
import random

guessesTaken = 0  # Количество попыток.
guess = 0  # Переменная которую будет вводить пользователь.
print('Введи своё имя:')
myName = input()
number = random.randint(1, 20)
print('Я хочу сыграть с тобой в одну игру… ' + myName + '. Угадывай число от 1 до 20. У тебя 4 попытки.')
for guessesTaken in range(4):
    print('Введи число:')
    guess = input()
    guess = int(guess)  # Приведение введенного числа пользователем к целочисденному типу.
    if guessesTaken == 3:
        break
    if guess < number:
        print('Больше...')
    if guess > number:
        print('Меньше...')
    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Угадал! С ' + guessesTaken + ' раза.')
if guess != number:
    number = str(number)
    print('Игра окончена! Ты проиграл. Я загадывал число ' + number + '.', end='')
