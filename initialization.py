from turtle import back
import pygame


# loads the word/definition data from the csv file created via webscraping
def load_data(file_name):
    with open(file_name, 'r') as data_file:
        lines = data_file.readlines()

    data = []
    for i in range(len(lines)):
        data.append(lines[i].split(',', 1))
        data[i][1] = data[i][1].strip()
        data[i][1] = data[i][1].strip('"')
    
    return data


# reads the how_to_play.txt file into a list to be used to format how to play screen
def load_how_to_play():
    instructions = []

    with open('how_to_play.txt', 'r') as file:
        lines = file.readlines()

        for line in lines:
            if line != '\n':
                line = line.strip()
                instructions.append(line)

    return instructions


# function to create a button on the main menu
def create_menu_button(button_x, button_y, button_w, button_h, button_text, button_text_color, button_font):
    button = pygame.Rect(button_x, button_y, button_w, button_h)
    border = pygame.Rect(button_x, button_y, button_w, button_h) 
    text = button_font.render(button_text, True, button_text_color)

    return button, border, text


# initialization
#--------------------------------------------------------------------------------------------------
pygame.init()
pygame.font.init()
pygame.mixer.init()

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

width = window.get_width()
height = window.get_height()

data = load_data('data.csv')

timer, timer_text = 0, '0'
#--------------------------------------------------------------------------------------------------


# fonts
# ---------------------------------------------------------------------
general_font = pygame.font.SysFont('Century Gothic', int(width * 0.021))

prompt_font = pygame.font.SysFont('Century Gothic', int(width * 0.021), bold = True)
prompt_font.set_underline(True)

button_font = pygame.font.SysFont('Century Gothic', int(width * 0.021), bold = True)

timer_font = pygame.font.SysFont('Century Gothic', int(width * 0.044), bold = True)
timer_font.set_underline(True)

how_to_font = pygame.font.SysFont('Century Gothic', int(width * 0.013))
how_to_font_bold = pygame.font.SysFont('Century Gothic', int(width * 0.013), bold = True)

credits_button_font = pygame.font.SysFont('Century Gothic', int(width * 0.015), bold = True)
credits_font_bold_under = pygame.font.SysFont('Century Gothic', int(width * 0.014), bold = True)
credits_font_bold_under.set_underline(True)
credits_font_bold = pygame.font.SysFont('Century Gothic', int(width * 0.012), bold = True)
credits_font = pygame.font.SysFont('Century Gothic', int(width * 0.012))

link_font = pygame.font.SysFont('Century Gothic', int(width * 0.012))
link_font.set_underline(True)
# ---------------------------------------------------------------------


# buttons and other layout/formatting objects
# ---------------------------------------------------------------------
background_img = pygame.image.load('Images/background.png')
background_img = pygame.transform.scale(background_img, (width, height))

play_area = pygame.Rect(width * 0.146, height * 0.139, width * 0.707, height * 0.722)
play_area_border = pygame.Rect(width * 0.146, height * 0.139, width * 0.707, height * 0.722)

title_screen = pygame.Rect(width * 0.426, height * 0.028, width * 0.145, height * 0.097)
title_border = pygame.Rect(width * 0.426, height * 0.028, width * 0.145, height * 0.097)
title = general_font.render('QuizCabulary', True, 'black')

quit_button, quit_border, quit_text = create_menu_button(width * 0.975, 0, width * 0.025, height * 0.062, 'X', 'white', button_font)

credits_button, credits_border, credits_text = create_menu_button(width * 0.456, height * 0.150, width * 0.082, height * 0.080, 'CREDITS', 'black', credits_button_font)

game_mode1_button, game_mode1_border, game_mode1_text = create_menu_button(width * 0.439, height * 0.393, width * 0.117, height * -0.111, 'MODE 1', 'white', button_font)

game_mode2_button, game_mode2_border, game_mode2_text = create_menu_button(width * 0.439, height * 0.552, width * 0.117, height * -0.111, 'MODE 2', 'white', button_font)

single_player_button, single_player_border, single_player_text = create_menu_button(width * 0.292, height * 0.319, width * 0.117, height * -0.111, '1 PLAYER', 'white', button_font)

multi_player_button, multi_player_border, multi_player_text = create_menu_button(width * 0.292, height * 0.472, width * 0.117, height * -0.111, '2 PLAYERS', 'white', button_font)

time_trial_button, time_trial_border, time_trial_text = create_menu_button(width * 0.292, height * 0.638, width * 0.117, height * -0.111, 'TIME TRIAL', 'white', button_font)

easy_button, easy_border, easy_text = create_menu_button(width * 0.585, height * 0.319, width * 0.117, height * -0.111, 'EASY', 'white', button_font)

medium_button, medium_border, medium_text = create_menu_button(width * 0.585, height * 0.472, width * 0.117, height * -0.111, 'MEDIUM', 'white', button_font)

hard_button, hard_border, hard_text = create_menu_button(width * 0.585, height * 0.638, width * 0.117, height * -0.111, 'HARD', 'white', button_font)

start_button, start_border, start_text = create_menu_button(width * 0.351, height * 0.798, width * 0.297, height * -0.111, 'START', 'white', button_font)

how_to_button, how_to_border, how_to_text = create_menu_button(width * 0.415, height * 0.986, width * 0.171, height * -0.111, 'HOW TO PLAY', 'black', button_font)

menu_button, menu_border, menu_text = create_menu_button(width * 0.415, height * 0.986, width * 0.170, height * -0.111, 'MAIN MENU', 'black', button_font)
# ---------------------------------------------------------------------