import pygame

from initialization import *


# creates a blank canvas
def draw_play_area():
    # draw background image
    window.blit(background_img, (0, 0))

    # draw game title
    pygame.draw.rect(window, 'white', title_screen, 0, 30)
    window.blit(title, (width * 0.430, height * 0.047))
    pygame.draw.rect(window, 'black', title_border, 2, 30)

    # draw play area
    pygame.draw.rect(window, 'white', play_area, 0, 30)
    pygame.draw.rect(window, 'black', play_area_border, 2, 30)

    # draw X button
    pygame.draw.rect(window, 'red', quit_button)
    pygame.draw.rect(window, 'black', quit_border, 2)
    window.blit(quit_text, (width * 0.981, 0))

    draw_menu_button(menu_button, '#696969', menu_text, (width * 0.443, height * 0.895), menu_border)

    pygame.display.update()


# draws the given button on the main menu
def draw_menu_button(button, button_color, button_text, text_coord, border):
    pygame.draw.rect(window, button_color, button, 0, 30)
    window.blit(button_text, text_coord)
    pygame.draw.rect(window, 'black', border, 4, 30)


# draws the buttons for the main menu
def draw_main_menu():
    draw_menu_button(game_mode1_button, '#8E44AD', game_mode1_text, (width * 0.458, height * 0.307), game_mode1_border)

    draw_menu_button(game_mode2_button, '#5B2C6F', game_mode2_text, (width * 0.459, height * 0.467), game_mode2_border)

    draw_menu_button(single_player_button, '#3498DB', single_player_text, (width * 0.305, height * 0.233), single_player_border)

    draw_menu_button(multi_player_button, '#2874A6', multi_player_text, (width * 0.302, height * 0.385), multi_player_border)

    draw_menu_button(time_trial_button, '#154360', time_trial_text, (width * 0.301, height * 0.553), time_trial_border)

    draw_menu_button(easy_button, '#22B14C', easy_text, (width * 0.620, height * 0.233), easy_border)

    draw_menu_button(medium_button, '#FFD700', medium_text, (width * 0.604, height * 0.385), medium_border)

    draw_menu_button(hard_button, '#ED1C24', hard_text, (width * 0.617, height * 0.553), hard_border)

    draw_menu_button(start_button, '#3C0000', start_text, (width * 0.470, height * 0.708), start_border)

    draw_menu_button(how_to_button, '#696969', how_to_text, (width * 0.434, height * 0.895), how_to_border)

    draw_menu_button(credits_button, '#696969', credits_text, (width * 0.467, height * 0.165), credits_border)

    pygame.display.update()


# draws the how to play screen
def draw_how_to_play():
    # set up a new area
    draw_play_area()
    draw_menu_button(menu_button, '#696969', menu_text, (width * 0.443, height * 0.895), menu_border)

    # load the instructions from how_to_play.txt
    instructions = load_how_to_play()

    # writes each instruction line by line
    # -------------------------------------------------------------------------------------------------
    # heading
    window.blit(how_to_font_bold.render(instructions[0], True, 'black'), (width * 0.158, height * 0.139))

    # instructions for game modes
    window.blit(how_to_font_bold.render(instructions[1], True, 'black'), (width * 0.158, height * 0.208))
    window.blit(how_to_font.render(instructions[2], True, 'black'), (width * 0.158, height * 0.257))
    window.blit(how_to_font.render(instructions[3], True, 'black'), (width * 0.158, height * 0.306))
    window.blit(how_to_font.render(instructions[4], True, 'black'), (width * 0.158, height * 0.354))
    
    # instructions for minigames
    window.blit(how_to_font_bold.render(instructions[5], True, 'black'), (width * 0.158, height * 0.424))
    window.blit(how_to_font.render(instructions[6], True, 'black'), (width * 0.158, height * 0.472))
    window.blit(how_to_font.render(instructions[7], True, 'black'), (width * 0.158, height * 0.521))

    # instructions for difficulties
    window.blit(how_to_font_bold.render(instructions[8], True, 'black'), (width * 0.158, height * 0.590))
    window.blit(how_to_font.render(instructions[9], True, 'black'), (width * 0.158, height * 0.639))
    window.blit(how_to_font.render(instructions[10], True, 'black'), (width * 0.158, height * 0.688))
    window.blit(how_to_font.render(instructions[11], True, 'black'), (width * 0.158, height * 0.736))

    # how to quit the game
    window.blit(how_to_font_bold.render(instructions[12], True, 'black'), (width * 0.158, height * 0.806))
    # -------------------------------------------------------------------------------------------------

    pygame.display.update()


# creates text surfaces so the user can later click on the links in credits
def create_credit_links(song, creator, cc_license, song_location, creator_location, license_location):
    song_link = window.blit(link_font.render(song, True, 'black'), song_location)
    creator_link = window.blit(link_font.render(creator, True, 'black'), creator_location)
    cc_license_link = window.blit(link_font.render(cc_license, True, 'black'), license_location)

    return song_link, creator_link, cc_license_link


# draws the timer
def draw_timer(timer):
    # draws a white rectangle behind the timer so the numbers dont draw over themselves
    pygame.draw.rect(window, 'white', (width * 0.770, height * 0.160, width * 0.074, height * 0.113))

    window.blit(timer_font.render(str(timer), True, 'black'), (width * 0.773, height * 0.139))
    pygame.display.update()


# draws the points
def draw_points(points):
    window.blit(general_font.render('Points:', True, 'black'), (width * 0.662, height * 0.144))
    window.blit(general_font.render(str(points), True, 'black'), (width * 0.732, height * 0.144))
    pygame.display.update()


# creates an answer choice button
def draw_answer_choice(button_center, choice_text, text_location):
    center = button_center

    pygame.draw.circle(window, 'black', center, height * 0.031)
    choice_button = pygame.draw.circle(window, '#696969', center, height * 0.028)

    window.blit(general_font.render(choice_text, True, 'black'), text_location)

    # returns the button to draw_easy/medium/hard_screen()
    return center, choice_button


# draws the screen for easy difficulty
def draw_easy_screen(prompt, question, choice_list):
    draw_play_area()

    # write out prompt and question
    window.blit(prompt_font.render(prompt, True, 'black'), (width * 0.176, height * 0.143))
    window.blit(general_font.render(question, True, 'black'), (width * 0.176, height * 0.268)) 

    # create answer choice buttons and draw them
    centerA, choiceA = draw_answer_choice((width * 0.176, height * 0.431), choice_list[0], (width * 0.200, height * 0.397))
    centerB, choiceB = draw_answer_choice((width * 0.176, height * 0.576), choice_list[1], (width * 0.200, height * 0.543))
    centerC, choiceC = draw_answer_choice((width * 0.176,  height * 0.722), choice_list[2], (width * 0.200, height * 0.689))
    pygame.display.update()

    # filler variables to be able to pass to answer_select()
    choiceD = pygame.Rect(0, 0, 0, 0)
    choiceE = pygame.Rect(0, 0, 0, 0)
    centerE, centerD = (0, 0)

    # return answer choice buttons and their coordinates to answer_select()
    return choiceA, choiceB, choiceC, choiceD, choiceE, centerA, centerB, centerC, centerD, centerE


# draws the screen for medium difficulty
def draw_medium_screen(prompt, question, choice_list):
    draw_play_area()

    # write out prompt and question
    window.blit(prompt_font.render(prompt, True, 'black'), (width * 0.176, height * 0.143))
    window.blit(general_font.render(question, True, 'black'), (width * 0.176, height * 0.247))

    # create answer choice buttons and draw them
    centerA, choiceA = draw_answer_choice((width * 0.176, height * 0.382), choice_list[0], (width * 0.200, height * 0.349))
    centerB, choiceB = draw_answer_choice((width * 0.176, height * 0.514), choice_list[1], (width * 0.200, height * 0.481))
    centerC, choiceC = draw_answer_choice((width * 0.176,  height * 0.646), choice_list[2], (width * 0.200, height * 0.613))
    centerD, choiceD = draw_answer_choice((width * 0.176,  height * 0.778), choice_list[3], (width * 0.200, height * 0.744))
    pygame.display.update()

    # filler variables to be able to pass to answer_select()
    choiceE = pygame.Rect(0, 0, 0, 0)
    centerE = (0, 0)

    # return answer choice buttons and their coordinates to answer_select()
    return choiceA, choiceB, choiceC, choiceD, choiceE, centerA, centerB, centerC, centerD, centerE


# draws the screen for hard difficulty
def draw_hard_screen(prompt, question, choice_list):
    draw_play_area()

    # write out prompt and question
    window.blit(prompt_font.render(prompt, True, 'black'), (width * 0.176, height * 0.143))
    window.blit(general_font.render(question, True, 'black'), (width * 0.176, height * 0.213))

    # create answer choice buttons and draw them
    centerA, choiceA = draw_answer_choice((width * 0.176, height * 0.333), choice_list[0], (width * 0.200, height * 0.300))
    centerB, choiceB = draw_answer_choice((width * 0.176, height * 0.447), choice_list[1], (width * 0.200, height * 0.414))
    centerC, choiceC = draw_answer_choice((width * 0.176,  height * 0.563), choice_list[2], (width * 0.200, height * 0.529))
    centerD, choiceD = draw_answer_choice((width * 0.176,  height * 0.676), choice_list[3], (width * 0.200, height * 0.643))
    centerE, choiceE = draw_answer_choice((width * 0.176,  height * 0.792), choice_list[4], (width * 0.200, height * 0.758))
    pygame.display.update()

    # return answer choice buttons and their coordinates to answer_select()
    return choiceA, choiceB, choiceC, choiceD, choiceE, centerA, centerB, centerC, centerD, centerE


# draws borders around main menu buttons when the player presses a button
def game_mode_selected(button):
    if button == 1:
        pygame.draw.rect(window, '#ffd700', game_mode1_border, 4, 30)
    else:
        pygame.draw.rect(window, 'black', game_mode1_border, 4, 30)

    if button == 2:
        pygame.draw.rect(window, '#ffd700', game_mode2_border, 4, 30)
    else: 
        pygame.draw.rect(window, 'black', game_mode2_border, 4, 30)


# draws borders around main menu buttons when the player presses a button
def num_players_selected(button):
    if button == 1:
        pygame.draw.rect(window, '#41fa53', single_player_border, 4, 30)
    else:
        pygame.draw.rect(window, 'black', single_player_border, 4, 30)

    if button == 2:
        pygame.draw.rect(window, '#41fa53', multi_player_border, 4, 30)
    else: 
        pygame.draw.rect(window, 'black', multi_player_border, 4, 30)

    if button == 3:
        pygame.draw.rect(window, '#41fa53', time_trial_border, 4, 30)
    else:
        pygame.draw.rect(window, 'black', time_trial_border, 4, 30)


# draws borders around main menu buttons when the player presses a button
def difficulty_selected(button):
    if button == 1:
        pygame.draw.rect(window, '#16c9fa', easy_border, 4, 30)
    else:
        pygame.draw.rect(window, 'black', easy_border, 4, 30)

    if button == 2:
        pygame.draw.rect(window, '#16c9fa', medium_border, 4, 30)
    else: 
        pygame.draw.rect(window, 'black', medium_border, 4, 30)

    if button == 3:
        pygame.draw.rect(window, '#16c9fa', hard_border, 4, 30)
    else:
        pygame.draw.rect(window, 'black', hard_border, 4, 30)

