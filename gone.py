import sys, pygame, random, pygame_gui
from games import *
from game_of_nim import GameOfNim

pygame.init()
size = width, height = 1024, 768
SCREEN = pygame.display.set_mode(size)
mainClock = pygame.time.Clock()


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


font = pygame.font.SysFont(None, 60)
COLOR_ACTIVE = pygame.Color('lightskyblue3')
COLOR_INACTIVE = pygame.Color('dodgerblue2')
pygame_icon = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/space.png')
pygame.display.set_icon(pygame_icon)
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

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def main_menu():
    CLOCK = pygame.time.Clock()

    SCREEN.fill("black")

    MENU_TEXT = get_font(30).render("Game of Nim Extension", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(520, 100))
    SCREEN.blit(MENU_TEXT, MENU_RECT)

    input_one_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((420, 170), (200, 25)), text="# Rows (max of 10)",
                                                  manager=manager)
    input_one = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((420, 190), (200, 50)), manager=manager)
    input_one.set_allowed_characters(allowed_characters="numbers")
    # input_one.set_text_length_limit(limit=1)

    input_two_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((420, 245), (200, 25)), text="Max # Sticks (max of 20)",
                                                  manager=manager)
    input_two = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((420, 265), (200, 50)), manager=manager)
    input_two.set_allowed_characters(allowed_characters="numbers")
    # input_two.set_text_length_limit(limit=1)

    start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((420, 325), (200, 50)), text='START GAME',
                                                manager=manager)
    how_to_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((420, 385), (200, 50)), text='HOW TO PLAY',
                                                 manager=manager)
    exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((420, 445), (200, 50)), text='EXIT',
                                               manager=manager)

    while True:
        time_delta = CLOCK.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    num_rows = input_one.get_text()
                    max_sticks = input_two.get_text()
                    print('Starting game with ' + num_rows + ' rows & ' + max_sticks + ' max sticks')
                    if int(num_rows) > 10:
                        num_rows  = 10
                    if int(max_sticks) > 20:
                        max_sticks  = 20
                    input_one.hide()
                    input_one_label.hide()
                    input_two.hide()
                    input_two_label.hide()
                    start_button.hide()
                    how_to_button.hide()
                    exit_button.hide()
                    game_new_two(int(num_rows), int(max_sticks))
                if event.ui_element == how_to_button:
                    print('How to play')
                    input_one.hide()
                    input_one_label.hide()
                    input_two.hide()
                    input_two_label.hide()
                    start_button.hide()
                    how_to_button.hide()
                    exit_button.hide()
                    how_to_play()
                if event.ui_element == exit_button:
                    quit()

            manager.process_events(event)

        manager.update(time_delta)
        # SCREEN.blit(background, (0, 0))
        manager.draw_ui(SCREEN)

        pygame.display.update()


def how_to_play():
    CLOCK = pygame.time.Clock()

    SCREEN.fill("black")
    rules_text = "Rules: The goal of the game to to not pick the last fern. You may pick any number of ferns from any given row, but only one row at a time."

    rules = pygame_gui.elements.UITextBox(html_text=rules_text, relative_rect=pygame.Rect((175, 50), (700, 300)), manager=manager)
    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((420, 445), (200, 50)), text='BACK', manager=manager)

    while True:
        time_delta = CLOCK.tick(60) / 1000.0
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
        # SCREEN.blit(background, (0, 0))
        manager.draw_ui(SCREEN)

        pygame.display.update()


click = False

def draw_sticks():
    return

def game_new_two(amt, user_max):
    CLOCK = pygame.time.Clock()

    SCREEN.fill("black")

    board = []
    for i in range(amt):
        board.append(random.randrange(1, user_max))
    gom = GameOfNim(board=board, screen=SCREEN, pygame=pygame, manager=manager)
    print(gom.result(gom.initial, (1,1) ))
    utility = gom.play_game(alpha_beta_player, query_player)
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
    exit
    
    # board = {}
    # for i in range(amt):
    #     board[i] = {}
    #     for j in range(random.randrange(1, user_max)):
    #         print(i)
    #         print(j)
    #         board[i][j] = True

    #create list of numbers and placement
    # for i in range(amt):
    #     numberx =10
    #     if i == 0:
    #         number_list.append(number0)
    #         numberrect = number0.get_rect()
    #         numberrect.topleft = (numberx, numbery)
    #         numberrect_list.append(numberrect)
    #         numbery += 50
    #     if i == 1:
    #         number_list.append(number1)
    #         numberrect = number1.get_rect()
    #         numberrect.topleft = (numberx,numbery)
    #         numberrect_list.append(numberrect)
    #         numbery+= 50
    #     if i == 2:
    #         number_list.append(number2)
    #         numberrect = number2.get_rect()
    #         numberrect.topleft = (numberx, numbery)
    #         numberrect_list.append(numberrect)
    #         numbery += 50
    #     if i == 3:
    #         number_list.append(number3)
    #         numberrect = number3.get_rect()
    #         numberrect.topleft = (numberx, numbery)
    #         numberrect_list.append(numberrect)
    #         numbery += 50
    #     if i == 4:
    #         number_list.append(number4)
    #         numberrect = number4.get_rect()
    #         numberrect.topleft = (numberx, numbery)
    #         numberrect_list.append(numberrect)
    #         numbery += 50
    #     if i == 5:
    #         number_list.append(number5)
    #         numberrect = number5.get_rect()
    #         numberrect.topleft = (numberx, numbery)
    #         numberrect_list.append(numberrect)
    #         numbery += 50
    #     if i == 6:
    #         number_list.append(number6)
    #         numberrect = number6.get_rect()
    #         numberrect.topleft = (numberx, numbery)
    #         numberrect_list.append(numberrect)
    #         numbery += 50
    #     if i == 7:
    #         number_list.append(number7)
    #         numberrect = number7.get_rect()
    #         numberrect.topleft = (numberx, numbery)
    #         numberrect_list.append(numberrect)
    #         numbery += 50
    #     if i == 8:
    #         number_list.append(number8)
    #         numberrect = number8.get_rect()
    #         numberrect.topleft = (numberx, numbery)
    #         numberrect_list.append(numberrect)
    #         numbery += 50
    #     if i == 9:
    #         number_list.append(number9)
    #         numberrect = number9.get_rect()
    #         numberrect.topleft = (numberx, numbery)
    #         numberrect_list.append(numberrect)
    #         numbery += 50
    #     if i > 10:
    #         number_list.append(arrow)
    #         numberrect = arrow.get_rect()
    #         numberrect.topleft = (numberx, numbery)
    #         numberrect_list.append(numberrect)
    #         numbery += 50

    # for i in range(amt):
    #     stick_x = 60 # space between the columns of sticks
    #     rand_range = random.randrange(1, user_max)
    #     b.append(rand_range)  # for the GameOfNim function
    #     for j in range(rand_range):
    #         stick_list.append(stick)
    #         stickrect = stick.get_rect()
    #         stickrect.topleft = (stick_x, stick_y)
    #         stick_x += 50
    #         stickrect_list.append(stickrect)
    #     stick_y += 50

def game_new(amt, user_max):
    CLOCK = pygame.time.Clock()

    SCREEN.fill("black")
    input_one = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((200, 700), (200, 50)), manager=manager)
    input_one.set_allowed_characters(allowed_characters="numbers")
    input_two = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((420, 700), (200, 50)), manager=manager)
    input_two.set_allowed_characters(allowed_characters="numbers")
    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((640, 700), (200, 50)), text='Make Move', manager=manager)

    stick_list = []
    stickrect_list = []
    #number placement holders
    number_list=[]
    numberrect_list = []
    #board
    b = []
    stick_y = 60  # space between the rows of sticks
    numbery = 60
    stick = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/fern.png')
    
    #images for numbers
    number0 = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/letter-o.png')
    number1 = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/number-1.png')
    number2 = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/number-2.png')
    number3 = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/number-3.png')
    number4 = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/number-four.png')
    number5 = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/number-5.png')
    number6 = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/six.png')
    number7 = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/seven.png')
    number8 = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/number-8.png')
    number9 = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/number-9.png')
    arrow = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/right-arrow.png')

    #create list of numbers and placement
    for i in range(amt):
        numberx =10
        if i == 0:
            number_list.append(number0)
            numberrect = number0.get_rect()
            numberrect.topleft = (numberx, numbery)
            numberrect_list.append(numberrect)
            numbery += 50
        if i == 1:
            number_list.append(number1)
            numberrect = number1.get_rect()
            numberrect.topleft = (numberx,numbery)
            numberrect_list.append(numberrect)
            numbery+= 50
        if i == 2:
            number_list.append(number2)
            numberrect = number2.get_rect()
            numberrect.topleft = (numberx, numbery)
            numberrect_list.append(numberrect)
            numbery += 50
        if i == 3:
            number_list.append(number3)
            numberrect = number3.get_rect()
            numberrect.topleft = (numberx, numbery)
            numberrect_list.append(numberrect)
            numbery += 50
        if i == 4:
            number_list.append(number4)
            numberrect = number4.get_rect()
            numberrect.topleft = (numberx, numbery)
            numberrect_list.append(numberrect)
            numbery += 50
        if i == 5:
            number_list.append(number5)
            numberrect = number5.get_rect()
            numberrect.topleft = (numberx, numbery)
            numberrect_list.append(numberrect)
            numbery += 50
        if i == 6:
            number_list.append(number6)
            numberrect = number6.get_rect()
            numberrect.topleft = (numberx, numbery)
            numberrect_list.append(numberrect)
            numbery += 50
        if i == 7:
            number_list.append(number7)
            numberrect = number7.get_rect()
            numberrect.topleft = (numberx, numbery)
            numberrect_list.append(numberrect)
            numbery += 50
        if i == 8:
            number_list.append(number8)
            numberrect = number8.get_rect()
            numberrect.topleft = (numberx, numbery)
            numberrect_list.append(numberrect)
            numbery += 50
        if i == 9:
            number_list.append(number9)
            numberrect = number9.get_rect()
            numberrect.topleft = (numberx, numbery)
            numberrect_list.append(numberrect)
            numbery += 50
        if i > 10:
            number_list.append(arrow)
            numberrect = arrow.get_rect()
            numberrect.topleft = (numberx, numbery)
            numberrect_list.append(numberrect)
            numbery += 50

    for i in range(amt):
        stick_x = 60 # space between the columns of sticks
        rand_range = random.randrange(1, user_max)
        b.append(rand_range)  # for the GameOfNim function
        for j in range(rand_range):
            stick_list.append(stick)
            stickrect = stick.get_rect()
            stickrect.topleft = (stick_x, stick_y)
            stick_x += 50
            stickrect_list.append(stickrect)
        stick_y += 50

    while True:
        time_delta = CLOCK.tick(60) / 1000.0
        SCREEN.fill("black")
        for i in range(amt):
            for j in range(len(stickrect_list)):
                SCREEN.blit(stick_list[j], stickrect_list[j])

        #display numbers on SCREEN beside sticks
        for i in range(amt):
            for j in range(len(numberrect_list)):
                SCREEN.blit(number_list[j], numberrect_list[j])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == back_button:
                    row_num = input_one.get_text()
                    stick_num = input_two.get_text()
                    print('Removing ' + stick_num + ' stick(s) from row ' + row_num)
                    del stickrect_list[-1]
                    print(stick_list)
                

            manager.process_events(event)

        manager.update(time_delta)
        # SCREEN.blit(background, (0, 0))
        manager.draw_ui(SCREEN)

        pygame.display.update()


def game(amt, user_max):
    SCREEN = pygame.display.set_mode(size)
    stick_list = []
    stickrect_list = []
    #number placement holders
    number_list=[]
    numberrect_list = []
    #board
    b = []
    stick_y = 60  # space between the rows of sticks
    numbery = 60
    stick = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/fern.png')
    
    #images for numbers
    number0 = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/letter-o.png')
    number1 = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/number-1.png')
    number2 = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/number-2.png')
    number3 = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/number-3.png')
    number4 = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/number-four.png')
    number5 = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/number-5.png')
    number6 = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/six.png')
    number7 = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/seven.png')
    number8 = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/number-8.png')
    number9 = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/number-9.png')
    arrow = pygame.image.load('../../Downloads/G.O.N.E-main-052022/G.O.N.E-main/right-arrow.png')

    #create list of numbers and placement
    for i in range(amt+1):
        numberx =10
        if i == 0:
            number_list.append(number0)
            numberrect = number0.get_rect()
            numberrect.topleft = (numberx, numbery)
            numberrect_list.append(numberrect)
            numbery += 50
        if i == 1:
            number_list.append(number1)
            numberrect = number1.get_rect()
            numberrect.topleft = (numberx,numbery)
            numberrect_list.append(numberrect)
            numbery+= 50
        if i == 2:
            number_list.append(number2)
            numberrect = number2.get_rect()
            numberrect.topleft = (numberx, numbery)
            numberrect_list.append(numberrect)
            numbery += 50
        if i == 3:
            number_list.append(number3)
            numberrect = number3.get_rect()
            numberrect.topleft = (numberx, numbery)
            numberrect_list.append(numberrect)
            numbery += 50
        if i == 4:
            number_list.append(number4)
            numberrect = number4.get_rect()
            numberrect.topleft = (numberx, numbery)
            numberrect_list.append(numberrect)
            numbery += 50
        if i == 5:
            number_list.append(number5)
            numberrect = number5.get_rect()
            numberrect.topleft = (numberx, numbery)
            numberrect_list.append(numberrect)
            numbery += 50
        if i == 6:
            number_list.append(number6)
            numberrect = number6.get_rect()
            numberrect.topleft = (numberx, numbery)
            numberrect_list.append(numberrect)
            numbery += 50
        if i == 7:
            number_list.append(number7)
            numberrect = number7.get_rect()
            numberrect.topleft = (numberx, numbery)
            numberrect_list.append(numberrect)
            numbery += 50
        if i == 8:
            number_list.append(number8)
            numberrect = number8.get_rect()
            numberrect.topleft = (numberx, numbery)
            numberrect_list.append(numberrect)
            numbery += 50
        if i == 9:
            number_list.append(number9)
            numberrect = number9.get_rect()
            numberrect.topleft = (numberx, numbery)
            numberrect_list.append(numberrect)
            numbery += 50
        if i > 10:
            number_list.append(arrow)
            numberrect = arrow.get_rect()
            numberrect.topleft = (numberx, numbery)
            numberrect_list.append(numberrect)
            numbery += 50

    for i in range(amt):
        stick_x = 60 # space between the columns of sticks
        rand_range = random.randrange(1, user_max)
        b.append(rand_range)  # for the GameOfNim function
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
        for i in range(amt - 1):
            pygame.draw.rect(SCREEN, (255, 0, 0), stickrect_list[i])
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                mx, my = pygame.mouse.get_pos()
                print(mx, my)
                if stickrect.collidepoint((mx, my)):
                    print('y')
                    # SCREEN.blit(stickrect, (0,0,0))
                    stick.fill((0, 0, 0, 0))
                    # if click:
                    #     print('yes')

        # stickrect = stickrect.move(x, y)
        # if stickrect.left < 0 or stickrect.right > width:
        #     speed[0] = -speed[0]
        # if stickrect.top < 0 or stickrect.bottom > height:
        #     speed[1] = -speed[1]

        SCREEN.fill(black)
        for i in range(amt):
            for j in range(len(stickrect_list)):
                SCREEN.blit(stick_list[j], stickrect_list[j])
        #display numbers on SCREEN beside sticks
        for i in range(amt):
            for j in range(len(numberrect_list)):
                SCREEN.blit(number_list[j], numberrect_list[j])


        pygame.display.flip()

        #get player move
        #or get AI move
        #remove from board, end of lists/rows or create new board?
        #redisplay new board^^
        #when winner if found display winner and allow to go back to main menu
        mainClock.tick(60)


if __name__ == "__main__":
    main_menu()
