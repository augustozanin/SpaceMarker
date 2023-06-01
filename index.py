import pygame

pygame.init()

tamanho = (600, 600)
display = pygame.display.set_mode(tamanho)
pygame.mixer.music.load("Space.mp3")
pygame.mixer.music.play(-1)
running = True
fundo = pygame.image.load("bg.jpg")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display.blit(fundo, (0, 0))
    pygame.display.update()

pygame.quit()
