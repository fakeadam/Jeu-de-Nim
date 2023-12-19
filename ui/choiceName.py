from utils.ScreenUtils import *


def pseudo():
    screen = Screen("choisisez votre pseudo")
    background = Picture(0,0, "./ressources/images/background.png")
    background.resize(1280,720)
    title = Text(690,85,"PSEUDO",70,)
    menuArea = Area(650,75,550,550)


    
    screen.add_element(background)
    screen.add_element(title)
    screen.add_element(Area)


    screen.run()