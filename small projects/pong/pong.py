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

    velocity = 4

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, white, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.velocity
        else:
            self.y += self.velocity

def draw(screen, leftPaddle, rightPaddle):
    screen.fill(black)
    leftPaddle.draw(screen)
    rightPaddle.draw(screen)

    pygame.display.update()


def handlePaddleMovement(keys, leftPaddle, rightPaddle):
    if keys[pygame.K_w] and leftPaddle.y - leftPaddle.velocity >= 0:
        leftPaddle.move()
    if keys[pygame.K_s] and leftPaddle.y + leftPaddle.velocity + leftPaddle.height <= height :
        leftPaddle.move(False)
    if keys[pygame.K_UP] and rightPaddle.y - rightPaddle.velocity >= 0:
        rightPaddle.move()
    if keys[pygame.K_DOWN] and rightPaddle.y + rightPaddle.velocity + rightPaddle.height <= height :
        rightPaddle.move(False)
        
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
        
        keys = pygame.key.get_pressed()
        handlePaddleMovement(keys, leftPaddle, rightPaddle)
    
    pygame.quit()



if __name__ == '__main__':
    print(__name__)
    main()


