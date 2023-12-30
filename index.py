import serial
import pygame
import random

# pygame setup
pygame.init()
ser = serial.Serial('COM3', baudrate=115200, timeout=1)  # open serial port
initial = 100
screen = pygame.display.set_mode((initial * 16, initial * 9))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE
    screen.fill('#1b1b1b')

    font = pygame.font.Font(None, 36)

    # origin: 75 / 825
    pygame.draw.rect(screen, '#f5f5f5', (73, 75, 5, 750)) # Y Axis Rectangle
    pygame.draw.rect(screen, '#f5f5f5', (75, 823, 1250, 5)) # X Axis Rectangle

    for value in [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]:
        pygame.draw.rect(screen, '#f5f5f5', (75 + value * 20, 825, 1, 20))
        screen.blit(font.render(str(value), True, '#f5f5f5'), (75 + value * 20 - 10, 860))
    
    for value in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]:
        pygame.draw.rect(screen, '#f5f5f5', (55, 825 - (value * 8), 20, 1))
        screen.blit(font.render(str(value), True, '#f5f5f5'), (20, 825 - (value * 8) - 10))

    pygame.display.flip() # put your work on screen

    clock.tick(60)  # limits FPS to 60

ser.close()
pygame.quit()
