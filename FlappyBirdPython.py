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
gravity = 1

# Configuración de los obstáculos
obstacle_width, obstacle_height = 50, random.randint(150, 400)
obstacle_x = width
obstacle_y = height - obstacle_height - 50
obstacle_velocity = 5
obstacle_gap = 200

# Función principal del juego
def run_game():
    global bird_y, bird_velocity, obstacle_x, obstacle_height, obstacle_y

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_velocity = -10

        # Actualizar posición del pájaro
        bird_velocity += gravity
        bird_y += bird_velocity

        # Actualizar posición del obstáculo
        obstacle_x -= obstacle_velocity

        # Verificar colisiones
        if (
            bird_x < obstacle_x + obstacle_width
            and bird_x + bird_width > obstacle_x
            and (bird_y < obstacle_y or bird_y + bird_height > obstacle_y + obstacle_gap)
        ):
            game_over()

        # Verificar si el pájaro pasa el obstáculo
        if obstacle_x + obstacle_width < bird_x:
            obstacle_x = width
            obstacle_height = random.randint(150, 400)
            obstacle_y = height - obstacle_height - 50

        # Verificar límites de pantalla
        if bird_y < 0 or bird_y + bird_height > height:
            game_over()

        # Dibujar en la pantalla
        screen.fill(white)
        pygame.draw.rect(screen, black, (bird_x, bird_y, bird_width, bird_height))
        pygame.draw.rect(screen, black, (obstacle_x, 0, obstacle_width, height - obstacle_height - obstacle_gap))
        pygame.draw.rect(screen, black, (obstacle_x, obstacle_y + obstacle_gap, obstacle_width, obstacle_height))
        pygame.display.flip()

        pygame.time.Clock().tick(30)

# Función para mostrar mensaje de Game Over
def game_over():
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over", True, black)
    screen.blit(text, (width // 2 - 80, height // 2 - 18))
    pygame.display.flip()
    pygame.time.delay(2000)  # Espera 2 segundos antes de salir
    pygame.quit()
    sys.exit()

# Ejecutar el juego
run_game()
