from client.NimClient import openSession
from ui.NameScreen import showNameScreen
from common.NimGame import Player

showNameScreen()

player = Player("test")
client_socket = openSession()
player.setClientSocket(client_socket)

player.sendPacket("CREER test test")