import pygame,random
pygame.init()

Clock = pygame.time.Clock()
run = True
screenWidth = 500
screenHeight = 750
score = 0
font1 = pygame.font.SysFont("Times",20)

Background_Image = pygame.image.load("images/background_bird.png")
Background_Image = pygame.transform.scale(Background_Image, (500,750))
Bird = pygame.image.load("images/bird.png")

OtherBird = pygame.image.load("images/bird.png")
OtherBird1 = pygame.image.load("images/bird.png")

Bird_x = 150
Bird_y = 300
Bird_y_Change = 0

OtherBirdWidth = 70
OtherBirdHeight = 70
OtherBird_X_Change = -4
OtherBird_X = 0
OtherBird_Y = random.randint(150,450)

OtherBird1Width = 70
OtherBird1Height = 70
OtherBird1_X_Change = -2
OtherBird1_X = 0
OtherBird1_Y = random.randint(150,450)

screen = pygame.display.set_mode((screenWidth,screenHeight))
#pygame.screen.draw("Score : ",topleft(0,20))

while run:
  #score+=1
  #print(score)
  BirdRect = Bird.get_rect(topleft=(Bird_x,Bird_y))
  OtherBirdRect = OtherBird.get_rect(topleft=(OtherBird_X,OtherBird_Y))
  OtherBird1Rect = OtherBird1.get_rect(topleft=(OtherBird1_X,OtherBird1_Y))
  for event in pygame.event.get():
    keys = pygame.key.get_pressed()
    if(event.type == pygame.QUIT):
      run = False
    if(keys[pygame.K_UP]):
      Bird_y_Change = -6
    if(keys[pygame.K_DOWN]):
      Bird_y_Change = +6

  screen.blit(Background_Image,(0,0))
  scores = font1.render(str(score), True, "black")
  screen.blit(scores, (10,10))
  Bird_y += Bird_y_Change
  if Bird_y > 480:
      Bird_y = 480
      Bird_y_Change = 0
  if Bird_y < 25:
      Bird_y = 25
      Bird_y_Change = 0

  screen.blit(Bird,(Bird_x,Bird_y))

  OtherBird_X -= OtherBird_X_Change
  if OtherBird_X >= 300:
      score += 1
      OtherBird_X = -10
      OtherBird_Y = random.randint(100, 500)

  OtherBird1_X -= OtherBird1_X_Change
  if OtherBird1_X >= 300:
      score += 1
      OtherBird1_X = -10
      OtherBird1_Y = random.randint(100, 500)
      
  if BirdRect.colliderect(OtherBirdRect):
      #score -= 1
      pygame.time.delay(10)
      pygame.draw.rect(screen,"black",BirdRect,4)
      pygame.draw.rect(screen,"yellow",OtherBirdRect,4)

  if BirdRect.colliderect(OtherBird1Rect):
      #score -= 1
      pygame.time.delay(10)
      pygame.draw.rect(screen,"black",BirdRect,4)
      pygame.draw.rect(screen,"green",OtherBird1Rect,4)

  screen.blit(OtherBird,(OtherBird_X,OtherBird_Y))
  screen.blit(OtherBird1,(OtherBird1_X,OtherBird1_Y))
  
  pygame.display.flip()
  Clock.tick(60)
print(score)
