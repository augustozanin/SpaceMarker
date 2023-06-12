import pygame
from tkinter import simpledialog
pygame.init()

estrelas = {}
tamanho = (600, 600)
display = pygame.display.set_mode(tamanho)
pygame.mixer.music.load("Space.mp3")
pygame.mixer.music.play(-1)
running = True
fundo = pygame.image.load("bg.jpg")
logo = pygame.image.load("space.png")
pygame.display.set_caption("Space Marker")
pygame.display.set_icon(logo)
branco = (255, 255, 255)
font = pygame.font.Font(None, 17)


def adicionar_estrela(pos):
    item = simpledialog.askstring("Space", "Nome da estrela:")
    print(item)
    if item is None or item.strip() == "":
        item = "desconhecido" + str(pos)
    estrelas[item] = pos

    pygame.draw.circle(display, branco, (int(pos[0]), int(pos[1])), 30)
    print(estrelas)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            adicionar_estrela(pos)
            



    display.blit(fundo, (0, 0))
    texto = font.render("Pressione F10 para Salvar os Pontos ", True, (255, 255, 255))
    texto2 = font.render("Pressione F11 para Carregar os Pontos ", True, (255, 255, 255))
    texto3 = font.render("Pressione F12 para Deletar os Pontos ", True, (255, 255, 255))
    display.blit(texto, (10, 10))
    display.blit(texto2, (10, 30))
    display.blit(texto3, (10, 50))
    
    pygame.display.update()

pygame.quit()
