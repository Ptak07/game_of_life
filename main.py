import sys

import pygame
import os
import grid

def main():
    os.environ["SDL_VIDEO_CENTERED"] = '1'

    width, height = 1920, 1080
    size = (width, height)

    pygame.init()
    pygame.display.set_caption("GAME OF LIFE")
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 30

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 80, 255)

    scale = 30
    offset = 1

    Grid = grid.Grid(width, height, scale, offset)
    Grid.random_array()

    pause = False
    run = True

    while run:
        clock.tick(fps)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    pause = not pause
                if event.key == pygame.K_c:
                    Grid.clear_array()
                if event.key == pygame.K_r:
                    Grid.random_array()

        Grid.conway(off_color=WHITE, on_color=BLUE, surface=screen, pause=pause)

        if pygame.mouse.get_pressed()[0]:
            mouseX, mouseY = pygame.mouse.get_pos()
            Grid.handle_left_mouse(mouseX, mouseY)

        if pygame.mouse.get_pressed()[2]:
            mouseX, mouseY = pygame.mouse.get_pos()
            Grid.handle_right_mouse(mouseX, mouseY)

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()


