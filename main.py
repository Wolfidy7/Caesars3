import pygame, cv2

from header import Button

pygame.init()

# création fenêtre
class screen():

    def __init__(self, screen_height, screen_width, title):
        self.height = screen_height
        self.width = screen_width
        self.title = pygame.display.set_caption(title)

    def display(self):
        pygame.display.set_mode((self.height, self.width))

    def background(self, background):
        bg = pygame.image.load(background)
        self.blit(bg, (0, 0))  #problème à régler ici



main_screen = screen(1080, 720, "Test boutons")
main_screen.display()
main_screen.background("main_image.jpg")



# Redimensionnement images
main_image = cv2.imread("main_image.jpg")
cv2.imwrite("main_image_r.jpg", cv2.resize(main_image, (main_screen.height, main_screen.width)))

# importation des images dans pygame

new_game = pygame.image.load("new_game.png")
load_game = pygame.image.load("load_game.png")


# création des boutons
NG_button = Button(400, 200, new_game, 0.3)
LG_button = Button(400, 400, load_game, 0.3)


# Boucle de jeu
running = True
while running:
    main_screen.background("main_image.jpg")

    NG_button.draw(main_screen)
    LG_button.draw(main_screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
    pygame.display.update() #mise à jour de l'interface

pygame.quit()

