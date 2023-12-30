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

points = []

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                points = []

    # RENDER YOUR GAME HERE
    screen.fill('#1b1b1b')

    font = pygame.font.Font(None, 36)

    origin_x = 75
    origin_y = 825

    pygame.draw.rect(screen, '#f5f5f5', (73, 75, 5, 750)) # Y Axis Rectangle
    pygame.draw.rect(screen, '#f5f5f5', (origin_x, 823, 1250, 5)) # X Axis Rectangle

    pygame.draw.polygon(screen, '#f5f5f5', ((65, 75), (75, 60), (85, 75))) # Y Axis Arrow
    pygame.draw.polygon(screen, '#f5f5f5', ((1325, 815), (1340, 825), (1325, 835))) # X Axis Arrow

    screen.blit(font.render(str('Entfernung in cm'), True, '#f5f5f5'), (30, 20)) # Y Achse Beschriftung
    screen.blit(font.render(str('Zeit in s'), True, '#f5f5f5'), (1375, origin_y - 10)) # X Achse Beschriftung

    for value in [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]:
        pygame.draw.rect(screen, '#f5f5f5', (origin_x + value * 20, origin_y, 1, 20))
        screen.blit(font.render(str(value), True, '#f5f5f5'), (origin_x + value * 20 - 10, 860))
    
    for value in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]:
        pygame.draw.rect(screen, '#f5f5f5', (origin_x - 20, origin_y - (value * 8), 20, 1))
        screen.blit(font.render(str(value), True, '#f5f5f5'), (20, origin_y - (value * 8) - 10))

    value = ser.readline().decode('UTF-8')
    
    if len(value) > 0:
        points.append(round(float(value), 2))

    for i, point in enumerate(points):
        if not i == 0:
            pygame.draw.line(screen, '#f5f5f5', (origin_x + (i - 1) * 20, origin_y - points[i - 1] * 8), (origin_x + i * 20, origin_y - points[i] * 8))

    pygame.display.flip() # put your work on screen

    clock.tick(60)  # limits FPS to 60

ser.close()
pygame.quit()
