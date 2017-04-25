

# created by Edward Mondragon

def create_hud(player):
    hud = player.name + "\n+---------------+\n|Health:       " + str(player.health) + \
          "|\n|Other:        3|\n+---------------+"
    print(hud)
    return hud