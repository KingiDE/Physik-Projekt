import serial
import pygame
import random

# pygame setup
pygame.init()
ser = serial.Serial('COM3', baudrate=115200, timeout=1)  # open serial port
screen = pygame.display.set_mode((1280, 720))
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

    pygame.draw.rect(screen, '#f5f5f5', (50, 75, 10, 550)) # Y Axis Rectangle
    pygame.draw.polygon(screen, '#f5f5f5', ((45, 75), (55, 60), (65, 75))) # Y Axis Arrow
    screen.blit(font.render("Entfernung in cm", True, '#f5f5f5'), (40, 20)) # Y Axis Text

    pygame.draw.rect(screen, '#f5f5f5', (50, 625, 1100, 10)) # X Axis Rectangle
    pygame.draw.polygon(screen, '#f5f5f5', ((1150, 620), (1165, 630), (1150, 640))) # X Axis Arrow
    screen.blit(font.render("Zeit in s", True, '#f5f5f5'), (1110, 660)) # X Axis Text

    # draw scale markers for x axis
    for second in [5, 10, 15, 20, 25, 30, 35, 40, 45]:
        pygame.draw.rect(screen, '#f5f5f5', (50 + second * 20 - 10, 625, 1, 30))
        screen.blit(font.render(str(second), True, '#f5f5f5'), (50 + second * 20 - 20, 660)) # X Axis Text

    value = ser.readline().decode('UTF-8')

    print(value)
    
    if len(value) > 0:
        points.append(round(float(value), 2))
    
    for i, point in enumerate(points):
        if not i == 0:
            pygame.draw.line(screen, '#f5f5f5', (50 + i * 20 - 10, 625 - (points[i - 1] * 10)), (50 + (i + 1) * 20 - 10, 625 - (points[i] * 10)), 5) 

    pygame.display.flip() # put your work on screen

    clock.tick(60)  # limits FPS to 60

ser.close()
pygame.quit()
