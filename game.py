#!/usr/bin/env python3
import pygame
import sys
import random
from external import *
pygame.font.init()

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
    # "nec" = new enemy counter
    self.nec = 0
    self.score = 10

    self.bg_surface = pygame.transform.scale(pygame.image.load("assets/bg.png"), (self.WIDTH, self.HEIGHT)).convert()
    self.enemy_surface = pygame.image.load("assets/bad-guy.png").convert_alpha()

    self.mainloop()

  def new_enemy(self):
    if self.nec >= 24:
      x_speed = random.choice([-1,1])
      y_speed = random.randrange(4,8)
      e = Enemy(random.randrange(0, 800), -50, pygame.transform.scale(self.enemy_surface, (random.randrange(40, 130), random.randrange(40, 130))), x_speed, y_speed)
      self.enemies.append(e)
      self.nec = 0
    else:
      self.nec += 1

  def move_enemy(self):
    for enemy in self.enemies:
      enemy.move()
  
  def check_enemy(self):
    for enemy in self.enemies:
      if enemy.x >= 850:
        self.enemies.remove(enemy)
      elif enemy.y >= 850:
        self.enemies.remove(enemy)

  def keys(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and self.player.y >= 10:
      self.player.y -= 7
    if keys[pygame.K_DOWN] and self.player.y <= 780:
      self.player.y += 7
    if keys[pygame.K_LEFT] and self.player.x >= 10:
      self.player.x -= 7
    if keys[pygame.K_RIGHT] and self.player.x <= 780:
      self.player.x += 7

  def collision(self):
    for enemy in self.enemies:
      if self.collide(self.player, enemy):
        self.game_active = False

  @staticmethod
  def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

  def update(self):
    self.new_enemy()
    self.check_enemy()
    self.collision()
    self.move_enemy()
    self.keys()

  def redraw(self):
    for enemy in self.enemies:
      enemy.draw(self.screen)

    self.player.draw(self.screen)

  def play(self):
    self.update()
    self.redraw()

  def endscreen_keys(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
      self.score = 0
      self.enemies.clear()
      self.player.x, self.player.y = 400, 400
      self.game_active = True

  def endscreen(self):
    font = pygame.font.SysFont("comicsans", 40)
    
    dead_label = font.render(f"You died with a score of {self.score}!", 1, (255,255,255))
    restart_label = font.render('To restart the game press the letter "r".', 1, (255,255,255))

    self.screen.blit(dead_label, (self.WIDTH/2 - dead_label.get_width()/2, 330))
    self.screen.blit(restart_label, (self.WIDTH/2 - restart_label.get_width()/2, 380))

    self.endscreen_keys()

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
