

#Written by Edward Mondragon

class Player(object):
    name = ""
    health = 5
    base_attack = 3
    inventory = []

    def __init__(self, name):
        self.name = name
        pass


class Entity(object):
    name = ""
    description = ""
    attributes = []

    def __init__(self, name, description, attribs):
        self.name = name
        self.description = description
        self.attributes = attribs


class Tile(object):
    tile_id = -1
    tile_description = ""
    entities = []
    neighboringIDs = []

    def __init__(self, tile_id, description):
        self.tile_id = tile_id
        self.tile_description = description


class Map(object):
    tiles = []

    def __init__(self):
        self.tiles.append(Tile(0, "A room of index " + str(0)))


def game(player, game_map):
    return game_map.tiles[0].tile_description
