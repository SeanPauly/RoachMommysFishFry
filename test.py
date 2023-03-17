import pygame
import os

# Initialize Pygame
pygame.init()

# Set up the display window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Boiling Frames Animation")

# Load the images into a list
frame_images = []
for i in range(8):
    filename = f"Boil_Frames/frame_{i}_delay-0.1s-removebg-preview.png"
    frame_images.append(pygame.image.load(os.path.join(filename)).convert_alpha())

# Set up the animation variables
frame_index = 0
frame_count = len(frame_images)
frame_time = 0.01
current_time = 0

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Display the current frame
    screen.blit(frame_images[frame_index], (0, 0))

    # Update the screen
    pygame.display.update()

    # Wait for the specified frame time
    current_time += pygame.time.get_ticks() / 1000
    if current_time >= frame_time:
        # Switch to the next frame
        frame_index = (frame_index + 1) % frame_count
        current_time = 0

# Quit Pygame
pygame.quit()
