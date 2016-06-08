from tkinter import *
from random import randint

map = [
[0,0,0,1,0,1,0,0,0,0],
[0,0,0,1,0,1,0,1,1,0],
[0,1,1,1,0,1,0,1,1,0],
[0,0,0,0,0,1,0,0,0,0],
[1,1,1,1,0,1,1,1,1,0],
[0,1,0,1,0,0,0,0,1,0],
[0,1,0,1,0,1,1,0,1,0],
[0,0,0,0,0,1,1,0,1,0],
[0,1,1,1,0,0,0,0,1,0],
[0,0,0,1,0,1,1,0,1,0],
[0,1,0,1,0,1,0,0,0,0]
]

board_width = 10
board_height = 11

def first_map():
    tiles = []
    for i in range(board_height):
        for j in range(board_width):
            if map[i][j] == 0:
                tiles.append(Tile(j, i, 'floor', True))
            else:
                tiles.append(Tile(j, i, 'wall', False))
    return tiles

def hero_starting_stats():
    hp = 20 + 3 * randint(1,6)
    dp = 2 * randint(1,6)
    sp = 5 + randint(1,6)
    return Hero(0, 0, 1, hp, dp, sp)

def skeleton_starting_stats(x, y, has_key):
    hp = 2 * randint(1,6)
    dp = 1 / 2 * randint(1,6)
    sp = randint(1,6)
    return Skeleton(x, y, 1, hp, dp, sp, has_key)

def boss_starting_stats(x,y):
    hp = 2 * randint(1,6) + randint(1,6)
    dp = 1 / 2 * randint(1,6) + randint(1,6) / 2
    sp = randint(1,6) + 1
    return Boss(x, y, 1, hp, dp, sp)

class GameBoard(object):
    def __init__(self):
        self.tiles = first_map()
        self.hero = hero_starting_stats()
        self.enemies = []
        self.enemies.append(skeleton_starting_stats(4, 3, False))
        self.enemies.append(skeleton_starting_stats(4, 8, True))
        self.enemies.append(skeleton_starting_stats(7, 8, False))
        self.enemies.append(boss_starting_stats(6,3))

    def screen_draw(self, canvas):
        canvas.delete('all')
        for x in range(len(self.tiles)):
            self.tiles[x].draw(canvas)
        for y in range(len(self.enemies)):
            self.enemies[y].draw(canvas)
        self.hero.draw(canvas)
        self.hero.stat_print(canvas, 1)
        for i in self.enemies:
            if self.hero.x == i.x and self.hero.y == i.y:
                i.stat_print(canvas, 2)

    def keyboard_event_controller(self, event, canvas):
        if event == 39 and self.can_move(self.hero, 0, 1):
            self.hero.move('down')
        if event == 25 and self.can_move(self.hero, 0, -1):
            self.hero.move('up')
        if event == 38 and self.can_move(self.hero, -1, 0):
            self.hero.move('left')
        if event == 40 and self.can_move(self.hero, 1, 0):
            self.hero.move('right')
        self.screen_draw(canvas)

    def can_move(self, who, direction_x, direction_y):
        for i in self.tiles:
            if i.x == (who.x + direction_x) and i.y == (who.y + direction_y) and i.accessible == True:
                return True
        return False

class Drawable(object):
    def draw(self, canvas):
        canvas.create_image(self.x * 72, self.y * 72, image = self.image, anchor = NW)

    def stat_print(self, canvas, wich_row):
        canvas.create_text(board_width * 72 / 2, board_height * 72 + wich_row * 20, text = self.stat())

class Tile(Drawable):
    def __init__(self, x, y, type_of_tile, accessible):
        self.x = x
        self.y = y
        self.type_of_tile = type_of_tile
        self.accessible = accessible
        if type_of_tile == 'floor':
            self.image = PhotoImage(file='floor.png')
        elif type_of_tile == 'wall':
            self.image = PhotoImage(file='wall.png')

class Character(object):
    def __init__(self, x, y, level, hp, dp, sp):
        self.x = x
        self.y = y
        self.level = level
        self.hp = hp
        self.dp = dp
        self.sp = sp

    def stat(self):
        return (self.name + ' (Level ' + str(self.level) + ') HP: ' + str(self.hp) + '/' + str(self.full_hp) + ' | DP: ' + str(self.dp) +' | SP: ' + str(self.sp))

class Hero(Drawable, Character):
    def __init__(self, x, y, level, hp, dp, sp):
        Character.__init__(self, x, y, level, hp, dp, sp)
        self.image = PhotoImage(file='hero-down.png')
        self.name = 'Hero'
        self.full_hp = hp

    def move(self, direction):
        if direction == 'down':
            self.image = PhotoImage(file='hero-down.png')
            self.y += 1
        if direction == 'up':
            self.image = PhotoImage(file='hero-up.png')
            self.y -= 1
        if direction == 'left':
            self.image = PhotoImage(file='hero-left.png')
            self.x -= 1
        if direction == 'right':
            self.image = PhotoImage(file='hero-right.png')
            self.x += 1

class Skeleton(Drawable, Character):
    def __init__(self, x, y, level, hp, dp, sp, has_the_key):
        Character.__init__(self, x, y, level, hp, dp, sp)
        self.image = PhotoImage(file='skeleton.png')
        if has_the_key == True:
            self.has_the_key = True
        else:
            self.has_the_key = False
        self.name = 'Skeleton'
        self.full_hp = hp

class Boss(Drawable, Character):
    def __init__(self, x, y, level, hp, dp, sp):
        Character.__init__(self, x, y, level, hp, dp, sp)
        self.image = PhotoImage(file='boss.png')
        self.name = 'Boss'
        self.full_hp = hp
