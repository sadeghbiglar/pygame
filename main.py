import pygame
pygame.init()
print("running")

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("myGame...")
running=True
blue=(0,0,255)
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        screen.fill((255,255,0))
        back=pygame.image.load('back1.png')
        back=pygame.transform.scale(back,(800,600))
        screen.blit(back,(0,0))
        pygame.draw.line(screen,(0,255,0),(0,520),(1000,520),6)

        """ pygame.draw.circle(screen,blue,(500,400),50)
        font=pygame.font.Font(None,50)
        text=font.render("step1",True,(0,0,0))
        screen.blit(text,(100,100)) """

        player=pygame.image.load('player.png')
        player=pygame.transform.scale(player,(100,125))
        screen.blit(player,(100,390))
        
        pygame.display.flip()
pygame.quit()