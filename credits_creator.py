from initialization import *

import draw_functions as draw

import sound_functions as sound

import webbrowser


# creates the screen that displays credits
def credits_creator():
    # draws music image
    music_note = pygame.image.load('Images/music_note.png')
    music_note = pygame.transform.scale(music_note, (width * 0.190, height * 0.451))
    window.blit(music_note, (width * 0.586, height * 0.278))
    music_note_area = pygame.Rect(width * 0.586, height * 0.278, width * 0.190, height * 0.451)

    # formatting
    # -------------------------------------------------------------------------------------------
    window.blit(credits_font_bold_under.render('QuizCabulary was created by Brendan Wyatt, Josh Nelson and Zach Thygesen for TAMUhack 2022.', True, 'black'), (width * 0.163, height * 0.167))
    window.blit(credits_font_bold.render('Main menu music:', True, 'black'), (width * 0.163, height * 0.222))
    window.blit(credits_font_bold.render('Game music:', True, 'black'), (width * 0.163, height * 0.424))

    window.blit(credits_font.render('by', True, 'black'), (width * 0.269, height * 0.271))
    window.blit(credits_font.render('by', True, 'black'), (width * 0.260, height * 0.319))
    window.blit(credits_font.render('by', True, 'black'), (width * 0.227, height * 0.368))
    window.blit(credits_font.render('by', True, 'black'), (width * 0.221, height * 0.472))
    window.blit(credits_font.render('by', True, 'black'), (width * 0.244, height * 0.521))
    window.blit(credits_font.render('by', True, 'black'), (width * 0.207, height * 0.569))
    window.blit(credits_font.render('by', True, 'black'), (width * 0.237, height * 0.618))
    window.blit(credits_font.render('by', True, 'black'), (width * 0.217, height * 0.667))
    window.blit(credits_font.render('by', True, 'black'), (width * 0.245, height * 0.715))
    window.blit(credits_font.render('by', True, 'black'), (width * 0.273, height * 0.764))

    window.blit(credits_font.render('is licensed under', True, 'black'), (width * 0.320, height * 0.271))
    window.blit(credits_font.render('is licensed under', True, 'black'), (width * 0.316, height * 0.319))
    window.blit(credits_font.render('is licensed under', True, 'black'), (width * 0.333, height * 0.368))
    window.blit(credits_font.render('is licensed under', True, 'black'), (width * 0.292, height * 0.472))
    window.blit(credits_font.render('is licensed under', True, 'black'), (width * 0.308, height * 0.521))
    window.blit(credits_font.render('is licensed under', True, 'black'), (width * 0.289, height * 0.569))
    window.blit(credits_font.render('is licensed under', True, 'black'), (width * 0.319, height * 0.618))
    window.blit(credits_font.render('is licensed under', True, 'black'), (width * 0.299, height * 0.667))
    window.blit(credits_font.render('is licensed under', True, 'black'), (width * 0.326, height * 0.715))
    window.blit(credits_font.render('is licensed under', True, 'black'), (width * 0.354, height * 0.764))
    # -------------------------------------------------------------------------------------------

    # creates the links players can click on
    song1, creator1, license1 = draw.create_credit_links('"Eye of the Storm"', 'Joth', 'CC0 1.0.', (width * 0.163, height * 0.271), (width * 0.290, height * 0.271), (width * 0.422, height * 0.271))
    song2, creator2, license2 = draw.create_credit_links('"gimme verse 2"', 'zagi2', 'CC BY-NC 3.0.', (width * 0.163, height * 0.319), (width * 0.280, height * 0.319), (width * 0.416, height * 0.319))
    song3, creator3, license3 = draw.create_credit_links('"Sky Loop"', 'FoolBoyMedia', 'CC BY-NC 3.0.', (width * 0.163, height * 0.368), (width * 0.247, height * 0.368), (width * 0.433, height * 0.368))
    song4, creator4, license4 = draw.create_credit_links('"Strings 1"', 'klaudux', 'CC0 1.0.', (width * 0.163, height * 0.472), (width * 0.242, height * 0.472), (width * 0.393, height * 0.472))
    song5, creator5, license5 = draw.create_credit_links('"Menu Music"', 'mrpoly', 'CC0 1.0.', (width * 0.163, height * 0.521), (width * 0.264, height * 0.521), (width * 0.408, height * 0.521))
    song6, creator6, license6 = draw.create_credit_links('"Rising"', 'HorrorPen', 'CC BY 3.0.', (width * 0.163, height * 0.569), (width * 0.227, height * 0.569), (width * 0.390, height * 0.569))
    song7, creator7, license7 = draw.create_credit_links('"Spirit Waltz"', 'HorrorPen', 'CC BY 3.0.', (width * 0.163, height * 0.618), (width * 0.258, height * 0.618), (width * 0.420, height * 0.618))
    song8, creator8, license8 = draw.create_credit_links('"Intense"', 'HorrorPen', 'CC BY 3.0.', (width * 0.163, height * 0.667), (width * 0.238, height * 0.667), (width * 0.400, height * 0.667))
    song9, creator9, license9 = draw.create_credit_links('"Red Curtain"', 'HorrorPen', 'CC BY 3.0.', (width * 0.163, height * 0.715), (width * 0.265, height * 0.715), (width * 0.426, height * 0.715))
    song10, creator10, license10 = draw.create_credit_links('"House in a Forest"', 'HorrorPen', 'CC BY 3.0.', (width * 0.163, height * 0.764), (width * 0.293, height * 0.764), (width * 0.455, height * 0.764))

    pygame.display.update()
    
    show_credits = True

    # continues until player quits or goes back to main menu
    while show_credits:
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
                    show_credits = False

                # secret
                if music_note_area.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

                # takes the player to the link according to what they pressed
                # --------------------------------------------------------------
                if song1.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://opengameart.org/content/eye-of-the-storm')

                if creator1.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://opengameart.org/users/joth')
                
                if license1.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://creativecommons.org/publicdomain/zero/1.0/')

                if song2.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://freesound.org/people/zagi2/sounds/616763/')

                if creator2.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://freesound.org/people/zagi2/')
                
                if license2.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://creativecommons.org/licenses/by-nc/3.0/')

                if song3.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://freesound.org/people/FoolBoyMedia/sounds/264295/')

                if creator3.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://freesound.org/people/FoolBoyMedia/')
                
                if license3.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://creativecommons.org/licenses/by-nc/3.0/')

                if song4.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://freesound.org/people/klaudux/sounds/265343/')

                if creator4.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://freesound.org/people/klaudux/')
                
                if license4.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://creativecommons.org/publicdomain/zero/1.0/')

                if song5.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://opengameart.org/content/menu-music')

                if creator5.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://opengameart.org/users/mrpoly')
                
                if license5.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://creativecommons.org/publicdomain/zero/1.0/')

                if song6.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://opengameart.org/content/game-music-loop-rising')

                if creator6.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://opengameart.org/users/horrorpen')
                
                if license6.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://creativecommons.org/licenses/by/3.0/')

                if song7.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://opengameart.org/content/spirit-waltz')

                if creator7.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://opengameart.org/users/horrorpen')
                
                if license7.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://creativecommons.org/licenses/by/3.0/')

                if song8.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://opengameart.org/content/game-music-loop-intense')

                if creator8.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://opengameart.org/users/horrorpen')
                
                if license8.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://creativecommons.org/licenses/by/3.0/')

                if song9.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://opengameart.org/content/red-curtain')

                if creator9.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://opengameart.org/users/horrorpen')
                
                if license9.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://creativecommons.org/licenses/by/3.0/')

                if song10.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://opengameart.org/content/loop-house-in-a-forest')

                if creator10.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://opengameart.org/users/horrorpen')
                
                if license10.collidepoint(mouse_pos):
                    sound.button_sound()
                    webbrowser.open('https://creativecommons.org/licenses/by/3.0/')  
                # --------------------------------------------------------------              