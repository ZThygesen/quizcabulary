from initialization import *

import game_end as end

import draw_functions as draw

import sound_functions as sound

import random

# controls the backend on how the games function
def game_mode_select(minigame, game_mode, difficulty):
    sound.start_playing_music()

    # for the in-game timer
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    # game mode 1 and 2 have a 60 second countdown timer
    timer = 60
    keep_timer = True

    # if player selected singleplayer
    if game_mode == 1:
        points = 0

        # continues the game until the timer runs out or the player exits
        while keep_timer:
            points, timer, keep_timer, main_menu = play_minigame(minigame, points, difficulty, timer, game_mode)
            if main_menu: return True

        # fade music out and give summary; wait until user chooses what to do next
        pygame.mixer.music.fadeout(2000) 
        main_menu = end.gameSummarySingle(points)
        if main_menu: return True
    
    # if player selected multiplayer
    elif game_mode == 2:
        player1_points = 0 
        player2_points = 0

        # continues the game until the timer runs out or the player exits
        while keep_timer:
            player1_points, timer, keep_timer, main_menu = play_minigame(minigame, player1_points, difficulty, timer, game_mode) 
            if main_menu: return True

        # fade music out, give players time to switch, start music once game begins; return to main menu if requested
        pygame.mixer.music.fadeout(2000)
        main_menu = draw_intermission()
        if main_menu: return True
        sound.start_playing_music()

        # timer needs to be reset for player 2    
        timer = 60
        keep_timer = True

        # continues the game until the timer runs out or the player exits
        while keep_timer:
            player2_points, timer, keep_timer, main_menu = play_minigame(minigame, player2_points, difficulty, timer, game_mode)
            if main_menu: return True
        
        # fade music out and give summary; wait until user chooses what to do next
        pygame.mixer.music.fadeout(2000)
        main_menu = end.gameSummaryMulti(player1_points, player2_points)
        if main_menu: return True

    # if player selected time trial
    elif game_mode == 3:
        sound.start_playing_music()

        # timer starts at zero and counts up for this game mode
        points = 0
        timer = 0

        # continues the game until the player reaches 10 points or the player exits
        while points < 10:
            points, timer, keep_timer, main_menu = play_minigame(minigame, points, difficulty, timer, game_mode)
            if main_menu: return True

        # fade music out and give summary; wait until user chooses what to do next
        pygame.mixer.music.fadeout(2000)
        main_menu = end.gameSummaryTime(timer)
        if main_menu: return True
    
    return main_menu

# facilitates the generation of questions/answer choices and player's answers for each question
def play_minigame(minigame, points, difficulty, timer, game_mode):
    prompt, question, choice_list, correct_letter = generate_question(minigame, difficulty)

    user_answer, timer, keep_timer, main_menu = answer_select(prompt, question, choice_list, correct_letter, difficulty, timer, game_mode, points)

    # increment points for correct answers
    if user_answer == correct_letter:
        points += 1

    # returns back to game_mode_select()
    return points, timer, keep_timer, main_menu


# generates a random question with answer choices
def generate_question(minigame, difficulty):

    # randomly generates the correct question/answer pair
    # facilitates the csv file created from webscraping... file loaded in initialize.py
    rand_row = random.randrange(0, 999)
    word = data[rand_row][0]
    definition = data[rand_row][1]

    # sets up for mode 1
    if (minigame == 1):
        prompt = 'Choose the definition that matches the word.'
        word_or_def = 1
        question = word
        answer = definition

    # sets up for mode 2
    elif (minigame == 2):
        prompt = 'Choose the word that matches the definition.'
        word_or_def = 0
        question = definition
        answer = word

    # need to generate different amounts of answer choices based on selected difficulty
    # the other few answer choices are randomly generated

    # easy - 3 choices
    if (difficulty == 1):
        num_choices = 3
        choice_list = [answer]
        for i in range(num_choices - 1):
            choice_list.append(data[random.randrange(0, 999)][word_or_def])
    
    # medium - 4 choices
    elif (difficulty == 2):
        num_choices = 4
        choice_list = [answer]
        for i in range(num_choices - 1):
            choice_list.append(data[random.randrange(0, 999)][word_or_def])
    
    # hard - 5 choices
    else:
        num_choices = 5
        choice_list = [answer]
        for i in range(num_choices - 1):
            choice_list.append(data[random.randrange(0, 999)][word_or_def])

    # shuffle the choice list and find the letter that corresponds to the correct answer
    random.shuffle(choice_list)
    abcde = ['A', 'B', 'C', 'D', 'E']
    correct_letter = ''
    for i in range(num_choices):
        if choice_list[i] == answer:
            correct_letter = abcde[i]
    
    # returns to play_minigame()
    return prompt, question, choice_list, correct_letter


# backend of the player's answer selection
def answer_select(prompt, question, choice_list, correct_letter, difficulty, timer, game_mode, points):
    # the layouts of each game is slightly different based on the difficulty the player chooses...
    # this draws the correct screen and receives the locations of each answer choice button (used to determine where the player clicks
    # and if they selected the right or wrong answer)
    if (difficulty == 1):
        choiceA, choiceB, choiceC, choiceD, choiceE, A_coord, B_coord, C_coord, D_coord, E_coord = draw.draw_easy_screen(prompt, question, choice_list)
    elif (difficulty == 2):
        choiceA, choiceB, choiceC, choiceD, choiceE, A_coord, B_coord, C_coord, D_coord, E_coord = draw.draw_medium_screen(prompt, question, choice_list)
    else:
        choiceA, choiceB, choiceC, choiceD, choiceE, A_coord, B_coord, C_coord, D_coord, E_coord = draw.draw_hard_screen(prompt, question, choice_list)

    user_answer = ''
    main_menu = False

    # loop the awaits the player's answer
    # this loop will end when either they choose an answer or the timer runs out
    choice_not_selected = True
    keep_timer = True
    while choice_not_selected and keep_timer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # controls the timer
            if event.type == pygame.USEREVENT:
                # we want the timer to count up for time trial
                if game_mode == 3:
                    timer += 1
                # we want the timer to count down for mode 1 and mode 2
                else:
                    timer -= 1
                    # break the loop once time runs out
                    if (timer <= 0):
                        keep_timer = False
                        user_answer = ''
                        break

            # if player clicks, take mouse position of click
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                # quit game button pressed
                if quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()

                # main menu button pressed
                if menu_button.collidepoint(mouse_pos):
                    sound.button_sound()
                    choice_not_selected = False
                    main_menu = True
                    return user_answer, timer, keep_timer, main_menu
                
                # if player selected first choice
                if choiceA.collidepoint(mouse_pos):
                    sound.button_sound()

                    # changes color of button to indicate correct/incorrect answer upon clicking it
                    if (correct_letter == 'A'):
                        choiceA = pygame.draw.circle(window, 'green', A_coord, height * 0.028)
                    else:
                        choiceA = pygame.draw.circle(window, 'red', A_coord, height * 0.028)

                    # need to record player's answer for point purposes and break the loop
                    user_answer = 'A'
                    choice_not_selected = False

                # if player selected second choice
                elif choiceB.collidepoint(mouse_pos):
                    sound.button_sound()

                    # changes color of button to indicate correct/incorrect answer upon clicking it
                    if (correct_letter == 'B'):
                        choiceB = pygame.draw.circle(window, 'green', B_coord, height * 0.028)
                    else:
                        choiceB = pygame.draw.circle(window, 'red', B_coord, height * 0.028)
                    
                    # need to record player's answer for point purposes and break the loop
                    user_answer = 'B'
                    choice_not_selected = False

                # if player selected third choice
                elif choiceC.collidepoint(mouse_pos):
                    sound.button_sound()

                    # changes color of button to indicate correct/incorrect answer upon clicking it
                    if (correct_letter == 'C'):
                        choiceC = pygame.draw.circle(window, 'green', C_coord, height * 0.028)
                    else:
                        choiceC = pygame.draw.circle(window, 'red', C_coord, height * 0.028)
                    
                    # need to record player's answer for point purposes and break the loop
                    user_answer = 'C'
                    choice_not_selected = False

                # if player selected fourth choice
                elif choiceD.collidepoint(mouse_pos):
                    sound.button_sound()

                    # changes color of button to indicate correct/incorrect answer upon clicking it
                    if (correct_letter == 'D'):
                        choiceD = pygame.draw.circle(window, 'green', D_coord, height * 0.028)
                    else:
                        choiceD = pygame.draw.circle(window, 'red', D_coord, height * 0.028)
                    
                    # need to record player's answer for point purposes and break the loop
                    user_answer = 'D'
                    choice_not_selected = False

                # if player selected fifth choice
                elif choiceE.collidepoint(mouse_pos):
                    sound.button_sound()

                    # changes color of button to indicate correct/incorrect answer upon clicking it
                    if (correct_letter == 'E'):
                        choiceE = pygame.draw.circle(window, 'green', E_coord, height * 0.028)
                    else:
                        choiceE = pygame.draw.circle(window, 'red', E_coord, height * 0.028)
                    
                    # need to record player's answer for point purposes and break the loop
                    user_answer = 'E'
                    choice_not_selected = False

        # continuously update the timer and points
        draw.draw_timer(timer)
        draw.draw_points(points)

    pygame.display.update()

    # pause for 0.5 secs after choosing an answer
    pygame.time.wait(500)
    
    # returns to play minigame to generate a new question (or end the game if time runs out)
    return user_answer, timer, keep_timer, main_menu


# draws the transition from player 1 to player 2 in multiplayer game mode
def draw_intermission():
    draw.draw_play_area()

    window.blit(general_font.render("Player 2's turn!", True, 'black'), (width * 0.428, height * 0.465))

    main_menu = False

    # there are 6 seconds of intermission
    timer = 6
    keep_timer = True

    # continues until timer runs out
    while keep_timer:
        for event in pygame.event.get():
            # timer counts down
            if event.type == pygame.USEREVENT:
                timer -= 1
                # break loop when time runs out
                if (timer <= 0):
                    keep_timer = False

            # if player clicks, take position of click
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                # quit game button pressed
                if quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()

                # main menu button pressed
                if menu_button.collidepoint(mouse_pos):
                    sound.button_sound()
                    keep_timer = False
                    main_menu = True

        # continuously draw the timer
        draw.draw_timer(timer)

    return main_menu