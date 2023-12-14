import random

def generateId(number):
    id_list = [random.randint(0, 9) for _ in range(number)]
    return id_list

def verifyDuplicateId(firstId, secondId):
    if(firstId == secondId):
        while firstId == secondId:
            secondId = generateId(5)
        return secondId
    else:
        return secondId