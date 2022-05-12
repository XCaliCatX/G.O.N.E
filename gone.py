import sys, pygame, random, pygame_gui
from games import *
from main import GameOfNim


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
GRAY = (127, 127, 127)

manager = pygame_gui.UIManager(size)


def main_menu():
    CLOCK = pygame.time.Clock()

    screen.fill("black")

    MENU_TEXT = font.render("Game of Nim Extension", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))
    screen.blit(MENU_TEXT, MENU_RECT)

    input_one_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 170), (200, 25)), text="# Rows", manager=manager)
    input_one = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300, 190), (200, 50)),manager=manager)
    input_one.set_allowed_characters(allowed_characters="numbers")
    # input_one.set_text_length_limit(limit=1)

    input_two_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 245), (200, 25)), text="Max # Sticks", manager=manager)
    input_two = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300, 265), (200, 50)),manager=manager)
    input_two.set_allowed_characters(allowed_characters="numbers")
    # input_two.set_text_length_limit(limit=1)

    start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 325), (200, 50)), text='START GAME', manager=manager)
    how_to_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 385), (200, 50)), text='HOW TO PLAY', manager=manager)
    exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 445), (200, 50)), text='EXIT', manager=manager)

    while True:
        time_delta = CLOCK.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    num_rows = input_one.get_text()
                    max_sticks = input_two.get_text()
                    print('Starting game with ' + num_rows + ' rows & ' + max_sticks + ' max sticks')
                    game(int(num_rows), int(max_sticks))
                if event.ui_element == how_to_button:
                    print('How to play')
                    input_one.hide()
                    input_two.hide()
                    start_button.hide()
                    how_to_button.hide()
                    exit_button.hide()
                    how_to_play()
                if event.ui_element == exit_button:
                    quit()

            manager.process_events(event)

        manager.update(time_delta)
        # screen.blit(background, (0, 0))
        manager.draw_ui(screen)

        pygame.display.update()

def how_to_play():
    CLOCK = pygame.time.Clock()

    screen.fill("black")
    rules_text = "Here we will explain the rules to the game.  It may not be very long, but there should be plenty of space to work with."
    
    
    rules = pygame_gui.elements.UITextBox(html_text=rules_text, relative_rect=pygame.Rect((50, 50), (700, 300)), manager=manager)
    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 445), (200, 50)), text='BACK', manager=manager)

    while True:
        time_delta = CLOCK.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == back_button:
                    print('Returning to main menu')
                    back_button.hide()
                    rules.hide()
                    main_menu()

            manager.process_events(event)

        manager.update(time_delta)
        # screen.blit(background, (0, 0))
        manager.draw_ui(screen)

        pygame.display.update()

click = False


def game(amt, user_max):
    screen = pygame.display.set_mode(size)
    stick_list = []
    stickrect_list = []
    b = []
    stick_y = 0 # space between the rows of sticks
    stick = pygame.image.load('fern.png')
    for i in range(amt):
        stick_x = 0 # space between the columns of sticks
        rand_range = random.randrange(1, user_max)
        b.append(rand_range) # for the GameOfNim function
        for j in range(rand_range):
            stick_list.append(stick)
            stickrect = stick.get_rect()
            stickrect.topleft = (stick_x, stick_y)
            stick_x += 50
            stickrect_list.append(stickrect)
        stick_y += 50
    print(b)

    gom = GameOfNim(board=b)
    while 1:
        # mx, my = pygame.mouse.get_pos()
        for i in range(amt-1):
            pygame.draw.rect(screen, (255, 0, 0), stickrect_list[i])
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

        # stickrect = stickrect.move(x, y)
        # if stickrect.left < 0 or stickrect.right > width:
        #     speed[0] = -speed[0]
        # if stickrect.top < 0 or stickrect.bottom > height:
        #     speed[1] = -speed[1]

        screen.fill(black)
        for i in range(amt):
            for j in range(len(stickrect_list)):
                screen.blit(stick_list[j], stickrect_list[j])
        pygame.display.flip()
        mainClock.tick(60)


if __name__ == "__main__":
    main_menu()
