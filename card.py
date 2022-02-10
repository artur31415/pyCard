import pygame

class Card:
    def __init__(self, img_path, json_data, img_scale_factor, position) -> None:
        self.card_img = pygame.image.load(img_path)
        size_x, size_y = self.card_img.get_size()
        self.card_img = pygame.transform.scale(self.card_img, (int(size_x / img_scale_factor), int(size_y / img_scale_factor)))

        self.position = position
        self.json_data = json_data
