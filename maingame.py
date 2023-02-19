import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Define some fonts
TITLE_FONT = pygame.font.Font(None, 100)
SUBTITLE_FONT = pygame.font.Font(None, 50)
FONT = pygame.font.Font(None, 36)

# Define the possible words for the game
WORDS = ["FISH", "SHRIMP", "LOBSTER", "OYSTER", "CLAM", "CRAB"]

# Define the possible difficulty levels
difficulty_levels = ["Easy", "Medium", "Hard"]

# Set the initial difficulty level
difficulty_index = 0

# Define the function to display the splash screen
def splash_screen():
    # Draw the background
    screen.fill(BLACK)

    # Draw the title
    title_text = TITLE_FONT.render("Roach Mommy's", True, GREEN)
    screen.blit(title_text, [100, 100])

    # Draw the subtitle
    subtitle_text = SUBTITLE_FONT.render("Fish Fry", True, WHITE)
    screen.blit(subtitle_text, [300, 200])

    # Update the screen
    pygame.display.update()

    # Wait for a short time
    pygame.time.wait(2000)

    # Display the menu screen
    menu_screen()


# Define the function to display the menu screen
def menu_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    play_game()
                elif event.key == pygame.K_2:
                    settings_screen()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        screen.fill(BLACK)
        title_text = TITLE_FONT.render("Roach Mommy's Fish Fry", True, WHITE)
        play_text = FONT.render("1. Play", True, WHITE)
        settings_text = FONT.render("2. Settings", True, WHITE)
        instructions_text = FONT.render("Press 1 or 2 to Choose, or Escape to Quit", True, WHITE)
        screen.blit(title_text, [50, 100])
        screen.blit(play_text, [200, 300])
        screen.blit(settings_text, [200, 400])
        screen.blit(instructions_text, [50, 600])
        pygame.display.update()

# Define the function to display the settings screen
def settings_screen():
    global difficulty_index

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu_screen()
                elif event.key == pygame.K_UP:
                    difficulty_index = (difficulty_index + 1) % len(difficulty_levels)
                elif event.key == pygame.K_DOWN:
                    difficulty_index = (difficulty_index - 1) % len(difficulty_levels)

        screen.fill(BLACK)
        title_text = TITLE_FONT.render("Settings", True, WHITE)
        difficulty_text = FONT.render("Difficulty Level: " + difficulty_levels[difficulty_index], True, WHITE)
        instructions_text = FONT.render("Press Up or Down to Change Difficulty, or Escape to Return to Menu", True, WHITE)
        screen.blit(title_text, [50, 100])
        screen.blit(difficulty_text, [200, 300])
        screen.blit(instructions_text, [50, 600])
        pygame.display.update()

# Define the function to play the game
def play_game():
    # Choose a random word from the list
    word = random.choice(WORDS)

    # Set the number of attempts based on the difficulty level
    if difficulty_levels[difficulty_index] == "Easy":
        attempts = 10
    elif difficulty_levels[difficulty_index] == "Medium":
        attempts = 8
    elif difficulty_levels[difficulty_index] == "Hard":
        attempts = 6

    # Create a list of underscores to represent the hidden letters
    hidden_word = ["_"] * len(word)

    # Loop until the player wins or runs out of attempts
    while attempts > 0 and "_" in hidden_word:
        # Clear the screen
        screen.fill(BLACK)

        # Display the word and the number of attempts
        word_text = FONT.render(" ".join(hidden_word), True, WHITE)
        attempts_text = FONT.render("Attempts: " + str(attempts), True, WHITE)
        screen.blit(word_text, [50, 200])
        screen.blit(attempts_text, [50, 100])

        # Update the screen
        pygame.display.update()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    # Convert the letter to uppercase
                    letter = event.unicode.upper()

                    # Check if the letter is in the word
                    if letter in word:
                        # Replace the underscores with the letter
                        for i in range(len(word)):
                            if word[i] == letter:
                                hidden_word[i] = letter
                    else:
                        # Decrement the number of attempts
                        attempts -= 1

    # Check if the player won or lost
    if "_" not in hidden_word:
        result_text = TITLE_FONT.render("You Win!", True, GREEN)
    else:
        result_text = TITLE_FONT.render("You Lose!", True, WHITE)

    # Display the result
    screen.fill(BLACK)
    screen.blit(result_text, [50, 100])
    pygame.display.update()

    # Wait for a short time
    pygame.time.wait(2000)

    # Return to the menu screen
    menu_screen()

# Call the splash screen function
splash_screen()

