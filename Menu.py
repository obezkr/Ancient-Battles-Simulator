# здесь подключаются модули
import pygame
 
# здесь определяются константы, классы и функции
FPS = 30
BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
tplayers=False
ForTwoPlayers=0    

# здесь происходит инициация, создание объектов и др.
pygame.init()
pygame.mixer.music.load('music/Menu Theme.ogg')
pygame.mixer.music.play()
mainpic = pygame.image.load('images/mainpic.jpeg')
mpic = mainpic.get_rect(bottomleft=(-250, 500))
titlepic = pygame.image.load('images/titlepic.png')
titlepic.set_colorkey(WHITE)
titp = titlepic.get_rect(bottomleft=(3, 118))
onecomputer = pygame.image.load('images/onecomputer.png')
onecomputer.set_colorkey(BLACK)
onecmp = onecomputer.get_rect(bottomleft=(65, 295))
localnetwork = pygame.image.load('images/localnetwork.png')
localnetwork.set_colorkey(BLACK)
lnet = localnetwork.get_rect(bottomleft=(225, 290))
campaign = pygame.image.load('images/campaign.png')
camp = campaign.get_rect(bottomleft=(120, 200))
twoplayers = pygame.image.load('images/twoplayers.png')
twop = twoplayers.get_rect(bottomleft=(120, 310))
exitt = pygame.image.load('images/exit.png')
ex = exitt.get_rect(bottomleft=(120, 420))
sc = pygame.display.set_mode((400, 500))
clock = pygame.time.Clock()
 
# если надо до цикла отобразить объекты на экране
sc.blit(mainpic, mpic)
sc.blit(titlepic, titp)
sc.blit(campaign, camp)
sc.blit(twoplayers, twop)
sc.blit(exitt, ex)
pygame.display.update()
f1 = pygame.font.Font(None, 32)
text1 = f1.render('One Computer', 1, WHITE)
text2 = f1.render('Local', 1, WHITE)
text3 = f1.render('Network', 1, WHITE)
text4 = f1.render('Server', 1, WHITE)
text5 = f1.render('Connect to:', 1, WHITE)
# главный цикл
while True:

    # задержка
    clock.tick(FPS)
 
    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
                x=i.pos[0]
                y=i.pos[1]
                if tplayers==True:
                    if ForTwoPlayers=='Local Network':
                        if 20<x<200 and 140<y<330:
                            pygame.quit()
                            import AncientBattlesSimulator_007server
                        if 200<x<380 and 140<y<330:
                            pygame.quit()
                            import AncientBattlesSimulator_007client
                    else:
                        if 20<x<200 and 140<y<330:
                            ForTwoPlayers='One Computer'
                        if 200<x<380 and 140<y<330:
                            ForTwoPlayers='Local Network'
                    if 120<x<285 and 350<y<420:
                        exit()
                    if ForTwoPlayers=='One Computer':
                        pygame.quit()
                        import AncientBattlesSimulator_007
                    if ForTwoPlayers=='Local Network':
                        sc.blit(mainpic, mpic)
                        sc.blit(titlepic, titp)
                        sc.blit(exitt, ex)
                        pygame.draw.rect(sc, BLACK, (20, 140, 360, 190))
                        pygame.draw.line(sc, WHITE, [200, 140], [200, 330], 3)
                        sc.blit(text4, (70, 200))
                        sc.blit(text5, (235, 200))
                        pygame.display.update()
                    
                if tplayers==False:
                    if 120<x<285 and 130<y<200:
                        pygame.quit()
                        import AncientBattlesSimulator_008campaign
                    if 120<x<285 and 240<y<310:
                        tplayers=True
                    if 120<x<285 and 350<y<420:
                        exit()
                if ForTwoPlayers!='Local Network':
                    if tplayers==True:
                        sc.blit(mainpic, mpic)
                        sc.blit(titlepic, titp)
                        sc.blit(exitt, ex)
                        pygame.draw.rect(sc, BLACK, (20, 140, 360, 190))
                        pygame.draw.line(sc, WHITE, [200, 140], [200, 330], 3)
                        sc.blit(onecomputer, onecmp)
                        sc.blit(localnetwork, lnet)
                        sc.blit(text1, (36, 160))
                        sc.blit(text2, (265, 155))
                        sc.blit(text3, (250, 180))
                        pygame.display.update()
                
 
    # --------
    # изменение объектов и многое др.
    # --------
    
    u=pygame.mixer.music.get_busy()
    if u==False:
        pygame.mixer.music.load('music/Menu Theme.ogg')
        pygame.mixer.music.play()
    
    
    # обновление экрана
    pygame.display.update()
