import pygame

pygame.init()


width, height = 700, 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

fps = 120

black = (0,0,0)
white = (255, 255, 255)

paddleWidth, paddleHeight= 20, 100

class Paddle:

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

class Ball():
    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = 5
        self.y_vel = 0

    def draw(self, screen):
        pygame.draw.circle(screen, white, (self.x, self.y), self.radius)
        
    def move(self):
        self.x+= self.x_vel
        self.y+= self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.x_vel *= -1
        self.y_vel = 0
        

def draw(screen, leftPaddle, rightPaddle, ball):
    screen.fill(black)
    leftPaddle.draw(screen)
    rightPaddle.draw(screen)
    ball.draw(screen)
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

def handleCollison(ball, leftPaddle, rightPaddle):
    if ball.y + ball.radius >= height:
        ball.y_vel *= -1
    elif ball.y - ball.radius < 0:
        ball.y_vel *= -1

    
    if ball.x_vel < 0:
        if ball.y >= leftPaddle.y and ball.y <= leftPaddle.y + leftPaddle.height:
            if ball.x - ball.radius < leftPaddle.width + leftPaddle.x:
                ball.x_vel *= -1

                middle_y = leftPaddle.y + leftPaddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (leftPaddle.height / 2) / 5
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel

    else:
        if ball.y >= rightPaddle.y and ball.y <= rightPaddle.y + rightPaddle.height:
            if ball.x + ball.radius > rightPaddle.x:
                ball.x_vel *= -1

                middle_y = rightPaddle.y + rightPaddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (rightPaddle.height / 2) / 5
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel
def main():
    run = True
    clock = pygame.time.Clock()

    leftPaddle = Paddle(10, height//2-paddleHeight//2, paddleWidth, paddleHeight)
    rightPaddle = Paddle(width - 10 - paddleWidth, height//2-paddleHeight//2, paddleWidth, paddleHeight)
    ball = Ball(width//2, height//2, 7)

    while run:
        clock.tick(fps)

        draw(screen, leftPaddle, rightPaddle, ball)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        handlePaddleMovement(keys, leftPaddle, rightPaddle)
        handleCollison(ball, leftPaddle, rightPaddle)
        ball.move()

        if ball.x < 0:
            ball.reset()
        elif ball.x > width:
            ball.reset()


    pygame.quit()



if __name__ == '__main__':
    main()


