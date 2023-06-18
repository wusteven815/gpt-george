import pygame


def truncate_string(text):
    if len(text) <= 80:
        return text
    else:
        truncated_text = text[:80].rsplit(' ', 1)[0]
        return truncated_text


def start_ui_task(get_state):

    pygame.init()
    width, height = 1280, 720
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True
    user_state = ""
    last_user_state = user_state

    user_text = "Play something just like this"
    user_text_counter = 0

    font = pygame.font.Font(r"C:\Windows\Fonts\SegoeUI.ttf", 24)

    while running:

        user_state, gpt_state = get_state()
        if user_state != last_user_state:
            user_text = user_state
            last_user_state = user_state
            user_text_counter = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    user_text = "Hello World!"
                    user_text_counter = 0

        screen.fill((45, 45, 45))

        text = font.render(user_text[:user_text_counter], True, "white")
        text_rect = text.get_rect()
        text_rect.center = (width // 2, 50)
        screen.blit(text, text_rect)

        height = 200
        while True:
            if gpt_state == "":
                break
            render = truncate_string(gpt_state)
            gpt_state = gpt_state.replace(render, "", 1)
            text = font.render(render, True, "white")
            text_rect = text.get_rect()
            text_rect.center = (width // 2, height)
            screen.blit(text, text_rect)
            height += 40

        if user_text_counter < 512:
            user_text_counter += 1

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
