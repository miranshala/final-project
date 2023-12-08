import pygame
import sys
import random

class SnakeGame:
    def __init__(self):
        pygame.init()

        self.width, self.height = 600, 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")

        self.clock = pygame.time.Clock()

        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.direction = pygame.K_RIGHT

        self.food = self.generate_food()

    def generate_food(self):
        while True:
            food = (random.randrange(0, self.width // 10) * 10,
                    random.randrange(0, self.height // 10) * 10)
            if food not in self.snake:
                return food

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != pygame.K_DOWN:
                        self.direction = pygame.K_UP
                    elif event.key == pygame.K_DOWN and self.direction != pygame.K_UP:
                        self.direction = pygame.K_DOWN
                    elif event.key == pygame.K_LEFT and self.direction != pygame.K_RIGHT:
                        self.direction = pygame.K_LEFT
                    elif event.key == pygame.K_RIGHT and self.direction != pygame.K_LEFT:
                        self.direction = pygame.K_RIGHT

            self.move_snake()
            self.check_collision()
            self.check_food()

            self.screen.fill((0, 0, 0))

            for segment in self.snake:
                pygame.draw.rect(self.screen, (255, 255, 255), (*segment, 10, 10))

            pygame.draw.rect(self.screen, (255, 0, 0), (*self.food, 10, 10))

            pygame.display.flip()
            self.clock.tick(15)

    def move_snake(self):
        head = self.snake[0]
        x, y = head

        if self.direction == pygame.K_UP:
            y -= 10
        elif self.direction == pygame.K_DOWN:
            y += 10
        elif self.direction == pygame.K_LEFT:
            x -= 10
        elif self.direction == pygame.K_RIGHT:
            x += 10

        self.snake.insert(0, (x, y))

        if self.snake[0] == self.food:
            self.food = self.generate_food()
        else:
            self.snake.pop()

    def check_collision(self):
        head = self.snake[0]
        if (
            head[0] < 0
            or head[0] >= self.width
            or head[1] < 0
            or head[1] >= self.height
            or head in self.snake[1:]
        ):
            pygame.quit()
            sys.exit()

    def check_food(self):
        if self.snake[0] == self.food:
            self.food = self.generate_food()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()

