import os
from pytimedinput import timedInput
from random import randint
from colorama import Fore, init

def draw_border():
    for cell in CELLS:
        if cell in snake:
            print(Fore.LIGHTGREEN_EX + 'o', end = '')
        elif cell[0] in (0, BORDER_WIDTH - 1) or cell[1] in (0, BORDER_HEIGHT - 1):
            print('#', end = '')
        elif cell == food:
            print(Fore.LIGHTYELLOW_EX + 'f', end = '')
        else:
            print(' ', end = '')

        if cell[0] == BORDER_WIDTH - 1:
            print('')

def update_snake():
    global food_eaten
    head = snake[0][0] + direction[0], snake[0][1] + direction[1]
    snake.insert(0, head)
    if not food_eaten:
        snake.pop(-1)
    food_eaten = False

def food_collision():
    global food, food_eaten, score
    if food == snake[0]:
        food = new_food()
        food_eaten = True
        score += 1

def new_food():
    x = randint(1, BORDER_WIDTH - 2)
    y = randint(1, BORDER_HEIGHT - 2)
    while (x, y) in snake:
        x = randint(1, BORDER_WIDTH - 2)
        y = randint(1, BORDER_HEIGHT - 2)
    return (x, y)

init(autoreset = True)

BORDER_WIDTH = 32
BORDER_HEIGHT = 16
CELLS = [(col, row) for row in range(BORDER_HEIGHT) for col in range(BORDER_WIDTH)]

snake = [(5, 5), (5, 4), (5, 3)]
DIRECTIONS = {'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0)}
direction = DIRECTIONS['down']

food = new_food()
food_eaten = False

score = 0

game_speed = 2

while True:
    os.system('clear')

    draw_border()

    print('score:', Fore.LIGHTGREEN_EX + str(score))

    input, _ = timedInput('input: ', timeout = game_speed * .1)
    match input:
        case 'w': direction = DIRECTIONS['up']
        case 's': direction = DIRECTIONS['down']
        case 'a': direction = DIRECTIONS['left']
        case 'd': direction = DIRECTIONS['right']

    update_snake()
    food_collision()

    if snake[0][0] in (0, BORDER_WIDTH - 1) or \
        snake[0][1] in (0, BORDER_HEIGHT - 1) or \
        snake[0] in snake[1:]:
        print(Fore.LIGHTRED_EX + 'game over.')
        break
