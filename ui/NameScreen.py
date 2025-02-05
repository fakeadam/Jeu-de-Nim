from utils.ScreenUtils import *
from ui.MainScreen import showMainScreen
from common.NimGame import Player
from client.NimClient import openSession

def showNameScreen():
    screen = Screen("Choix du pseudonyme")
    background = Picture(0, 0, "ressources/images/background.png")
    background.resize(1280,720)

    area = Area(350, 200, 600, 400, "#DED0B6", "#BBAB8C")
    inputArea = Area(400, 350, 500, 125, "#FDF7E4", "#FAEED1")
    inputShadow = Area(415, 450, 450, 5, "#FDF7E4", "#DED0B6")
    text = Text(400, 250, "CHOIX PSEUDO", 40)

    text = Text(100, 5, "TEST_PSEU", 60)

    profil = Picture(10, 10, "./ressources/images/userIcon.png")
    profil.resize(75,75)


    inputBox = InputBox(425, 400, 450, 75, 65, (255,255,255))

    def handler_click_confirm():
        running = False
        text.setText(inputBox.get_text())
        player = Player(inputBox.get_text())
        client_socket = openSession()
        player.setClientSocket(client_socket)
        
        

    confirmButton = Button(400, 500, "VALIDER", handler_click_confirm, 500, 60, "#FDF7E4", "#FAEED1", 40)

    screen.add_element(background)
    screen.add_element(area)
    screen.add_element(inputArea)
    screen.add_element(text)
    screen.add_element(inputBox)
    screen.add_element(inputShadow)
    screen.add_element(profil)
    screen.add_element(confirmButton)

    # Boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                inputBox.handle_event(event)  # Gérer l'événement de la zone de texte
                confirmButton.handle_click()  # Gérer le clic sur le bouton

            elif event.type == pygame.KEYDOWN:
                inputBox.handle_event(event)  # Gérer l'événement de la zone de texte

    # Dessiner les éléments
        screen.screen.fill((255, 255, 255))
        for element in screen.elements:
            element.draw(screen.screen)

        pygame.display.flip()
        screen.clock.tick(60)

    pygame.quit()

# Pause courte pour permettre à la fenêtre de se mettre à jour
    pygame.time.delay(100)

# Maintenant, après la boucle principale, vous pouvez appeler showMainScreen si nécessaire.
    showMainScreen()