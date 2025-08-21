import pandas as pd
import numpy as np
import time


# Main player object
class Player:
    # Player stats
    overall = 0
    pick = 0
    tds = 0
    ints = 0
    yards = 0
    team = ""

    def __init__(self, name):
        self.name = name


# Draft simulation
def draft(player):
    player.pick = np.random.randint(1, 257)
    player.team = "Knoxville TESTs"
    print(
        f"With pick {player.pick} in the NFL draft, the {player.team} select {player.name}!"
    )

    # Player Overall
    if player.pick >= 10:
        player.overall = 80
    elif player.pick >= 32:
        player.overall = 75
    elif player.pick >= 150:
        player.overall = 70
    else:
        player.overall = 65

    # Display starting stats
    print(f"-- {player.name} Stats --\nOverall: {player.overall}")
    return


def main():
    name = input("Player Name: ")
    player = Player(name)
    draft(player)


main()
