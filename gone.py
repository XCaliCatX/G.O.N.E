# Imports for project
import sys, pygame, random, pygame_gui
from games import *
from game_of_nim import GameOfNim

# Initialize PyGame instance
pygame.init()
pygame.display.set_caption('G.O.N.E')

# Create screen for game
size = width, height = 1024, 768
SCREEN = pygame.display.set_mode(size)
mainClock = pygame.time.Clock()

# Function to draw text onto the screen
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Set game-wide constants
font = pygame.font.SysFont(None, 60)
COLOR_ACTIVE = pygame.Color('lightskyblue3')
COLOR_INACTIVE = pygame.Color('dodgerblue2')
pygame_icon = pygame.image.load('../../Downloads/G.O.N.E.-Final/G.O.N.E.-Final/assets/space.png')
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

# Create manager to be used for pygame_gui
manager = pygame_gui.UIManager(size)

# Gets "Arcade" font for title and game over screens
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

# Displays the main menu of the game
def main_menu():
    # Start the clock
    CLOCK = pygame.time.Clock()

    # Fill screen
    SCREEN.fill("black")
    # Main menu text
    MENU_TEXT = get_font(30).render("Game of Nim Extension", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(520, 100))
    SCREEN.blit(MENU_TEXT, MENU_RECT)
    # Input one
    input_one_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((420, 170), (200, 25)), text="# Rows (max of 10)", manager=manager)
    input_one = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((420, 190), (200, 50)), manager=manager)
    input_one.set_allowed_characters(allowed_characters="numbers")
    # Input two
    input_two_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((420, 245), (200, 25)), text="Max # Sticks (max of 20)", manager=manager)
    input_two = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((420, 265), (200, 50)), manager=manager)
    input_two.set_allowed_characters(allowed_characters="numbers")
    # Buttons
    start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((420, 325), (200, 50)), text='START GAME', manager=manager)
    how_to_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((420, 385), (200, 50)), text='HOW TO PLAY', manager=manager)
    exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((420, 445), (200, 50)), text='EXIT', manager=manager)

    # Execute this loop until the game is either closed or redirected elsewhere
    while True:
        time_delta = CLOCK.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    num_rows = input_one.get_text()
                    max_sticks = input_two.get_text()
                    if num_rows == "" or max_sticks == "" or int(num_rows) < 2 or int(max_sticks) < 2:
                        break
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
                    game(int(num_rows), int(max_sticks))
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

        # Update screen
        manager.update(time_delta)
        manager.draw_ui(SCREEN)
        pygame.display.update()


# Displays the rules for the game
def how_to_play():
    # Start the clock
    CLOCK = pygame.time.Clock()

    # Fill screen
    SCREEN.fill("black")
    # Rules
    rules_text = "Rules: The goal of the game is to not pick the last fern. You may pick any number of ferns from any given row, but only one row at a time. " \
    "Start the game by choosing a number of rows (min = 2, max = 10), and maximum number of sticks per row (min = 2, max = 20), and select the 'Play Game' button." \
    "To make a move type in the row number in the box on the left and number of ferns to remove in the box to right."
    rules = pygame_gui.elements.UITextBox(html_text=rules_text, relative_rect=pygame.Rect((175, 50), (700, 300)), manager=manager)
    # Button
    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((420, 445), (200, 50)), text='BACK', manager=manager)

    # Execute this loop until the game is either closed or redirected elsewhere
    while True:
        time_delta = CLOCK.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == back_button:
                    back_button.hide()
                    rules.hide()
                    main_menu()

            manager.process_events(event)

        # Update screen
        manager.update(time_delta)
        manager.draw_ui(SCREEN)
        pygame.display.update()

# Displays the game over screen
def game_over(winner):
    # Start the clock
    CLOCK = pygame.time.Clock()

    # Fill screen
    SCREEN.fill("black")
    # Message text
    if winner == "Player":
        txt = "You won! :D"
    else:
        txt = "You lost! :("
    MENU_TEXT = get_font(30).render(txt, True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(520, 100))
    SCREEN.blit(MENU_TEXT, MENU_RECT)
    # Buttons
    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((420, 445), (200, 50)), text='MAIN MENU', manager=manager)

    # Execute this loop until the game is either closed or redirected elsewhere
    while True:
        time_delta = CLOCK.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == back_button:
                    back_button.hide()
                    main_menu()

            manager.process_events(event)

        # Update screen
        manager.update(time_delta)
        manager.draw_ui(SCREEN)
        pygame.display.update()

# Displays the actual gameplay of the game
def game(amt, user_max):
    # Start the clock
    CLOCK = pygame.time.Clock()

    # Fill screen
    SCREEN.fill("black")

    # Create board & game given user inputs
    board = []
    for i in range(amt):
        board.append(random.randrange(1, user_max))
    gom = GameOfNim(board=board, screen=SCREEN, pygame=pygame, manager=manager)
    # print(gom.result(gom.initial, (1,1) ))

    # Call function to actually "play" the game
    utility = gom.play_game(alpha_beta_player, query_player)

    # Determine winner based on the result above
    if (utility < 0):
        print("MIN won the game")
        winner = "Player"
    else:
        print("MAX won the game")
        winner = "AI"

    # Pass winner over to game_over function to be displayed
    game_over(winner)
    
# Main function, which opens up the main menu when the game is run
if __name__ == "__main__":
    main_menu()

