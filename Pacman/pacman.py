import pygame

AMARELO = (255, 255, 0)
PRETO = (0,0,0,)
VELOCIDADE = 0.1
pygame.init()

tela = pygame.display.set_mode((640,480),0)
x = 10
y = 10
raio = 30
vel_x = VELOCIDADE
vel_y = VELOCIDADE

while True:

    # Calcula as regras
    x = x + vel_x
    y = y + vel_y
    if x + raio > 640:
        vel_x = -VELOCIDADE

    if x - raio < 0:
        vel_x = VELOCIDADE

    if y + raio> 480:
        vel_y = -VELOCIDADE

    if y - raio< 0:
        vel_y = VELOCIDADE

    # Pinta
    tela.fill(PRETO) #apagar o rastro
    pygame.draw.circle(tela,AMARELO,(int(x),int(y)),raio,0) #armazenar o desenho
    pygame.display.update() # desenhar de fato

    # Eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()


