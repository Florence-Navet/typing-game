import pygame
from __settings__ import SCREEN, TEXT_COLOR, TEXT_COLOR_DARK
from display.display_models.__settings__ import BACKGROUND_IMAGE
from display.display_menu import get_buttons
from game.game_functions import clock_tick

def in_main_menu(clock, fps, translator):
    """
        generate main_menu assets for caption, background and
        launch for event loop to handle mouse click and return
        chosen option
    """
    main_button_list = get_buttons(translator)

    title = translator.translate("fruit_slicer")
    location = translator.translate("main_menu")
    caption = f"{title} - {location}"

    current_background = SCREEN.background(BACKGROUND_IMAGE, caption)
    SCREEN.screen.blit(current_background, (0,0))

    while True:
        clock_tick(clock, fps)
        
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    game_menu = "main_menu"
                    return game_menu

            for main_button in main_button_list:  
                if main_button.image_rect.collidepoint(mouse_position):
                    main_button.hovered = True
                    main_button.draw(TEXT_COLOR_DARK)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        game_menu = main_button.identification
                        return game_menu
                else:
                    main_button.hovered = False
                    main_button.draw(TEXT_COLOR)