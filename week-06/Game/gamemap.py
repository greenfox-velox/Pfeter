from drawables import *
from characters import *

class GameMap(object):
    def __init__(self):
        self.map_height = 11
        self.map_width = 10
        self.map_level = 1

    def tutorial_tiles(self):
        first_map = [
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
        self.map_height = len(first_map)
        self.map_width = len(first_map[0])
        tiles = []
        for i in range(self.map_height):
            for j in range(self.map_width):
                if first_map[i][j] == 0:
                    tiles.append(FloorTile(j, i))
                else:
                    tiles.append(WallTile(j, i))
        return tiles

    def tutorial_enemies(self):
        first_enemies = [
        ['skeleton', 4, 3, False],
        ['skeleton', 4, 8, True],
        ['skeleton', 7, 8, False],
        ['boss', 6, 3]
        ]
        enemies = []
        for i in range(len(first_enemies)):
            if first_enemies[i][0] ==  'skeleton':
                enemies.append(Skeleton(first_enemies[i][1], first_enemies[i][2], first_enemies[i][3]))
            elif first_enemies[i][0] == 'boss':
                enemies.append(Boss(first_enemies[i][1], first_enemies[i][2]))
        return enemies

    def new_level_enemies(self):
        self.map_level += 1
        random_enemies = [
        ['skeleton', 4, 3, False, self.map_level],
        ['skeleton', 4, 8, True, self.map_level],
        ['skeleton', 7, 8, False, self.map_level],
        ['boss', 6, 3, self.map_level]
        ]
        enemies = []
        for i in range(len(random_enemies)):
            if random_enemies[i][0] ==  'skeleton':
                enemies.append(Skeleton(random_enemies[i][1], random_enemies[i][2], random_enemies[i][3], random_enemies[i][4]))
            elif random_enemies[i][0] == 'boss':
                enemies.append(Boss(random_enemies[i][1], random_enemies[i][2], random_enemies[i][3]))
        return enemies
