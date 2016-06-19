from random import randint

class RollStats(object):
    def roll_stats(self, hp_base = 0, hpc = 1, dp_base = 0, dpc = 1, sp_base = 0, spc = 1, level = 1):
        self.hp = hp_base + self.dice_6.roll(hpc) * level
        self.dp = dp_base + self.dice_6.roll(dpc) * level / 2
        self.sp = sp_base + self.dice_6.roll(spc) * level

class Dice(object):
    def __init__(self, sides):
        self.sides = sides

    def roll(self, number_of_rolls):
        if number_of_rolls <= 1:
            return randint(1,self.sides)
        else:
            return randint(1,self.sides) + self.roll(number_of_rolls - 1)

class StatPrint(object):
    def stat_print(self, canvas, which_row, map_size):
        canvas.create_text(map_size[0] * 72 / 2, map_size[1] * 72 + which_row * 20, text = self.stat())
