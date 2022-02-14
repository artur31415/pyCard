from asyncio.windows_events import NULL
import json
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

# Opening JSON file
f = open(current_dir + r'\data\cards.json')
 
# returns JSON object as
# a dictionary
card_data = json.load(f)


for a in range(5):
    myCards.append(Card(current_dir + card_path, card_data['cards'][a], 4, (100 * a, 20)))


f.close()

log_count = 0

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 10)

selected_card = None

print("rect > ", myCards[0].card_img.get_rect())

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("pressed A")
            elif event.key == pygame.K_d:
                print("pressed D")

        #selected_card = None

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            # get a list of all sprites that are under the mouse cursor
            clicked_cards = [s for s in myCards if s.card_img.get_rect().collidepoint(mouse_pos)]
            if len(clicked_cards) > 0:
                for x in range(len(clicked_cards)):
                    selected_card = clicked_cards[x]
                    print(log_count, "# Card -> ", clicked_cards[x].json_data['name'], " clicked")
                    log_count += 1


        mouse_pos = pygame.mouse.get_pos()
        if myCards[0].card_img.get_rect().collidepoint((mouse_pos[0] - myCards[0].position[0], mouse_pos[1] - myCards[0].position[1])):
            print(log_count, "# mouse is over ", myCards[0].json_data['name'], "; card pos = ", myCards[0].position, "; mouse pos = ", pygame.mouse.get_pos())
            log_count += 1


    # Fill the background with white
    screen.fill((255, 255, 255))


    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    for a in range(5):
        screen.blit(myCards[a].card_img, (card_pad_left + myCards[a].position[0], myCards[a].position[1]))
        screen.blit(newCard.card_img, (card_pad_left + 100 * a, 400))


    if selected_card != None:
        textsurface = myfont.render(selected_card.json_data['name'], False, (0, 0, 0))
        screen.blit(textsurface, (selected_card.position[0], selected_card.position[1] + 30))
    # Flip the display
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()