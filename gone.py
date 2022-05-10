import sys, pygame
from games import *
import game_of_nim

pygame.init()
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)
mainClock = pygame.time.Clock()


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


font = pygame.font.SysFont(None, 60)
COLOR_ACTIVE = pygame.Color('lightskyblue3')
COLOR_INACTIVE = pygame.Color('dodgerblue2')
black = (0, 0, 0)
white = (255, 255, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)


def main_menu():
    user_text = ''
    active = False
    color = COLOR_INACTIVE
    rect_width = 200
    rect_height = 50
    text_box = pygame.Rect(450, 250, rect_width, rect_height)
    titleFont = pygame.font.SysFont("rockwell", 32)
    titleText = titleFont.render("Game of Nim Extension", True, BLACK)
    pygame.display.set_caption("G.O.N.E")
    icon = pygame.image.load("space.png")
    pygame.display.set_icon(icon)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if text_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if (user_text.isdigit()):
                            print(user_text)
                            game(int(user_text))
                        # else:
                        #     draw_text('input a number amount', font, white, screen, 20, 20)
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
        screen.fill(WHITE)
        screen.blit(titleText, (340, 15))
        pygame.draw.rect(screen, color, text_box)
        color = COLOR_ACTIVE if active else COLOR_INACTIVE
        text_surface = font.render(user_text, True, BLACK)
        screen.blit(text_surface, (text_box.x + 5, text_box.y + 5))
        text_box.w = max(100, text_surface.get_width() + 10)
        draw_text('input depth amount (integer):', titleFont, BLACK, screen, 300, 200)

        pygame.display.flip()
        mainClock.tick(60)


click = False


def game(amt):
    gom = game_of_nim(amt)
    screen = pygame.display.set_mode(size)
    stick = pygame.image.load('stick.png')
    stickrect = stick.get_rect()
    rect_width = 50
    rect_height = 200
    stickrect2 = pygame.Rect((width / 2) - (rect_width / 2), (height / 2) - (rect_height / 2), rect_width, rect_height)
    # stickrect2
    # pos = 0
    x = 0
    y = 0

    while 1:
        # mx, my = pygame.mouse.get_pos()

        pygame.draw.rect(screen, (255, 0, 0), stickrect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                mx, my = pygame.mouse.get_pos()
                print(mx, my)
                if stickrect.collidepoint((mx, my)):
                    print('y')
                    # screen.blit(stickrect, (0,0,0))
                    stick.fill((0, 0, 0, 0))
                    # if click:
                    #     print('yes')

        stickrect = stickrect.move(x, y)
        # if stickrect.left < 0 or stickrect.right > width:
        #     speed[0] = -speed[0]
        # if stickrect.top < 0 or stickrect.bottom > height:
        #     speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(stick, stickrect)
        pygame.display.flip()
        mainClock.tick(60)


if __name__ == "__main__":
    main_menu()
