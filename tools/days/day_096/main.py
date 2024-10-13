from days.day_096.files.helpers import *


def day_096():
    title("SPACE INVADERS")
    from days.day_096.files.config import (
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        OFFSET,
        FPS,
        BLACK,
        YELLOW,
        LEVEL_UI,
        GG_UI,
        SCORE_UI,
        HIGHSCORE_UI,
        FONT,
        pg,
        GameLogic,
        sys,
        random,
    )

    pg.init()

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + (2 * OFFSET)))
    pg.display.set_caption("Space Invaders")
    clock = pg.time.Clock()

    logic = GameLogic(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)

    SHOOT_LASER = pg.USEREVENT
    pg.time.set_timer(SHOOT_LASER, 300)

    MYSTERYSHIP = pg.USEREVENT + 1
    pg.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

    while True:
        # time.sleep(5)
        # Check for events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        if event.type == SHOOT_LASER and logic.run:
            logic.alien_shoot_laser()

        if event.type == MYSTERYSHIP and logic.run:
            logic.create_mystery_ship()
            pg.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] and logic.run == False:
            logic.reset()

        # Update Logic
        if logic.run:
            logic.spaceship_group.update()
            logic.move_aliens()
            logic.alien_lasers_group.update()
            logic.mystery_ship_group.update()
            logic.check_for_collisions()

        # BG
        screen.fill(BLACK)

        # UI
        pg.draw.rect(screen, YELLOW, (10, 10, 780, 780), 2, 0, 60, 60, 60, 60)
        pg.draw.line(screen, YELLOW, (25, 730), (775, 730), 3)

        if logic.run:
            screen.blit(LEVEL_UI, (570, 740, 50, 50))
        else:
            screen.blit(GG_UI, (570, 740, 50, 50))

        x = 50
        for life in range(logic.lives):
            screen.blit(logic.spaceship_group.sprite.image, (x, 745))
            x += 50

        screen.blit(SCORE_UI, (50, 15, 50, 50))
        formatted_score = str(logic.score).zfill(5)
        score_ui = FONT.render(formatted_score, False, YELLOW)
        screen.blit(score_ui, (50, 40, 50, 50))
        screen.blit(HIGHSCORE_UI, (550, 15, 50, 50))
        formatted_highscore = str(logic.highscore).zfill(5)
        highscore_ui = FONT.render(formatted_highscore, False, YELLOW)
        screen.blit(highscore_ui, (625, 40, 50, 50))

        logic.spaceship_group.draw(screen)
        logic.spaceship_group.sprite.lasers_group.draw(screen)
        for obstacle in logic.obstacles:
            obstacle.blocks_group.draw(screen)
        logic.aliens_group.draw(screen)
        logic.alien_lasers_group.draw(screen)
        logic.mystery_ship_group.draw(screen)

        pg.display.update()
        clock.tick(FPS)  # 60 FPS
