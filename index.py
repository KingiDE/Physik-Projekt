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
leading = []

def calculateLeading():
    for i in range(13):
        if i == 0:
            leading.append(random.choice(range(1, 90)))
        else: 
            generated = leading[i - 1] + random.choice(range(-12, 12))
            if generated < 5: 
                leading.append(5)
            elif generated > 90:
                leading.append(90)
            else: 
                leading.append(generated)

calculateLeading()


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                points = []
                leading = []
                calculateLeading()

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
    
    for value in [0, 20, 40, 60, 80, 100, 120, 140, 160]:
        pygame.draw.rect(screen, '#f5f5f5', (origin_x - 20, origin_y - (value * 4), 20, 1))
        screen.blit(font.render(str(value), True, '#f5f5f5'), (10, origin_y - (value * 4) - 10))

    for i, l in enumerate(leading): # draw leading line
        if not i == 0:
            pygame.draw.line(screen, '#772ac0', (origin_x + (i - 1) * 100, origin_y - leading[i - 1] * 4), (origin_x + i * 100, origin_y - leading[i] * 4)) 

    value = ser.readline().decode('UTF-8')
    
    if len(points) >= 60:
        points = []

    if len(value) > 0:
        points.append(round(float(value), 2))

    for i, point in enumerate(points): # draw points line
        if not i == 0:
            color = '#ff4050' if origin_y - points[i - 1] * 4 < 75 and origin_y - points[i] * 4 < 75 else '#f5f5f5'
            pygame.draw.line(screen, color, (origin_x + (i - 1) * 20, origin_y - points[i - 1] * 4 if origin_y - points[i - 1] * 4 > 75 else 75), (origin_x + i * 20, origin_y - points[i] * 4 if origin_y - points[i] * 4 > 75 else 75))

    pygame.display.flip() # put your work on screen

    clock.tick(60)  # limits FPS to 60

ser.close()
pygame.quit()
