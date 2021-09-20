import random
import time
def display_into():
    print('''Перед тобой 2 пещеры.''', end='')
    print()
def choose_cave():
    cave = ''
    while cave != '1' and cave != '2':
        print('В какую пещеру вы пойдете? 1 или 2')
        cave = input()
    return cave
def check_cave(chosen_cave):
    print('Вы приближаетесь к пещере...')
    time.sleep(2)
    print('Вам страшно...')
    time.sleep(2)
    print('На вас выпрыгивает большой дракон и...', end='')
    print()
    time.sleep(2)
    friendly_cave = random.randint(1, 2)
    if chosen_cave == str(friendly_cave):
        print('... Делится с вами сокровищами!')
    else:
        print('... Откусывает вам голову!!!')
play_again = 'y'
while play_again == 'y':
    display_into()
    cave_numder = choose_cave()
    check_cave(cave_numder)
    print('Испытаешь удачу еще раз? (y//n)')
    play_again = input()
