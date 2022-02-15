import pygame
pygame.init()


width, height = 700, 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

fps = 60

black = (0,0,0)
white = (255, 255, 255)

paddleWidth, paddleHeight= 20, 100

class Paddle():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, white, (self.x, self.y, self.width, self.height))

def draw(screen, leftPaddle, rightPaddle):
    screen.fill(black)
    leftPaddle.draw(screen)
    rightPaddle.draw(screen)

    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()

    leftPaddle = Paddle(10, height//2-paddleHeight//2, paddleWidth, paddleHeight)
    rightPaddle = Paddle(width - 10 - paddleWidth, height//2-paddleHeight//2, paddleWidth, paddleHeight)

    while run:
        clock.tick(fps)

        draw(screen, leftPaddle, rightPaddle)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()



if __name__ == '__main__':
    main()


