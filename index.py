import serial
import pygame

# pygame setup
pygame.init()
ser = serial.Serial('COM3', baudrate=115200, timeout=1)  # open serial port
screen = pygame.display.set_mode((1280, 720))
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

    pygame.draw.rect(screen, '#f5f5f5', (50, 75, 10, 600)) # Y Axis Rectangle
    pygame.draw.polygon(screen, '#f5f5f5', ((45, 75), (55, 60), (65, 75))) # Y Axis Arrow
    screen.blit(font.render("Entfernung in cm", True, '#f5f5f5'), (40, 20)) # Y Axis Text

    # put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

ser.close()
pygame.quit()
