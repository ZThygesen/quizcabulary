from initialization import *

import draw_functions as draw

import sound_functions as sound


# awaits player's response to either quit the game or go back to main menu after finishing a game
def play_again():
    waiting = True
    main_menu = False

    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

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
                    waiting = False
                    main_menu = True

    return main_menu

# gives a summary of how the player performed in their single player game
def gameSummarySingle(points):
    draw.draw_play_area()

    # ensures proper grammar
    if points == 1:
        summary = 'You got 1 question correct!'
    else:
        summary = 'You got {} questions correct!'.format(points)

    # writes summary to screen
    window.blit(general_font.render(summary, True, 'black'), (width * 0.351, height * 0.456))
    pygame.display.update()

    return play_again()


# gives a summary of how the players performed in their multiplayer game
def gameSummaryMulti(player1_points, player2_points):
    draw.draw_play_area()

    # ensures proper grammar
    if player1_points == 1:
        summary1 = 'Player 1: 1 point'
    else:
        summary1 = 'Player 1: {} points'.format(player1_points)   

    if player2_points == 1:
        summary2 = 'Player 2: 1 point'
    else:
        summary2 = 'Player 2: {} points'.format(player2_points) 

    # writes summary to screen
    window.blit(general_font.render(summary1, True, 'black'), (width * 0.416, height * 0.351))
    window.blit(general_font.render(summary2, True, 'black'), (width * 0.416, height * 0.490))
    pygame.display.update()

    return play_again()


# gives a summary of how the player performed in their time trial
def gameSummaryTime(elapsed_time):
    draw.draw_play_area()

    # writes summary to screen
    summary = 'You completed 10 questions in {} seconds!'.format(elapsed_time)
    window.blit(general_font.render(summary, True, 'black'), (width * 0.281, height * 0.456))
    pygame.display.update()

    return play_again()