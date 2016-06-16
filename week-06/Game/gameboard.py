from gamemap import *

class GameBoard(object):
    def __init__(self):
        self.game_map = GameMap()
        self.map_size = [self.game_map.map_width, self.game_map.map_height]
        self.tiles = self.game_map.tutorial_tiles()
        self.enemies = self.game_map.tutorial_enemies()
        self.hero = Hero(0, 0)

    def screen_draw(self, canvas):
        canvas.delete('all')
        for x in range(len(self.tiles)):
            self.tiles[x].draw(canvas)
        for y in range(len(self.enemies)):
            self.enemies[y].draw(canvas)
        self.hero.draw(canvas)
        self.hero.stat_print(canvas, 1, self.map_size)
        if self.overlap_a_character() != 0:
            self.overlap_a_character().stat_print(canvas, 2, self.map_size)

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
            self.battle(self.hero, self.overlap_a_character())
        self.screen_draw(canvas)

    def overlap_a_character(self):
        for overlapped_character in self.enemies:
            if self.hero.x == overlapped_character.x and self.hero.y == overlapped_character.y:
                return(overlapped_character)
        return 0

    def battle(self, hero, enemy):
        hero.strike(enemy)
        if enemy.hp <= 0:
            self.enemies.remove(enemy)
            if enemy.name == 'Skeleton' and enemy.has_the_key:
                self.hero.has_the_key = True
        else:
            enemy.strike(hero)

    def can_move(self, who, direction_x, direction_y):
        for i in self.tiles:
            if i.x == (who.x + direction_x) and i.y == (who.y + direction_y) and i.accessible:
                return True
        return False
