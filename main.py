import pygame, cv2
pygame.init()

# création fenêtre
screen_height = 1080
screen_width = 720
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption('Test Buttons')

# Redimensionnement images
main_image = cv2.imread("main_image.jpg")
cv2.imwrite("main_image_r.jpg", cv2.resize(main_image, (screen_height, screen_width)))

# importation des images dans pygame
bg = pygame.image.load("main_image_r.jpg")
new_game = pygame.image.load("new_game.png")
load_game = pygame.image.load("load_game.png")

class Button():

    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.x = x
        self.y = y

    def draw(self):
        # dessin du bouton sur l'écran
        screen.blit(self.image, (self.x, self.y))


# création des boutons
NG_button = Button(400, 200, new_game, 0.3)
LG_button = Button(400, 400, load_game, 0.3)


# Boucle de jeu
running = True
while running:
    screen.blit(bg, (0, 0))

    NG_button.draw()
    LG_button.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
    pygame.display.update() #mise à jour de l'interface

pygame.quit()

