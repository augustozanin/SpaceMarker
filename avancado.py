import pygame
import math
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
                distancia = self.calcular_distancia(outra_estrela)
                texto_distancia = font.render(
                    f"{distancia:.2f}", True, (255, 255, 255))
                display.blit(texto_distancia, ((self.pos[0] + outra_estrela.pos[0]) // 2, (self.pos[1] + outra_estrela.pos[1]) // 2))
                pygame.draw.line(surface, branco, self.pos, outra_estrela.pos, 1)
    
    def calcular_distancia(self, outra_estrela):
        dx = outra_estrela.pos[0] - self.pos[0]
        dy = outra_estrela.pos[1] - self.pos[1]
        distancia = math.sqrt(dx**2 + dy**2)
        return distancia
    
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

def carregar_estrela():
    print("Chegou em carregar")
    try:
        with open("bd.estrelas", "r") as arquivo:
            for linha in arquivo:
                # Extrai as informações da estrela da linha
                nome_pos = linha.strip().split(" - ")
                nome = nome_pos[0].split(": ")[1]
                pos_str = nome_pos[1].split(": ")[1]
                pos = tuple(map(int, pos_str.strip("()").split(", ")))
                # Cria um novo objeto Estrela e adiciona à lista estrelas
                estrela = Estrela(pos, nome)
                estrelas.append(estrela)
    except:
        print("deu errado!")
    print("Estrelas carregadas com sucesso!")



def delete_estrela(estrelas):
    confirmacao = simpledialog.askstring("Space","Tem certeza que deseja deletar todos os registros? (S/N): ")
    if confirmacao.upper() == "S":
        estrelas.clear()
        arquivo = open("bd.estrelas", "w")
        arquivo.close()
        print("Registros deletados")


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salvar_estrela()
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            salvar_estrela()
            running = False  
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            adicionar_estrela()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
            print("Tecla F10 pressionada!")
            salvar_estrela(estrelas)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            print("Tecla F11 pressionada!")
            carregar_estrela()

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
