import pygame

pygame.init()

screen_width, screen_height = 1000, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Great Britain Poster")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

british_flag = pygame.image.load('flag.png')
british_flag = pygame.transform.scale(british_flag, (200, 120))

tea_image = pygame.image.load('tea.jpg')

tower_image = pygame.image.load('tower.png')
tower_image = pygame.transform.scale(tower_image, (200, 200))

shakespeare_image = pygame.image.load('shakespeare.jpeg')
shakespeare_image = pygame.transform.scale(shakespeare_image, (200, 200))

font_title = pygame.font.Font(None, 80)
font_subtitle = pygame.font.Font(None, 40)
font_text = pygame.font.Font(None, 30)

title_text = font_title.render("Welcome to Great Britain", True, RED)
subtitle_text = font_subtitle.render("Famous for its rich history and culture", True, BLUE)
fact1 = font_text.render("Great Britain is known for its monarchy, famous landmarks,", True, WHITE)
fact2 = font_text.render("and cultural contributions. It has been home to iconic", True, WHITE)
fact3 = font_text.render("figures like William Shakespeare, and traditions like", True, WHITE)
fact4 = font_text.render("afternoon tea. London, the capital, is a vibrant mix of", True, WHITE)
fact5 = font_text.render("history and modernity, with sights such as the Tower of London.", True, WHITE)

pygame.mixer.music.load("gb.mp3")
pygame.mixer.music.play(-1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((50, 50, 50))

    pygame.draw.rect(screen, RED, [50, 100, 900, 5])
    pygame.draw.rect(screen, RED, [50, 500, 900, 5])

    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 20))
    screen.blit(subtitle_text, (350, 150))
    screen.blit(fact1, (350, 200))
    screen.blit(fact2, (350, 230))
    screen.blit(fact3, (350, 260))
    screen.blit(fact4, (350, 290))
    screen.blit(fact5, (350, 320))

    screen.blit(british_flag, (100, 150))
    screen.blit(tea_image, (50, 350))
    screen.blit(tower_image, (420, 350))
    screen.blit(shakespeare_image, (720, 350))

    pygame.display.flip()

pygame.quit()

