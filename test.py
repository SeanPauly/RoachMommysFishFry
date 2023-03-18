import pygame

# Initialize Pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode((400, 400))


rm_width = 200
rm_height = 125

button_width = 150
button_height = 50

rm_frame_0 = pygame.image.load('Images\RoachMommy_Frames\Frame_0_delay-0.1s.png')
rm_frame_0 = pygame.transform.scale(rm_frame_0, (rm_width, rm_height))

rm_frame_1 = pygame.image.load('Images\RoachMommy_Frames\Frame_1_delay-0.1s.png')
rm_frame_1 = pygame.transform.scale(rm_frame_1, (rm_width, rm_height))

rm_frame_2 = pygame.image.load('Images\RoachMommy_Frames\Frame_2_delay-0.1s.png')
rm_frame_2 = pygame.transform.scale(rm_frame_2, (rm_width, rm_height))

rm_frame_3 = pygame.image.load('Images\RoachMommy_Frames\Frame_3_delay-0.1s.png')
rm_frame_3 = pygame.transform.scale(rm_frame_3, (rm_width, rm_height))

rm_frame_4 = pygame.image.load('Images\RoachMommy_Frames\Frame_4_delay-0.1s.png')
rm_frame_4 = pygame.transform.scale(rm_frame_4, (rm_width, rm_height))

rm_frame_5 = pygame.image.load('Images\RoachMommy_Frames\Frame_5_delay-0.1s.png')
rm_frame_5 = pygame.transform.scale(rm_frame_5, (rm_width, rm_height))

rm_frame_6 = pygame.image.load('Images\RoachMommy_Frames\Frame_6_delay-0.1s.png')
rm_frame_6 = pygame.transform.scale(rm_frame_6, (rm_width, rm_height))

rm_frame_7 = pygame.image.load('Images\RoachMommy_Frames\Frame_7_delay-0.1s.png')
rm_frame_7 = pygame.transform.scale(rm_frame_7, (rm_width, rm_height))


# Load the frames
rm_frame_images = [rm_frame_0, rm_frame_1, rm_frame_2, rm_frame_3, rm_frame_4, rm_frame_5, rm_frame_6, rm_frame_6]

# Set the frame rate
rm_frame_rate = 10 # frames per second

# Set the initial frame index
rm_frame_index = 0

# Set the clock
clock = pygame.time.Clock()

# Start the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Blit the current frame
    screen.blit(rm_frame_images[rm_frame_index], (0, 0))
    # Update the frame index
    rm_frame_index = (rm_frame_index + 1) % len(rm_frame_images)
    # Wait for the next frame
    clock.tick(rm_frame_rate)
    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
