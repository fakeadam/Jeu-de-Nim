from ui.NameScreen import showNameScreen
import random

def generateId():
    id_list = [random.randint(0, 9) for _ in range(5)]
    return id_list

player_id = generateId()
player_name = "PLAYER_" + "".join(map(str, player_id))

showNameScreen()