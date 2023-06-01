import pygame

pygame.init()

tamanho = (800,600)
display = pygame.display.set_mode(tamanho)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()

pygame.quit()