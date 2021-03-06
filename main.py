from asyncio.windows_events import NULL
import json
import string
import pygame
from pathlib import Path



from card import *
from field_slot import *

pygame.init()

# Set up the drawing window

width = 500
height = 500

screen = pygame.display.set_mode([width, height])
# Run until the user asks to quit

running = True
current_dir = str(Path().absolute())
card_path = r'\img\card_back.jpg'

print("current path is ", current_dir)
# E:\LAPTOP_BACKUP\Duat\Nirvana\NeoSoft\Python\pyCard\img

newCard = Card(current_dir + card_path, "{name:debug1}", 4, (0, 0))

myCards = []

myField = []
enemyField = []

card_pad_left = 25

# Opening JSON file
f = open(current_dir + r'\data\cards.json')
 
# returns JSON object as
# a dictionary
card_data = json.load(f)

field_base_height = 130
fields_delta_height = 10

for a in range(5):
    myCards.append(Card(current_dir + card_path, card_data['cards'][a], 4, (100 * a + card_pad_left, 20)))

    enemyField.append(FieldSlot((50 + 72 * a, field_base_height), None, CardClass.Magic, 70, 110))   
    myField.append(FieldSlot((50 + 72 * a, field_base_height + fields_delta_height + 110), None, CardClass.Magic, 70, 110))


f.close()

log_count = 0

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 10)

selected_card = None

print("rect > ", myCards[0].card_img.get_rect())

######################################################################
######################################################################
######################################################################
def GetSelectedCardIndex():
    for x in range(len(myCards)):
        if myCards[x].is_selected:
            return x
    return -1

def UnselectAllMyCardsExcept(exceptionIndex):
    for x in range(len(myCards)):
        if x != exceptionIndex:
            myCards[x].is_selected = False

def GetCardIndexByName(cardArray, cardName):
    for x in range(len(cardArray)):
        if cardArray[x].json_data['name'] == cardName:
            return x
    return -1

def PointMinus(pointA, pointB):
    return (pointA[0] - pointB[0], pointA[1] - pointB[1])

######################################################################
######################################################################
######################################################################
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
            clicked_cards = [s for s in myCards if s.card_img.get_rect().collidepoint(PointMinus(mouse_pos, s.position))]
            clicked_my_slots = [s for s in myField if s.get_rect().collidepoint(PointMinus(mouse_pos, s.position))]
            clicked_enemy_slots = [s for s in enemyField if s.get_rect().collidepoint(PointMinus(mouse_pos, s.position))]


            # CHECK FOR CLICKED CARDS
            if len(clicked_cards) > 0:
                for x in range(len(clicked_cards)):
                    selected_card = clicked_cards[x]
                    print(log_count, "# Clicked Card -> ", clicked_cards[x].json_data['name'], " clicked")
                    log_count += 1

                    #TODO: IF CARD IS IN HAND, SET SCHEMA TO PLACE CARD IN FIELD
                    #TODO: IF CARD IS ON FIELD, ATK/DEF STANCE
                    selected_card_index = GetCardIndexByName(myCards, clicked_cards[x].json_data['name'])
                    if selected_card_index != -1:
                        myCards[selected_card_index].is_selected = True
                        #TODO: UNSELECT ALL OTHERS
                        UnselectAllMyCardsExcept(selected_card_index)

            # CHECK FOR CLICKED MY SLOTS
            if len(clicked_my_slots) > 0:
                for my_slot in clicked_my_slots:
                    print(log_count, "# Clicked My Slot at -> ", my_slot.position, " clicked")
                    log_count += 1
                    #TODO: CHECK IF CARD IS SELECTED
                    selected_card_index = GetSelectedCardIndex()
                    if selected_card_index != -1:
                        myCards[selected_card_index].position = my_slot.position

            # CHECK FOR CLICKED ENEMY SLOTS
            if len(clicked_enemy_slots) > 0:
                for my_slot in clicked_enemy_slots:
                    print(log_count, "# Clicked Enemy Slot at -> ", my_slot.position, " clicked")
                    log_count += 1


        for myCard in myCards:
            mouse_pos = pygame.mouse.get_pos()
            colide_pos = PointMinus(mouse_pos, myCard.position) # (mouse_pos[0] - myCard.position[0], mouse_pos[1] - myCard.position[1])
            if myCard.card_img.get_rect().collidepoint(colide_pos):
                print(log_count, "# mouse is over ", myCard.json_data['name'], "; card pos = ", myCard.position, "; mouse pos = ", pygame.mouse.get_pos(), "; colide_pos = ", colide_pos)
                log_count += 1


    # Fill the background with white
    screen.fill((255, 255, 255))

    for a in range(5):
        screen.blit(myCards[a].card_img, (myCards[a].position[0], myCards[a].position[1]))
        screen.blit(newCard.card_img, (card_pad_left + 100 * a, 400))

    

    if selected_card != None:
        textsurface = myfont.render(selected_card.json_data['name'] + r": (" + str(selected_card.json_data['atk']) + r", " + str(selected_card.json_data['def']) + ")", False, (0, 0, 0))
        screen.blit(textsurface, (selected_card.position[0], selected_card.position[1] + 70))
    
    #pygame.draw.circle(screen, (0, 0, 255), myCards[1].position, 10)

    # (_, _, rect_w, rect_h) = myCards[0].card_img.get_rect()
    # row_counts = 3
    # for k in range(row_counts):
    #     pygame.draw.line(screen, (0, 0, 255), (0, 200 + k * rect_w), (width, 200 + k * rect_w))
    #     pygame.draw.line(screen, (0, 0, 255), (200 + k * rect_w, 200), (200 + k * rect_w, 200 + row_counts * rect_w))
    
    for myFieldSlot in myField:
        pygame.draw.rect(screen, (0, 0, 255), myFieldSlot.get_rect_with_pos(), 1)

    for enemyFieldSlot in enemyField:
        pygame.draw.rect(screen, (0, 255, 255), enemyFieldSlot.get_rect_with_pos(), 1)

    # Flip the display
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()