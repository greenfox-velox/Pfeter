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
                tiles.append(FloorTile(j, i))
            else:
                tiles.append(WallTile(j, i))
    return tiles

class GameBoard(object):
    def __init__(self):
        self.tiles = first_map()
        self.hero = Hero(0, 0)
        self.enemies = []
        self.enemies.append(Skeleton(4, 3))
        self.enemies.append(Skeleton(4, 8, True))
        self.enemies.append(Skeleton(7, 8))
        self.enemies.append(Boss(6,3))

    def screen_draw(self, canvas):
        canvas.delete('all')
        for x in range(len(self.tiles)):
            self.tiles[x].draw(canvas)
        for y in range(len(self.enemies)):
            self.enemies[y].draw(canvas)
        self.hero.draw(canvas)
        self.hero.stat_print(canvas, 1)
        if self.overlap_a_character() != 0:
            self.overlap_a_character().stat_print(canvas, 2)

    def keyboard_event_controller(self, event, canvas):
        if event == 39 and self.can_move(self.hero, 0, 1):
            self.hero.move('down')
        if event == 25 and self.can_move(self.hero, 0, -1):
            self.hero.move('up')
        if event == 38 and self.can_move(self.hero, -1, 0):
            self.hero.move('left')
        if event == 40 and self.can_move(self.hero, 1, 0):
            self.hero.move('right')
        if event == 65 and self.overlap_a_character() != 0:
            self.hero.strike(self.overlap_a_character())
            self.overlap_a_character().strike(self.hero)
        self.screen_draw(canvas)

    def overlap_a_character(self):
        for overlapped_character in self.enemies:
            if self.hero.x == overlapped_character.x and self.hero.y == overlapped_character.y:
                return(overlapped_character)
        return 0

    def can_move(self, who, direction_x, direction_y):
        for i in self.tiles:
            if i.x == (who.x + direction_x) and i.y == (who.y + direction_y) and i.accessible:
                return True
        return False

class RollStats(object):
    def roll_stats(self, hp_base = 0, hpc = 1, dp_base = 0, dpc = 1, sp_base = 0, spc = 1):
        self.hp = hp_base + hpc * randint(1,6)
        self.dp = dp_base + dpc * randint(1,6)
        self.sp = sp_base + spc * randint(1,6)

class Drawable(object):
    def __init__(self, x, y):
            self.x = x
            self.y = y

    def draw(self, canvas):
        canvas.create_image(self.x * 72, self.y * 72, image = self.image, anchor = NW)

    def stat_print(self, canvas, wich_row):
        canvas.create_text(board_width * 72 / 2, board_height * 72 + wich_row * 20, text = self.stat())

class WallTile(Drawable):
    def __init__(self, x, y):
        Drawable.__init__(self, x, y)
        self.accessible = False
        self.image = PhotoImage(file='wall.png')

class FloorTile(Drawable):
    def __init__(self, x, y):
        Drawable.__init__(self, x, y)
        self.accessible = True
        self.image = PhotoImage(file='floor.png')

class Character(object):
    def stat(self):
        return (self.name + ' (Level ' + str(self.level) + ') HP: ' + str(self.hp) + '/' + str(self.full_hp) + ' | DP: ' + str(self.dp) +' | SP: ' + str(self.sp))

    def strike(self, enemy):
        sv = self.sp + randint(1,6) * 2
        if sv > enemy.dp:
            enemy.hp -= sv - enemy.dp

class Hero(Drawable, Character):
    def __init__(self, x, y):
        Drawable.__init__(self, x, y)
        self.image = PhotoImage(file='hero-down.png')
        self.name = 'Hero'
        self.level = 1
        RollStats.roll_stats(self, hp_base = 20, hpc = 3, dpc = 2, sp_base = 5)
        self.full_hp = self.hp

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
    def __init__(self, x, y, has_the_key = False):
        Drawable.__init__(self, x, y)
        self.image = PhotoImage(file='skeleton.png')
        if has_the_key == True:
            self.has_the_key = True
        else:
            self.has_the_key = False
        self.name = 'Skeleton'
        self.level = 1
        RollStats.roll_stats(self, hpc = 2, dpc = 1/2)
        self.full_hp = self.hp

class Boss(Drawable, Character):
    def __init__(self, x, y):
        Drawable.__init__(self, x, y)
        self.image = PhotoImage(file='boss.png')
        self.name = 'Boss'
        self.level = 1
        RollStats.roll_stats(self, hpc = 3, sp_base = 1)
        self.full_hp = self.hp
