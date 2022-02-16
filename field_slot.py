import pygame

class FieldSlot:
    def __init__(self, position, card, type, width, height) -> None:
        self.position = position
        self.card = card
        self.type = type

        self.width = width
        self.height = height