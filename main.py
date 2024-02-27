import pygame
from pygame.math import Vector2
from pygame.rect import Rect
from brick_class import brick



# config:
FRAMERATE = 60
SCREEN_SIZE = Vector2(1200, 800)


# pygame init:
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("")
font = pygame.font.SysFont('Comic Sans MS', 30)

# definitions:
def main():
    # game setup:
    clock = pygame.time.Clock()
    lives = 3
    score = 0
    xpos = 0
    xpos = SCREEN_SIZE.x/2
    ypos = 600
    vx = 0

    bx = 0
    by = 0
    bVx = 5
    bVy = -5

    
    pressed_space = False

    bricks = []
    for i in range (12):
        for j in range (14):
            bricks.append(brick(j*80+50, i*30+80))

    # main loop:
    running = True
    while running:
        delta = clock.tick(FRAMERATE) / 1000

        # input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            if keys [pygame.K_LEFT]:
                vx = -10
            elif keys [pygame.K_RIGHT]:
                vx = 10
            else:
                vx = 0
            if keys [pygame.K_SPACE] and pressed_space == False:
                pressed_space = True

        if pressed_space == False:
            bx = (xpos+50)
            by = (ypos-50)
        else:
            bx += bVx
            by += bVy
        
        if by < 0:
            bVy *= -1
        if bx < 0 or bx+ 20 > 1200:
            bVx *= -1
        if bx >= xpos and by+9 >= ypos and bx <= xpos+100 and by <= ypos+20:
            bVy *= -1
        if by + 20 > 800:
            lives -= 1
            bVy *= -1
            
            
            if lives >= 1:
                pressed_space = False
            else:
                
                running = False


        if xpos < 0:
            xpos = 0
            vx = 0
        elif xpos > 1100:
            xpos = 1100
            vx = 0
        else:
            xpos += vx

        for b in bricks:
            if b.collide(bx, by):
                bVy *= -1
                score += 1
                bricks.remove(b)
                

        # draw:
        screen.fill("#000000")
        for i in range (len(bricks)):
            bricks[i].draw(screen)

        score_text = font.render("Score:", False, (255, 100, 0))
        screen.blit(score_text, (50, 10))
        score_num = font.render(str(score), False, (255, 0, 0))
        screen.blit(score_num, (150, 10))

        lives_text = font.render("Lives:", False, (100, 255, 0))
        screen.blit(lives_text, (50, 720))
        lives_num = font.render(str(lives), False, (99, 242, 160))
        screen.blit(lives_num, (150, 720))

        pygame.draw.rect(screen, (255,255,255), (xpos, ypos, 100, 20), 1)
        pygame.draw.circle(screen, (255,255,255), (bx, by), 10)

        pygame.display.flip()

if __name__ == "__main__":
    main()