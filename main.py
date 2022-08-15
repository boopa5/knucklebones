import pygame
import Game

MIDDLE_GAP = 200
MARGIN = 200
BOX_SIZE = 50

SCREEN_DIM = [3 * BOX_SIZE + 2 * MARGIN, MIDDLE_GAP + 6 * BOX_SIZE]

FONT_SIZE = 40
FONT_PX = FONT_SIZE * 72 / 96


game = Game.Game()

pygame.init()

font1 = pygame.font.SysFont(None, FONT_SIZE)

screen = pygame.display.set_mode(SCREEN_DIM)


def get_col(pos):
    res = (pos[0] - MARGIN) // BOX_SIZE
    return res if res >= 0 and res <= 2 else -1


def draw():

    # Numbers
    for i, col in enumerate(game.board["p1"]):
        for j, val in enumerate(col):
            txt = font1.render(str(val), True, (0, 0, 0))
            screen.blit(txt, (MARGIN + BOX_SIZE / 2 + i * BOX_SIZE - FONT_PX / 2, 3 * BOX_SIZE + MIDDLE_GAP + j * BOX_SIZE + BOX_SIZE / 2 - FONT_PX / 2))

    
    for i, col in enumerate(game.board["p2"]):
        for j, val in enumerate(col):
            txt = font1.render(str(val), True, (0, 0, 0))
            screen.blit(txt, (MARGIN + BOX_SIZE / 2 + i * BOX_SIZE - FONT_PX / 2, 3 * BOX_SIZE - j * BOX_SIZE - BOX_SIZE / 2 - FONT_PX / 2))

    # Column scores
    for i, col in enumerate(game.board["p1"]):
        txt = font1.render(str(sum(col)), True, (0, 0, 0))
        screen.blit(txt, (MARGIN + BOX_SIZE / 2 + i * BOX_SIZE - FONT_PX / 2, 3 * BOX_SIZE - FONT_PX + MIDDLE_GAP))

    for i, col in enumerate(game.board["p2"]):
        txt = font1.render(str(sum(col)), True, (0, 0, 0))
        screen.blit(txt, (MARGIN + BOX_SIZE / 2 + i * BOX_SIZE - FONT_PX / 2, 3 * BOX_SIZE + FONT_PX / 2))

    # Grid
    for i in range(4):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (MARGIN, i * BOX_SIZE), (3 * BOX_SIZE + MARGIN, i * BOX_SIZE), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * BOX_SIZE + MARGIN, 0), (i * BOX_SIZE + MARGIN, 3 * BOX_SIZE), thick)

        pygame.draw.line(screen, (0, 0, 0), (MARGIN, i * BOX_SIZE + 3 * BOX_SIZE + MIDDLE_GAP), (3 * BOX_SIZE + MARGIN, i * BOX_SIZE + 3 * BOX_SIZE + MIDDLE_GAP), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * BOX_SIZE + MARGIN, 3 * BOX_SIZE + MIDDLE_GAP), (i * BOX_SIZE + MARGIN, (3 * BOX_SIZE + MIDDLE_GAP) + 3 * BOX_SIZE), thick)

    pygame.draw.line(screen, (0, 0, 0), (0, 3 * BOX_SIZE), (SCREEN_DIM[0], 3 * BOX_SIZE), 7)
    pygame.draw.line(screen, (0, 0, 0), (0, 3 * BOX_SIZE + MIDDLE_GAP), (SCREEN_DIM[0], 3 * BOX_SIZE + MIDDLE_GAP), 7)

    # Player colors
    pygame.draw.rect(screen, (90, 230, 120), (0, 3 * BOX_SIZE + MIDDLE_GAP, MARGIN, 6 * BOX_SIZE + MIDDLE_GAP))
    pygame.draw.rect(screen, (90, 230, 120), (MARGIN + 3 * BOX_SIZE, 3 * BOX_SIZE + MIDDLE_GAP, 2 * MARGIN + 3 * BOX_SIZE, 6 * BOX_SIZE + MIDDLE_GAP))

    pygame.draw.rect(screen, (227, 79, 106), (0, 0, MARGIN, 3 * BOX_SIZE))
    pygame.draw.rect(screen, (227, 79, 106), (MARGIN + 3 * BOX_SIZE, 0, 2 * MARGIN + 3 * BOX_SIZE, 3 * BOX_SIZE))

    # Dice roll
    txt = font1.render(f"{game.turn} rolled {game.dice_val}", True, (0, 0, 0))
    screen.blit(txt, (SCREEN_DIM[0] / 2 - txt.get_size()[0] / 2, SCREEN_DIM[1] / 2- txt.get_size()[1] / 2))



running = True
while running:

    # Check winner
    if game.game_over():
        winner = game.winner()
        game.reset_game()

    # Update mouse pos
    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Place value in column
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.take_turn(get_col(pos))
    # White bg
    screen.fill((255, 255, 255))
    draw()


    pygame.display.update()

# Done! Time to quit.
pygame.quit()