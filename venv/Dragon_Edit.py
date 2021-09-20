import random
import time
def display_into():
    print('''Перед тобой 2 пещеры.''', end='')
    print()
def choose_cave():
    cave = ''
    while cave != '1' and cave != '2':
        print('В какую пещеру вы пойдете? 1 или 2')
        cave = str(random.randint(1,2))
        print('Компутер отправился в ' + cave)
    return cave
def check_cave(chosen_cave):
    a = 0
    print('Вы приближаетесь к пещере...')
#    time.sleep(2)
    print('Вам страшно...')
#    time.sleep(2)
    print('На вас выпрыгивает большой дракон и...', end='')
    print()
#    time.sleep(2)
    friendly_cave = random.randint(1, 2)
    if chosen_cave == str(friendly_cave):
        print('... Делится с вами сокровищами!')
        a = a + 1
    else:
        print('... Откусывает вам голову!!!')
    return a
i = 0
a = 0
play_again = 'y'
while play_again == 'y' and i != 10:
    i = i + 1
    display_into()
    cave_numder = choose_cave()
    check_cave(cave_numder)
    print('Испытаешь удачу еще раз? (y//n)')
    play_again = 'y'
print(a)