import sys, pygame, pygame_gui
from games import *

pygame.init()

SCREEN_SIZE = width, height = (800, 600)

pygame.display.set_caption('G.O.N.E')
SCREEN = pygame.display.set_mode(SCREEN_SIZE)

background = pygame.Surface(SCREEN_SIZE)
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager(SCREEN_SIZE)

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def main_menu():
    CLOCK = pygame.time.Clock()

    SCREEN.fill("black")

    MENU_TEXT = get_font(30).render("Game of Nim Extension", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))
    SCREEN.blit(MENU_TEXT, MENU_RECT)

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
        # SCREEN.blit(background, (0, 0))
        manager.draw_ui(SCREEN)

        pygame.display.update()

def how_to_play():
    CLOCK = pygame.time.Clock()

    SCREEN.fill("black")
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
        # SCREEN.blit(background, (0, 0))
        manager.draw_ui(SCREEN)

        pygame.display.update()

main_menu()