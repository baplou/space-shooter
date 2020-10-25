#!/usr/bin/env python3
import pygame
import sys
import random

class Player(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.image = pygame.image.load("assets/main.png").convert()

  def draw(self, window):
    window.blit(self.image, (self.x, self.y))

class Enemy(object):
  def __init__(self, x, y, image):
    self.x = x
    self.y = y
    self.image = image

  def draw(self, window):
    window.blit(self.image, (self.x, self.y))

class Game(object):
  def __init__(self):
    self.WIDTH = 800
    self.HEIGHT = 800
    self.FPS = 60
    self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
    self.clock = pygame.time.Clock()
    
    self.game_active = True
    self.enemies = []
    self.player = Player(400, 500)
    self.nec = 0

    self.bg_surface = pygame.transform.scale(pygame.image.load("assets/bg.png"), (self.WIDTH, self.HEIGHT)).convert()
    self.enemy_surface = pygame.image.load("assets/bad-guy.png").convert()

    self.mainloop()

  def new_enemy(self):
    if self.nec >= 30:
      e = Enemy(random.randrange(-200, -50), random.randrange(-200, -50), pygame.transform.scale(self.enemy_surface, (random.randrange(100, 200), random.randrange(100, 200))))
      self.enemies.append(e)
      self.nec = 0
    else:
      self.nec += 1
  
  def move_enemy(self):
    for enemy in self.enemies:
      enemy.x += 10
      enemy.y += 10

  def check_enemy(self):
    for enemy in self.enemies:
      if enemy.x >= 850:
        pass
      elif enemy.x <= -50:
        pass
      elif enemy.y >= 850:
        pass
      elif enemy.y <= -50:
        pass

  def update(self):
    self.check_enemy()
    self.new_enemy()
    self.move_enemy()

  def redraw(self):
    for enemy in self.enemies:
      enemy.draw(self.screen)

    self.player.draw(self.screen)

  def play(self):
    self.update()
    self.redraw()

  def endscreen(self):
    pass

  def main(self):
    if self.game_active:
      self.play()
    else:
      self.endscreen()

  def mainloop(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

      self.screen.blit(self.bg_surface, (0,0))
      self.main()

      pygame.display.update()
      self.clock.tick(self.FPS)

if __name__ == "__main__":
  g = Game()
