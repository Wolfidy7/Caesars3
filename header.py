import pygame

class Button():

    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.x = x
        self.y = y

    def draw(self, screen):
        # dessin du bouton sur l'écran
        screen.blit(self.image, (self.x, self.y))
