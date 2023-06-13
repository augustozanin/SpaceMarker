import pygame
import time
from tkinter import simpledialog
pygame.init()
# Objeto estrela


class Estrela:
    # comando self é quando se trata do proprio objeto
    # função inicial que recebe posicao e nome
    def __init__(self, pos, nome):
        self.pos = pos
        self.nome = nome
    # funcao para desenhar os circulos de cada estrela

    def desenhar(self, surface):
        texto5 = font.render(self.nome, True, (255, 255, 255))
        display.blit(texto5, (self.pos))
        branco = (255, 255, 255)
        pygame.draw.circle(surface, branco, self.pos, 3)

        for outra_estrela in estrelas:
            if outra_estrela != self:
                pygame.draw.line(surface, branco, self.pos,
                                 outra_estrela.pos, 1)

    # funcao para exibir no console cada estrela cadastrada
    def __str__(self):
        return f"Estrela: {self.nome} - Posicao: {self.pos}"


        

estrelas = []
tamanho = (600, 600)
display = pygame.display.set_mode(tamanho)
pygame.mixer.music.load("Space.mp3")
pygame.mixer.music.play(-1)
running = True
fundo = pygame.image.load("bg.jpg")
logo = pygame.image.load("space.png")
pygame.display.set_caption("Space Marker")
pygame.display.set_icon(logo)
font = pygame.font.Font(None, 17)


def adicionar_estrela():
    item = simpledialog.askstring("Space", "Nome da estrela:")
    if item is None or item.strip() == "":
        item = "desconhecido" + str(pos)
    estrela = Estrela(pos, item)
    estrelas.append(estrela)
    print(estrela)


def salvar_estrela(estrelas):
    print("executou a função salvar estrela")
    with open("bd.estrelas", "a") as arquivo:
        for estrela in estrelas:
            arquivo.write(str(estrela) + '\n')
    print("Dados salvos")


def delete_estrela(estrelas):
    confirmacao = input("Tem certeza que deseja deletar todos os registros? (S/N): ")
    if confirmacao.upper() == "S":
        estrelas.clear()
        arquivo = open("bd.estrelas", "w")
        arquivo.close()
        print("Registros deletados")



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            adicionar_estrela()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
            print("Tecla F10 pressionada!")
            salvar_estrela(estrelas)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            print("Tecla F11 pressionada!")

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F12:
            print("Tecla F12 pressionada!")
            delete_estrela(estrelas)

    display.blit(fundo, (0, 0))
    for estrela in estrelas:
        estrela.desenhar(display)
    texto = font.render(
        "Pressione F10 para Salvar os Pontos", True, (255, 255, 255))
    texto2 = font.render(
        "Pressione F11 para Carregar os Pontos", True, (255, 255, 255))
    texto3 = font.render(
        "Pressione F12 para Deletar os Pontos", True, (255, 255, 255))
    display.blit(texto, (10, 10))
    display.blit(texto2, (10, 30))
    display.blit(texto3, (10, 50))

    pygame.display.update()

pygame.quit()
