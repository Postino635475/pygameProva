import pygame 
import sys
import time 

black=(0,0,0)
white=(255,255,255)

# serve per inizializzare tutti gli oggetti creati in pygame
pygame.init()

# scriviamo a schermo
font = pygame.font.SysFont('monospace', 25)

# init la schermata 
size=(800,700)
screen = pygame.display.set_mode(size)

# creiamo un orologio
clock= pygame.time.Clock() # gestione la sincronizzazione tra il prograemma con i tick
A=pygame.image.load('a.png')
# Main loop 
running=True
while running:
    # background
    screen.fill(black)
    for event in pygame.event.get():# lista di tutti gli eventi nell'ultima fase di get
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print('letter '+str(event.key)+" aka '"+ pygame.key.name(event.key)+' down')
            if (event.type==pygame.K_a):
                screen.blit(A,(0,0))
        if event.type == pygame.KEYUP:
            print("letter "+ str(event.key)+" aka '"+ pygame.key.name(event.key)+" up")
    

    keys= pygame.key.get_pressed()
    if keys[pygame.K_a]:
        screen.blit(A, (0,0))
    

    # refresh
    pygame.display.flip()

    #orologio 
    clock.tick(60) # 60 frame al secondo, è basato sull'orologio integrato su sdl
    # può urilizzare tick_busy_loop() più preciso ma più pesante

time.sleep(3)
pygame.quit()
