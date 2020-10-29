import pygame
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
RED = (255, 0, 0)
YELLOW =(0, 255, 255)

class Bird(pygame.sprite.Sprite):
    def __init__(self, BirdImage):
        super(Bird,self).__init__()
        self.BirdImage = BirdImage
        self._draw_me()
        self.rect = self.image.get_rect()
        self.imagesUp = []
        self.imagesDown = []
        self.imagesUp.append(pygame.image.load("BirdUp1.png").convert_alpha())
        self.imagesUp.append(pygame.image.load("BirdUp2.png").convert_alpha())
        self.imagesDown.append(pygame.image.load("BirdDown.png").convert_alpha())
        self.imagesDown.append(pygame.image.load("BirdDown2.png").convert_alpha())
        self.index = 0
        self.index2 = 0
    def _draw_me(self):
        pass
    def moveUp(self, pixels):
        self.rect.y -= pixels  
        self.index2 += 1
        if self.index2 >= len(self.imagesUp):
            self.index2 = 0
        self.image = self.imagesUp[self.index2]     
    def moveDown(self, pixels):
        self.rect.y += pixels
        self.index += 1
        if self.index >= len(self.imagesDown):
            self.index = 0
        self.image = self.imagesDown[self.index]        
class FlappyBird(Bird):
    def _draw_me(self):
        self.image = pygame.image.load(self.BirdImage).convert_alpha()
    
class pipes(pygame.sprite.Sprite):    
    def __init__(self, width, height, speed):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.width=width
        self.height=height
        self.speed = speed
        self._draw_me()
        self.rect = self.image.get_rect()
    def _draw_me(self):
        pass
    def moveForward(self, speed):
        self.rect.x -= self.speed * speed / 20
    
class pipeBottom(pipes):
    def _draw_me(self):  
        self.image = pygame.image.load("BottomPipe.png").convert_alpha()
    
class pipeTop(pipes):
    def _draw_me(self):
        self.image = pygame.image.load("TopPipe.png").convert_alpha()
    
class floor(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.width=width
        self.height=height
        self._draw_me()
        self.rect = self.image.get_rect()
    def _draw_me(self):
        pass
    
class Bottom(floor):
        def _draw_me(self):
            self.image = pygame.image.load("Floor.png").convert_alpha()

