import string
import pygame
from pathlib import Path

from card import Card


pygame.init()

# Set up the drawing window

screen = pygame.display.set_mode([500, 500])
# Run until the user asks to quit

running = True
current_dir = str(Path().absolute())
card_path = r'\img\card_back.jpg'

print("current path is ", current_dir)
# E:\LAPTOP_BACKUP\Duat\Nirvana\NeoSoft\Python\pyCard\img

newCard = Card(current_dir + card_path, "{name:debug1}", 4, (0, 0))

myCards = []

card_pad_left = 25


for a in range(5):
    myCards.append(Card(current_dir + card_path, "{name:debug" + str(a) + "}", 4, (100 * a, 0)))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("pressed A")
            elif event.key == pygame.K_d:
                print("pressed D")

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            # get a list of all sprites that are under the mouse cursor
            clicked_cards = [s for s in myCards if s.rect.collidepoint(pos)]
            if clicked_cards.count > 0:



    # Fill the background with white
    screen.fill((255, 255, 255))


    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    for a in range(5):
        screen.blit(myCards[a].card_img, (card_pad_left + myCards[a].position[0], myCards[a].position[1]))
        screen.blit(newCard.card_img, (card_pad_left + 100 * a, 400))

    # Flip the display
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()