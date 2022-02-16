import pygame

class FieldSlot:
    def __init__(self, position, card, card_class, width, height) -> None:
        self.position = position
        self.card = card
        self.card_class = card_class

        self.width = width
        self.height = height

    def get_rect(self):
        return pygame.Rect(self.position[0], self.position[1], self.width, self.height) # [self.position[0], self.position[1], self.width, self.height]