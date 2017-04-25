#Written by Edward Mondragon

class Player(object):
    health = 3
    base_attack = 3
    def __init__(self):
        pass

class Entity(object):
    name = ""
    description = ""
    attributes = []
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Tile(object):
    tileID = -1
    tileDescription = ""
    entities = []
    neighboringIDs = []
    def __init__(self, id, description):
        self.tileID = id
        self.tileDescription = description

class Map(object):
    tiles = []
    def __init__(self):
        tiles.append(Tile());

def game(player, map):
    return