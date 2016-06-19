from tkinter import *
from stats import *
from drawables import Drawable

class Character(StatPrint):
    def __init__(self):
        self.dice_6 = Dice(6)
        self.dice_10 = Dice(10)

    def stat(self):
        return (self.name + ' (Level ' + str(self.level) + ') HP: ' + str(self.hp) + '/' + str(self.full_hp) + ' | DP: ' + str(self.dp) +' | SP: ' + str(self.sp))

    def strike(self, enemy):
        sv = self.sp + self.dice_6.roll(2)
        if sv > enemy.dp:
            enemy.hp -= sv - enemy.dp

class Hero(Drawable, Character):
    def __init__(self, x, y):
        Drawable.__init__(self, x, y)
        Character.__init__(self)
        self.image = PhotoImage(file='images/hero-down.png')
        self.has_the_key = False
        self.name = 'Hero'
        self.level = 1
        RollStats.roll_stats(self, hp_base = 20, hpc = 3, dpc = 2, sp_base = 5)
        self.full_hp = self.hp

    def move(self, direction):
        if direction == 'down':
            self.image = PhotoImage(file='images/hero-down.png')
            self.y += 1
        if direction == 'up':
            self.image = PhotoImage(file='images/hero-up.png')
            self.y -= 1
        if direction == 'left':
            self.image = PhotoImage(file='images/hero-left.png')
            self.x -= 1
        if direction == 'right':
            self.image = PhotoImage(file='images/hero-right.png')
            self.x += 1

    def leveling(self):
        self.level += 1
        self.full_hp += self.dice_6.roll(1)
        self.dp += self.dice_6.roll(1)
        self.sp += self.dice_6.roll(1)

class Enemy(object):
    def leveling(self, map_level):
        rolled = self.dice_10.roll(1)
        if rolled <= 5:
            return map_level
        elif rolled <= 9:
            return map_level + 1
        else:
            return map_level + 2

class Skeleton(Drawable, Character, Enemy):
    def __init__(self, x, y, has_the_key, level = 1):
        Drawable.__init__(self, x, y)
        Character.__init__(self)
        self.image = PhotoImage(file='images/skeleton.png')
        self.has_the_key = has_the_key
        self.name = 'Skeleton'
        self.level = self.leveling(level)
        RollStats.roll_stats(self, hpc = 2, dpc = 1/2, level = self.level)
        self.full_hp = self.hp

class Boss(Drawable, Character, Enemy):
    def __init__(self, x, y, level = 1):
        Drawable.__init__(self, x, y)
        Character.__init__(self)
        self.image = PhotoImage(file='images/boss.png')
        self.name = 'Boss'
        self.level = self.leveling(level)
        RollStats.roll_stats(self, hp_base = self.dice_6.roll(1), hpc = 2, dp_base = self.dice_6.roll(1)/2, dpc = self.level/2, sp_base = self.level, spc = self.level, level = self.level)
        self.full_hp = self.hp
