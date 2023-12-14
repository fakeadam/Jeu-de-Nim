from utils.ScreenUtils import *

def showSettingsScreen():

    screen = Screen("Paramètres")
    background = Picture(0, 0, "./ressources/images/background.png")
    background.resize(1280, 720)
    settingsText = Text(530, 60, "PARAMETRES", 70)

    matchesNumberText = Text(475, 200, "Nombres\nallumettes", 30)
    maxMatchesNumberText = Text(475, 325, "Nombre prises\nmaxi", 30)

    def handler_reset_button():
        print("reset")

    def handler_validate_button():
        print("validate")

    def handler_return_button():
        print("retour")

    def handler_removeMatches_button():
        print("-1 matches")
    def handler_addMatches_button():
        print("+1 matches")
    def handler_numberOfMatches_button():
        print("x matches")

    def handler_removeMaxTakenMatches_button():
        print("-1 matches")
    def handler_addMaxTakenMatches_button():
        print("+1 matches")
    def handler_numberOfMaxTakenMatches_button():
        print("x matches")

    resetButton = Button(675, 475, "Réinitialiser", handler_reset_button, 450, 40, "#FDF7E4", "#FAEED1", 20)
    validateButton = Button(675, 550, "Valider", handler_validate_button, 450, 95, "#FDF7E4", "#FAEED1", 40)
    returnButton = Button(525, 550, "<", handler_return_button, 95, 95, "#FDF7E4", "#FAEED1", 40)

    removeMatches = Button(780, 200, "-", handler_removeMatches_button, 95, 95, "#FDF7E4", "#FAEED1", 40)
    matchesNumber = Button(905, 200, "16", handler_numberOfMatches_button, 95, 95, "#FDF7E4", "#FAEED1", 40)
    addMatches = Button(1035, 200, "+", handler_addMatches_button, 95, 95, "#FDF7E4", "#FAEED1", 40)

    removeMaxTakenMatches = Button(780, 325, "-", handler_removeMaxTakenMatches_button, 95, 95, "#FDF7E4", "#FAEED1", 40)
    maxTakenMatches = Button(905, 325, "3", handler_numberOfMaxTakenMatches_button, 95, 95, "#FDF7E4", "#FAEED1", 40)
    addMaxTakenMatches = Button(1035, 325, "+", handler_addMaxTakenMatches_button, 95, 95, "#FDF7E4", "#FAEED1", 40)

    settingsArea = Area(425, 50, 750, 625)

    screen.add_element(background)
    screen.add_element(settingsArea)
    screen.add_element(settingsText)
    screen.add_element(matchesNumberText)
    screen.add_element(maxMatchesNumberText)
    screen.add_element(resetButton)
    screen.add_element(validateButton)
    screen.add_element(returnButton)

    screen.add_element(removeMatches)
    screen.add_element(addMatches)
    screen.add_element(matchesNumber)

    screen.add_element(removeMaxTakenMatches)
    screen.add_element(addMaxTakenMatches)
    screen.add_element(maxTakenMatches)

    screen.run()

