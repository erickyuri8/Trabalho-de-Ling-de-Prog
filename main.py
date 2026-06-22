import pygame

print("Setup started")
pygame.init()
window = pygame.display.set_mode(size=(800, 600))
print("Setup ended")

print("Loop started")
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #close window
            quit() #end pygame
