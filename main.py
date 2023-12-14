from ui.MainScreen import showMainScreen
from ui.SettingsScreen import showSettingsScreen
from utils.GameUtils import generateId
from utils.RoomUtils import createRoom
from common.NimGame import Player
from client.NimClient import openSession
<<<<<<< Updated upstream

showSettingsScreen()
=======
from ui.SoloScreen import *
player_id = generateId(5)
player_name = "PLAYER_" + "".join(map(str, player_id))

showSoloScreen()
>>>>>>> Stashed changes
