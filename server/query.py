

#Written by Edward Mondragon

class Player(object):
    health = 5
    base_attack = 3

    def __init__(self):
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

    def set_description(self, description):
        self.tile_description = description

    def get_description(self):
        print(self.tile_description)


class Map(object):
    tiles = []

    def __init__(self):
        self.tiles.append(Tile(0, "A room of index " + str(0)))


def game(player, game_map):
    print(game_map.tiles[0].get_description())
    return

player1 = Player()
my_map = Map()
game(player1, my_map)
