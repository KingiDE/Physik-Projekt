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

leading = []

def calculate():
    for i in range(12):
        if i == 0:
            leading.append(random.choice(range(1, 100)))
        else: 
            leading.append(leading[i - 1] + random.choice(range(-8, 8)))
    
calculate()

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
                calculate()

    # RENDER YOUR GAME HERE
    screen.fill('#1b1b1b')

    font = pygame.font.Font(None, 36)

    # draw leading line
    for i, p in enumerate(leading):
        if not i == 0:
            pygame.draw.line(screen, 'purple', (i * 80 + 5, 625 - leading[i - 1] * 5), ((i + 1) * 80 + 5, 625 - leading[i] * 5), 1) 

    pygame.draw.rect(screen, '#f5f5f5', (75, 75, 10, 550)) # Y Axis Rectangle
    pygame.draw.polygon(screen, '#f5f5f5', ((70, 75), (80, 60), (90, 75))) # Y Axis Arrow
    screen.blit(font.render("Entfernung in cm", True, '#f5f5f5'), (60, 20)) # Y Axis Text

    pygame.draw.rect(screen, '#f5f5f5', (75, 625, 1100, 10)) # X Axis Rectangle
    pygame.draw.polygon(screen, '#f5f5f5', ((1175, 620), (1190, 630), (1175, 640))) # X Axis Arrow
    screen.blit(font.render("Zeit in s", True, '#f5f5f5'), (1135, 660)) # X Axis Text

    # draw scale markers for x axis
    for second in [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]:
        pygame.draw.rect(screen, '#f5f5f5', (75 + second * 20 - 10, 625, 1, 30))
        screen.blit(font.render(str(second), True, '#f5f5f5'), (75 + second * 20 - 20, 660)) # X Axis Text

    # and for y axis
    for distance in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        pygame.draw.rect(screen, '#f5f5f5', (55, 625 - (distance * 5), 20, 1))
        screen.blit(font.render(str(distance), True, '#f5f5f5'), (10, 625 - (distance * 5) - 10)) # Y Axis Text

    value = ser.readline().decode('UTF-8')

    print(value)
    
    if len(value) > 0:
        points.append(round(float(value), 2))
    
    for i, point in enumerate(points):
        if not i == 0:
            pygame.draw.line(screen, '#f5f5f5', (75 + i * 20 - 10, 625 - (points[i - 1] * 5)), (75 + (i + 1) * 20 - 10, 625 - (points[i] * 5)), 1) 

    pygame.display.flip() # put your work on screen

    clock.tick(60)  # limits FPS to 60

ser.close()
pygame.quit()
