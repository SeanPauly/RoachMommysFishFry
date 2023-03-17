import os
import random
import pygame

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()
pygame.mixer.init()


# Load the audio file
lose_sound = pygame.mixer.Sound('sounds/lose.mp3')
game_sound = pygame.mixer.Sound('sounds/game.mp3')
correct = pygame.mixer.Sound('SE\Correct.mp3')
lever = pygame.mixer.Sound('SE\Lever.mp3')
rope = pygame.mixer.Sound('SE\Rope.mp3')
wrong = pygame.mixer.Sound('SE\Wrong.mp3')
FONT = pygame.font.Font(None, 36)
# Set screen size
SCREEN_WIDTH = 920
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set font for text
font = pygame.font.Font(None, 50)


# Define the possible words for the game
Easy_WORDS = ['apple', 'banana', 'car', 'dog', 'cat', 'book', 'chair', 'tree', 'bird', 'flower',               
              'happy', 'sad', 'good', 'bad', 'funny', 'serious', 'hot', 'cold', 'tall', 'short',              
              'big', 'small', 'fast', 'slow', 'light', 'heavy', 'loud', 'quiet', 'clean', 'dirty',               
              'hard', 'soft', 'sharp', 'dull', 'thick', 'thin', 'sweet', 'sour', 'spicy', 'bitter',               
              'healthy', 'sick', 'old', 'young', 'rich', 'poor', 'happy', 'angry', 'tired', 'awake',              
              'thin', 'fat', 'beautiful', 'ugly', 'nice', 'mean', 'big', 'little', 'smart', 'dumb',               
              'easy', 'difficult', 'simple', 'complicated', 'bright', 'dark', 'smooth', 'rough',               
              'straight', 'curvy', 'wet', 'dry', 'fresh', 'stale', 'delicious', 'gross', 'strong',               
              'weak', 'empty', 'full', 'right', 'wrong', 'true', 'false', 'real', 'fake', 'solid',               
              'liquid', 'gas', 'loud', 'soft', 'old', 'new', 'fast', 'slow', 'dark', 'light',                   
              'thick', 'thin', 'tall', 'short']

Medium_WORDS = ['aberration', 'abhorrence', 'abstemious', 'accede', 'accolade', 'acerbic', 'acquiesce', 
                'adamant', 'admonish', 'adroit', 'affable', 'alacrity', 'alias', 'alleviate', 'aloof', 
                'ambivalent', 'ameliorate', 'amenable', 'anachronistic', 'anathema', 'anomaly', 'antediluvian', 
                'antipathy', 'apathetic', 'apocryphal', 'approbation', 'arduous', 'articulate', 'ascetic', 
                'assiduous', 'audacity', 'austere', 'avarice', 'aversion', 'banal', 'bastion', 'belligerent', 
                'benign', 'bereft', 'blasphemy', 'bolster', 'bombastic', 'boon', 'bourgeois', 'brusque', 
                'cacophony', 'callous', 'candor', 'capacious', 'capitulate', 'carouse', 'castigate', 'caustic', 
                'celibate', 'censure', 'chicanery', 'churlish', 'circumlocution', 'circumspect', 'clemency', 
                'clique', 'cogent', 'coherent', 'collusion', 'commensurate', 'complicity', 'conciliatory', 
                'condescension', 'confidant', 'congenial', 'congruity', 'connive', 'consensus', 'consign', 
                'consternation', 'consummate', 'contemptuous', 'contentious', 'contravene', 'contrite', 
                'conundrum', 'convergence', 'convivial', 'copious', 'corpulent', 'corroborate', 'cower', 
                'craven', 'credence', 'credulous', 'cryptic', 'culpable', 'cumbersome', 'curtail', 'cynical']

Hard_WORDS = ['abstemiousness', 'abstruse', 'acrimonious', 'adumbrate', 'aesthete', 'altruism', 'anodyne', 
              'antediluvianism', 'antinomy', 'apoplectic', 'arbitrage', 'ascertain', 'asperity', 'assiduity', 
              'augury', 'autodidact', 'bibliophile', 'blandishment', 'cachinnate', 'calumniate', 'canard', 
              'capricious', 'cavil', 'charlatan', 'chicanery', 'chimera', 'cogitate', 'commodious', 'compendium', 
              'concinnity', 'concomitant', 'concupiscence', 'conflate', 'connubial', 'contumacious', 'convalesce', 
              'conviviality', 'coruscant', 'cosset', 'crepuscular', 'cupidity', 'defenestration', 'deleterious', 
              'demagogue', 'denouement', 'deontological', 'depredation', 'deracinate', 'desuetude', 'diaphanous', 
              'didacticism', 'diffidence', 'discomfit', 'disparate', 'disquietude', 'divestiture', 'doughty', 
              'efficacious', 'effulgent', 'egregious', 'eleemosynary', 'emolument', 'encomiastic', 'enervate', 
              'engender', 'enigmatic', 'ephemeral', 'epistemology', 'equivocate', 'ersatz', 'esoteric', 'evanescent', 
              'excoriate', 'execration', 'exegesis', 'exemplar', 'exiguity', 'exiguous', 'exorbitant', 'expatiate', 
              'expedient', 'expurgate', 'extemporaneous', 'extirpate', 'factitious', 'factotum', 'fastidious', 'fatuous', 
              'febrile', 'felicitous', 'feral', 'feuilleton', 'filigree', 'flagitious', 'flibbertigibbet', 'flummox', 'frangible']


# Define the possible difficulty levels
difficulty_levels = ["Easy", "Medium", "Hard"]

# Set the initial difficulty level
difficulty_index = 0

cr_image = pygame.image.load('Images/CreditsScreen.png')
cr_image = pygame.transform.scale(cr_image, (SCREEN_WIDTH-100, SCREEN_HEIGHT-100))
ru_image = pygame.image.load('Images/RulesScreen.png')
ru_image = pygame.transform.scale(ru_image, (SCREEN_WIDTH-100, SCREEN_HEIGHT-100))
bg_image = pygame.image.load('Images/RMFFTitleCard.png')
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
ga_image = pygame.image.load('Images/GameScreen.png')
ga_image = pygame.transform.scale(ga_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
go_image = pygame.image.load('Images/GameOver.png')
go_image = pygame.transform.scale(go_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
wi_image = pygame.image.load('Images/WinScreen.png')
wi_image = pygame.transform.scale(wi_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up splash screen
splash_screen_text = font.render("Welcome to My Game", True, WHITE)
splash_screen_text_rect = splash_screen_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))


button_width = 150
button_height = 50

guess_width = 250
guess_height = 150

# Set up menu screen
play_button_img = pygame.image.load("Images\ButtonFrames\PlayButton\playbuttonframe_0.png")
play_button_img = pygame.transform.scale(play_button_img, (button_width, button_height))
credits_button_img = pygame.image.load("Images\ButtonFrames\CreditsButton\creditsbuttonframe_0.png")
credits_button_img = pygame.transform.scale(credits_button_img, (button_width, button_height))
quit_button_img = pygame.image.load("Images\ButtonFrames\QuitButton\quitbuttonframe_0.png")
quit_button_img = pygame.transform.scale(quit_button_img, (button_width, button_height))
gu_image = pygame.image.load('Images/Guess-O-Tron.png')
gu_image = pygame.transform.scale(gu_image, (guess_width, guess_height))
guess_rect = gu_image.get_rect(center=(SCREEN_WIDTH * .185, 150))

button_y = 125
menu_screen_play_button_rect = play_button_img.get_rect(center=(SCREEN_WIDTH * .925, button_y))
menu_screen_credits_button_rect = credits_button_img.get_rect(center=(SCREEN_WIDTH * .915, button_y+175))
menu_screen_quit_button_rect = quit_button_img.get_rect(center=(SCREEN_WIDTH * .915, button_y+350))



# Set up rules screen

rules_screen_img_rect = ru_image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))


# Set up pause screen
pause_screen_resume_button_text = font.render("Resume", True, WHITE)
pause_screen_resume_button_rect = pause_screen_resume_button_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2-50))
pause_screen_restart_button_text = font.render("Restart", True, WHITE)
pause_screen_restart_button_rect = pause_screen_restart_button_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
pause_screen_quit_to_title_button_text = font.render("Quit to Title", True, WHITE)
pause_screen_quit_to_title_button_rect = pause_screen_quit_to_title_button_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2+50))

# Set up credits screen
credits_screen_img_rect = cr_image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))


# Set up game screen
game_screen_text = font.render("This is the game screen", True, WHITE)
game_screen_text_rect = game_screen_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))


# Set initial screen to splash screen
global current_screen
current_screen = "menu"

# Define the function to play the game
def play_game():
    # Initialize game variables
    num_wins = 0
    num_games = 0
    max_num_games = 3
    attempts = 6
    screen.blit(ga_image, (0, 0))

    # Main game loop
    while num_wins < max_num_games: 
        if num_wins == 0:
            word = random.choice(Easy_WORDS)
        elif num_wins == 1:
            word = random.choice(Medium_WORDS)       
        elif num_wins == 2:
            word = random.choice(Hard_WORDS)

        # Create a list of underscores to represent the hidden letters
        hidden_word = ["_"] * len(word)

        rm_frame_images = []
        for i in range(8):
            filename = f"Images/RoachMommy_Frames/frame_{i}_delay-0.1s-removebg-preview.png"
            rm_frame_images.append(pygame.image.load(os.path.join(filename)).convert_alpha())

        # Set up the animation variables
        rm_frame_index = 0
        rm_frame_count = len(rm_frame_images)
        rm_frame_time = 0.1
        current_time = 0



        # Load the images into a list
        boil_frame_images = []
        for i in range(8):
            filename = f"Images/Boil_Frames/frame_{i}_delay-0.1s-removebg-preview.png"
            boil_frame_images.append(pygame.image.load(os.path.join(filename)).convert_alpha())

        # Set up the animation variables
        boil_frame_index = 0
        boil_frame_count = len(boil_frame_images)
        frame_time = 0.01
        current_time = 0

        # Loop until the player wins or runs out of attempts
        while attempts > 0 and "_" in hidden_word:
            # Clear the screen and display the background
            screen.blit(ga_image, (0, 0))

            # Display the word and the number of attempts
            word_text = FONT.render(" ".join(hidden_word), True, WHITE)
            attempts_text = FONT.render("Attempts: " + str(attempts), True, WHITE)
            screen.blit(gu_image, guess_rect)
            screen.blit(word_text, [115, 145]) 
            screen.blit(attempts_text, [100, 115])
            screen.blit(boil_frame_images[boil_frame_index], (175, 330))
            screen.blit(rm_frame_images[rm_frame_index], (300, 115))

            # Wait for the specified frame time
            current_time += pygame.time.get_ticks() / 1000
            if current_time >= frame_time:
                # Switch to the next frame
                boil_frame_index = (boil_frame_index + 1) % boil_frame_count
                current_time = 0            
            elif current_time >= rm_frame_time:
                # Switch to the next frame
                rm_frame_index = (rm_frame_index + 1) % rm_frame_count
                current_time = 0            

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.unicode.isalpha():
                        # Convert the letter to uppercase
                        letter = event.unicode.lower()
                        # Check if the letter is in the word
                        if letter in word:
                            correct.play()
                            # Replace the underscores with the letter
                            for i in range(len(word)):
                                if word[i] == letter:
                                    hidden_word[i] = letter
                        else:
                            wrong.play()
                            lever.play()
                            # Decrement the number of attempts
                            attempts -= 1

            # Update the screen
            pygame.display.update()


        # Check if the player won or lost
        if "_" not in hidden_word:
            num_wins += 1
            screen.blit(wi_image, (0, 0))
            attempts = 6
            # win_sound.play()
        else:
            screen.blit(go_image, (0, 0))
            # lose_sound.play()

        # Increment the number of games played
        num_games += 1

        # Display the result
        pygame.display.update()

        # Wait for a short time before continuing to the next game
        pygame.time.wait(3000)

    # Display the game over screen
    # game_over_sound.play()

    # Update the screen
    pygame.display.update()

    # Wait for a short time before quitting the game
    pygame.time.wait(5000)



 

done = False
while not done:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if current_screen == "game":
                current_screen = "pause"
        elif event.type == pygame.KEYDOWN and event.key != pygame.K_ESCAPE:
            if current_screen == "rules":
                current_screen = "game"
            elif current_screen == "credits":
                current_screen = "menu"
            elif current_screen == "pause":
                current_screen = "game"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if current_screen == "menu":
                if menu_screen_play_button_rect.collidepoint(mouse_pos):
                    current_screen = "rules"
                elif menu_screen_credits_button_rect.collidepoint(mouse_pos):
                    current_screen = "credits"
                elif menu_screen_quit_button_rect.collidepoint(mouse_pos):
                    done = True
            elif current_screen == "rules":
                    current_screen = "rules"
            elif current_screen == "pause":
                if pause_screen_resume_button_rect.collidepoint(mouse_pos):
                    current_screen = "game"
                elif pause_screen_restart_button_rect.collidepoint(mouse_pos):
                    current_screen = "rules"
                elif pause_screen_quit_to_title_button_rect.collidepoint(mouse_pos):
                    current_screen = "menu"

    # Draw current screen
    screen.fill(BLACK)
    if current_screen == "splash":
        screen.blit(splash_screen_text, splash_screen_text_rect)
    elif current_screen == "menu":
        screen.blit(bg_image, (0, 0))
        screen.blit(play_button_img, menu_screen_play_button_rect)
        screen.blit(credits_button_img, menu_screen_credits_button_rect)
        screen.blit(quit_button_img, menu_screen_quit_button_rect)
    elif current_screen == "rules":
        screen.blit(ru_image, rules_screen_img_rect)
    elif current_screen == "game":
        play_game()
    elif current_screen == "pause": 
        screen.blit(pause_screen_resume_button_text, pause_screen_resume_button_rect)
        screen.blit(pause_screen_restart_button_text, pause_screen_restart_button_rect)
        screen.blit(pause_screen_quit_to_title_button_text, pause_screen_quit_to_title_button_rect)
    elif current_screen == "credits":
        screen.blit(cr_image, credits_screen_img_rect)
    pygame.display.flip()

pygame.quit()



