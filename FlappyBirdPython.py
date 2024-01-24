import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird Replica")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)

# Configuración del pájaro
bird_width, bird_height = 50, 40
bird_x = width // 4
bird_y = height // 2 - bird_height // 2
bird_velocity = 5
jump_height = 10
gravity = 1

# Configuración de los obstáculos
obstacle_width, obstacle_height = 50, random.randint(150, 400)
obstacle_x = width
obstacle_y = height - obstacle_height - 50
obstacle_velocity = 5
obstacle_gap = 200

# Puntaje
score = 0

# Función principal del juego
def run_game():
    global bird_y, bird_velocity, obstacle_x, obstacle_height, obstacle_y, score

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_velocity = -jump_height

                # Agregar la opción de continuar después de morir
                if event.key == pygame.K_RETURN:
                    reset_game()

        # Actualizar posición del pájaro
        bird_velocity += gravity
        bird_y += bird_velocity

        # Actualizar posición del obstáculo
        obstacle_x -= obstacle_velocity

        # Verificar si el pájaro pasa el obstáculo y actualizar el puntaje
        if obstacle_x + obstacle_width < bird_x:
            score += 1
            obstacle_x = width
            obstacle_height = random.randint(150, 400)
            obstacle_y = height - obstacle_height - 50

        # Verificar colisiones
        if (
            bird_x < obstacle_x + obstacle_width
            and bird_x + bird_width > obstacle_x
            and (bird_y < obstacle_y or bird_y + bird_height > obstacle_y + obstacle_gap)
        ):
            game_over()

        # Verificar límites de pantalla
        if bird_y < 0:
            bird_y = 0
            bird_velocity = 0
        elif bird_y + bird_height > height:
            game_over()

        # Dibujar en la pantalla
        screen.fill(white)
        pygame.draw.rect(screen, black, (bird_x, bird_y, bird_width, bird_height))
        pygame.draw.rect(screen, black, (obstacle_x, 0, obstacle_width, obstacle_y))
        pygame.draw.rect(screen, black, (obstacle_x, obstacle_y + obstacle_gap, obstacle_width, height - obstacle_y - obstacle_gap))

        # Mostrar puntaje
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, black)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

        pygame.time.Clock().tick(30)

# Función para mostrar mensaje de Game Over y opción de continuar
def game_over():
    global score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Game Over - Score: {score}", True, black)
    screen.blit(text, (width // 2 - 120, height // 2 - 18))

    # Mostrar opción para continuar
    continue_text = font.render("Press ENTER to continue", True, black)
    screen.blit(continue_text, (width // 2 - 150, height // 2 + 30))

    pygame.display.flip()

    # Esperar hasta que se presione ENTER
    waiting_for_enter = True
    while waiting_for_enter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    reset_game()
                    waiting_for_enter = False  # Salir del bucle cuando se presiona ENTER

        pygame.time.Clock().tick(30)

# Función para reiniciar el juego
def reset_game():
    global bird_y, bird_velocity, obstacle_x, obstacle_height, obstacle_y, score

    bird_y = height // 2 - bird_height // 2
    bird_velocity = 0

    obstacle_x = width
    obstacle_height = random.randint(150, 400)
    obstacle_y = height - obstacle_height - 50

    score = 0

# Ejecutar el juego
run_game()
