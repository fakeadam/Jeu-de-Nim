from utils.GameUtils import generateId

def createRoom(player):
    id = generateId(5)
    roomId = "ROOM_".join(map(str, id))
    key = generateId(6)
    roomKey = "".join(map(str, key))
    player.sendPacket(f"CREATE {player.getName()} {roomId} {roomKey}")