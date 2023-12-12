from utils.ScreenUtils import *

def showNameScreen():
    screen = Screen("Choix du pseudonyme")
    background = Picture(0, 0, "ressources/images/background.png")
    background.resize(1280,720)

    area = Area(350, 200, 600, 300, "#DED0B6", "#BBAB8C")
    text = Text(400, 250, "CHOIX PSEUDO", 60)

    screen.add_element(background)
    screen.add_element(area)
    screen.add_element(text)
    screen.run()