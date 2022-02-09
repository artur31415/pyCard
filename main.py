import pygame
pygame.init()

# Set up the drawing window

screen = pygame.display.set_mode([500, 500])
# Run until the user asks to quit

running = True

back_card_img = pygame.image.load(r'C:\Users\br0049087103\Documents\Code\Python\simpleChess\img\card_back.jpg')
size_x, size_y = back_card_img.get_size()
scale_factor = 4
back_card_img = pygame.transform.scale(back_card_img, (int(size_x / scale_factor), int(size_y / scale_factor)))

card_pad_left = 25


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
            clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]


    # Fill the background with white
    screen.fill((255, 255, 255))


    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    for a in range(5):
        screen.blit(back_card_img, (card_pad_left + 100 * a, 0))
        screen.blit(back_card_img, (card_pad_left + 100 * a, 400))

    # Flip the display
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()