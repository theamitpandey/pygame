import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("MCQ Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
selected_color = (0, 255, 0)  # Color for selected answer

# Fonts
font = pygame.font.Font(None, 36)

# Define questions, answers, and correct answers for each level
questions = [
    "What is 2 + 2?",
    "What is the capital of Italy?",
    "Which gas do plants use for photosynthesis?",
    "Which planet is known as the Red Planet?"
]

answers = [
    ["3", "4", "5", "6"],
    ["Paris", "Berlin", "Rome", "Madrid"],
    ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"],
    ["Mars", "Venus", "Jupiter", "Saturn"]
]

correct_answers = [1, 2, 0, 0]

question_index = 0
selected_option = None
score = 0
level = 1
correct_answers_count = 0

def display_question(index):
    question_text = font.render(questions[index], True, black)
    screen.blit(question_text, (50, 50))
    
    for i, answer in enumerate(answers[index]):
        option_color = selected_color if selected_option == i else black
        answer_text = font.render(answer, True, option_color)
        screen.blit(answer_text, (50, 100 + i * 50))
        
        pygame.draw.circle(screen, option_color, (30, 125 + i * 50), 15, 1)

def main():
    global question_index, selected_option, score, level, correct_answers_count
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                clicked_option = (y - 100) // 50
                if 0 <= clicked_option < len(answers[question_index]):
                    selected_option = clicked_option
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if selected_option is not None:
                    if selected_option == correct_answers[question_index]:
                        print("Correct!")
                        score += 1
                        correct_answers_count += 1
                        if correct_answers_count == 2:
                            level += 1
                            correct_answers_count = 0
                    else:
                        print("Incorrect.")
                    question_index += 1
                    selected_option = None
                    if question_index >= len(questions):
                        question_index = 0
                        if level > 2:
                            print("Game Over. Your final score:", score)
                            running = False
        
        screen.fill(white)
        display_question(question_index)
        
        # Display score and level
        score_text = font.render("Score: " + str(score), True, black)
        screen.blit(score_text, (screen_width - 150, 20))
        
        level_text = font.render("Level: " + str(level), True, black)
        screen.blit(level_text, (screen_width - 150, 60))
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
