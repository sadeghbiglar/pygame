import pygame
pygame.init()
print("running")

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("myGame...")
running=True
blue=(0,0,255)
x=100
y=390
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        screen.fill((255,255,0))
        back=pygame.image.load('back1.png')
        back=pygame.transform.scale(back,(800,600))
        screen.blit(back,(0,0))
        pygame.draw.line(screen,(200,0,0),(0,517),(1000,517),6)

        """ pygame.draw.circle(screen,blue,(500,400),50)
        font=pygame.font.Font(None,50)
        text=font.render("step1",True,(0,0,0))
        screen.blit(text,(100,100)) """

        player=pygame.image.load('player.png')
        player=pygame.transform.scale(player,(100,125))
        screen.blit(player,(x,y))
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
               y=y-10
            elif event.key==pygame.K_DOWN:
                y=y+10
            elif event.key==pygame.K_LEFT:
                x=x-10
            elif event.key==pygame.K_RIGHT:
                x=x+10
        if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.draw.line(screen,(0,255,0),(0,517),(1000,517),6)



        pygame.display.flip()
pygame.quit()