import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird Replica")

# Cargar imagen del pájaro
bird_image = pygame.image.load(r'C:\Users\Admin\Desktop\sure lock & key\Flappy Bird Python\pajaro.png')
bird_image = pygame.transform.scale(bird_image, (50, 40))

# Configuración del pájaro
bird_rect = bird_image.get_rect()
bird_rect.x = width // 4
bird_rect.y = height // 2 - bird_rect.height // 2
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
    global bird_rect, bird_velocity, obstacle_x, obstacle_height, obstacle_y, score

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
        bird_rect.y += bird_velocity

        # Actualizar posición del obstáculo
        obstacle_x -= obstacle_velocity

        # Verificar si el pájaro pasa el obstáculo y actualizar el puntaje
        if obstacle_x + obstacle_width < bird_rect.x:
            score += 1
            obstacle_x = width
            obstacle_height = random.randint(150, 400)
            obstacle_y = height - obstacle_height - 50

        # Verificar colisiones
        if bird_rect.colliderect(pygame.Rect(obstacle_x, 0, obstacle_width, obstacle_y)) or \
           bird_rect.colliderect(pygame.Rect(obstacle_x, obstacle_y + obstacle_gap, obstacle_width, height - obstacle_y - obstacle_gap)):
            game_over()

        # Verificar límites de pantalla
        if bird_rect.y < 0:
            bird_rect.y = 0
            bird_velocity = 0
        elif bird_rect.y + bird_rect.height > height:
            game_over()

        # Dibujar en la pantalla
        screen.fill((255, 255, 255))
        screen.blit(bird_image, bird_rect)
        pygame.draw.rect(screen, (0, 0, 0), (obstacle_x, 0, obstacle_width, obstacle_y))
        pygame.draw.rect(screen, (0, 0, 0), (obstacle_x, obstacle_y + obstacle_gap, obstacle_width, height - obstacle_y - obstacle_gap))

        # Mostrar puntaje
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

        pygame.time.Clock().tick(30)

# Función para mostrar mensaje de Game Over y opción de continuar
def game_over():
    global score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Game Over - Score: {score}", True, (0, 0, 0))
    screen.blit(text, (width // 2 - 120, height // 2 - 18))

    # Mostrar opción para continuar
    continue_text = font.render("Press ENTER to continue", True, (0, 0, 0))
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
    global bird_rect, bird_velocity, obstacle_x, obstacle_height, obstacle_y, score

    bird_rect.x = width // 4
    bird_rect.y = height // 2 - bird_rect.height // 2
    bird_velocity = 0

    obstacle_x = width
    obstacle_height = random.randint(150, 400)
    obstacle_y = height - obstacle_height - 50

    score = 0

# Ejecutar el juego
run_game()
