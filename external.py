import pygame

class Bullet(object):
  def __init__(self):
    pass

class Player(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.image = pygame.image.load("assets/main.png").convert()
    self.mask = pygame.mask.from_surface(self.image)

  def draw(self, window):
    window.blit(self.image, (self.x, self.y))

  def shoot(self):
    pass

class Enemy(object):
  def __init__(self, x, y, image, x_speed, y_speed):
    self.x = x
    self.y = y
    self.image = image
    self.x_speed = x_speed
    self.y_speed = y_speed
    self.mask = pygame.mask.from_surface(self.image)

  def draw(self, window):
    window.blit(self.image, (self.x, self.y))

  def move(self):
    self.x += self.x_speed
    self.y += self.y_speed


