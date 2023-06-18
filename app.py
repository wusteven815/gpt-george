import pygame
import sys

# Initialize Pygame
pygame.init()
pygame.display.set_caption("GPT George")
size = (700, 500)
screen = pygame.display.set_mode(size)

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

font = pygame.font.Font(None, 25)
messages = ['Welcome to GPT George.', 'Press record voice to start.']
button_text = ['Record Voice', 'Emotion Analysis']
current_messages = ['', '']
index = [0, 0]


def wrap_text(message, width):
    words = message.split(' ')
    lines = []
    current_line = []
    for word in words:
        if font.size(' '.join(current_line + [word]))[0] > width:
            lines.append(' '.join(current_line))
            current_line = [word]
        else:
            current_line.append(word)
    lines.append(' '.join(current_line))
    return lines

def reset_text():
    current_messages = ['', '']
    index = [0, 0]

# Button dimensions
button_width = 100
button_height = 50
button1 = pygame.Rect(size[0] / 2 - button_width - 60, size[1] / 2 - button_height / 2, button_width, button_height)
button2 = pygame.Rect(size[0] / 2 + 60, size[1] / 2 - button_height / 2, button_width, button_height)

# Main loop
done = False
clock = pygame.time.Clock()
while not done:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if buttons are clicked
            if button1.collidepoint(event.pos):
                reset_text()
                print("andy")
            elif button2.collidepoint(event.pos):
                print("bob")

    # Rolling text effect
    for i in range(2):
        if len(current_messages[i]) < len(messages[i]):
            current_messages[i] += messages[i][index[i]]
            index[i] += 1

    # Clear screen
    screen.fill(WHITE)
    pygame.draw.rect(screen, GRAY, button1)
    pygame.draw.rect(screen, GRAY, button2)

    # Draw rectangles and text
    for i in range(2):
        rect_width = size[0] * 0.8
        rect_height = size[1] / 4 - 20
        rect = pygame.Rect(size[0] / 2 - rect_width / 2, size[1] / 4 * (i * 2 + 1) - rect_height / 2, rect_width, rect_height)

        pygame.draw.rect(screen, BLACK, rect, 2)
        wrapped_text = wrap_text(current_messages[i], rect_width - 20)
        for j, line in enumerate(wrapped_text):
            screen.blit(font.render(line, True, BLACK), (rect.x + 10, rect.y + 10 + j * font.size(line)[1]))

        pygame.draw.rect(screen, GRAY, button1)
        button_text = wrap_text('Start Recording', button_width - 20)
        for j, line in enumerate(button_text):
            screen.blit(font.render(line, True, BLACK), (button1.x + 10, button1.y + 10 + j * font.size(line)[1]))

        pygame.draw.rect(screen, GRAY, button2)
        button_text = wrap_text('Emotion Analysis', button_width - 20)
        for j, line in enumerate(button_text):
            screen.blit(font.render(line, True, BLACK), (button2.x + 10, button2.y + 10 + j * font.size(line)[1]))
    


    # Update screen
    pygame.display.flip()
    clock.tick(60)  # Slow down the text rolling speed

pygame.quit()
sys.exit()
