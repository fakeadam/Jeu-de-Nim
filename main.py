from ui.MainScreen import showMainScreen
from utils.GameUtils import generateId
from utils.RoomUtils import createRoom
from common.NimGame import Player
from client.NimClient import openSession

player_id = generateId(5)
player_name = "PLAYER_" + "".join(map(str, player_id))
player = Player(player_name)
client_socket = openSession()
player.setClientSocket(client_socket)
createRoom(player)

showMainScreen()