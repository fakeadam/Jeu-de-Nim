from utils.ScreenUtils import *
def handler_button():
    print("Button Clicked")



def showMainScreen():

    screen = Screen("Jeu de Nim !")
    background = Picture(0,0, "./ressources/images/background.png")
    background.resize(1280,720)
    credit = Text(10,700,"Projet NSI 2023 réalisé par Adame et Thomas",10)
    title = Text(690,85,"JEU DE NIM",70,)
    menuArea = Area(650,75,550,550)
    soloBtn = Button(710,190,"Solo",handler_button,425,105)
    localBtn = Button(710,325,"Local",handler_button,425,105)
    enligneBtn = Button(710,460,"EnLigne",handler_button,425,105)

    
    screen.add_element(background)
    screen.add_element(credit)
    screen.add_element(menuArea)
    screen.add_element(soloBtn)
    screen.add_element(localBtn)
    screen.add_element(enligneBtn)
    screen.add_element(title)
    screen.run()

