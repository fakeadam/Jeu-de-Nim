import random

def generateId(number):
    id_list = [random.randint(0, 9) for _ in range(number)]
    return id_list