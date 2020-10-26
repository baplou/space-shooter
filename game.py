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
    self.nec = 0
    self.score = 0
    self.shoot_counter = 0
    self.score_counter = 0
    self.high_score = 0

    self.bg_surface = pygame.transform.scale(pygame.image.load("assets/bg.png"), (self.WIDTH, self.HEIGHT)).convert()
    self.enemy_surface = pygame.image.load("assets/bad-guy.png").convert_alpha()

    self.mainloop()

  def highscore(self):
    if self.score >= self.high_score:
      self.high_score = self.score

  def new_enemy(self):
    if self.nec >= 24:
      x_speed = random.choice([-1,1])
      y_speed = random.randrange(4,8)
      e = Enemy(random.randrange(0, 800), -50, pygame.transform.scale(self.enemy_surface, (random.randrange(40, 130), random.randrange(40, 130))), x_speed, y_speed)
      self.enemies.append(e)
      self.nec = 0
    else:
      self.nec += 1

  def update_score(self):
    if self.score_counter >= 120:
      self.score += 1
      self.score_counter = 0
    else:
      self.score_counter += 1

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
      self.player.y -= 8
    elif keys[pygame.K_DOWN] and self.player.y <= 780:
      self.player.y += 8
    elif keys[pygame.K_LEFT] and self.player.x >= 10:
      self.player.x -= 8
    elif keys[pygame.K_RIGHT] and self.player.x <= 780:
      self.player.x += 8

    if keys[pygame.K_SPACE] and self.shoot_counter >= 40:
      self.player.shoot()
      self.shoot_counter = 0
    else:
      self.shoot_counter += 1

  def check_bullets(self):
    for bullet in self.player.bullets:
      if bullet.y >= 850:
        self.player.bullets.remove(bullet)

  def move_bullets(self):
    for bullet in self.player.bullets:
      bullet.move()

  def update_player(self):
    self.check_bullets()
    self.move_bullets()

  def collision(self):
    for enemy in self.enemies:
      if self.collide(self.player, enemy):
        self.game_active = False
      for bullet in self.player.bullets:
        if self.collide(bullet, enemy):
          self.enemies.remove(enemy)
          self.player.bullets.remove(bullet)
          self.score += 20

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
    self.update_player()
    self.update_score()
    self.keys()
    self.highscore()

  def redraw(self):
    for enemy in self.enemies:
      enemy.draw(self.screen)

    for bullet in self.player.bullets:
      bullet.draw(self.screen)

    self.player.draw(self.screen)
    
    font = pygame.font.SysFont("comicsans", 40)
    score_label = font.render(f"Score: {self.score}", 1, (255,255,255))
    highscore_label = font.render(f"High Score: {self.high_score}", 1, (255,255,255))
    self.screen.blit(score_label, (5,3))
    self.screen.blit(highscore_label, ((800 - highscore_label.get_width()) - 3, 3))

  def play(self):
    self.update()
    self.redraw()

  def endscreen_keys(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
      self.score = 0
      self.enemies.clear()
      self.player.x, self.player.y = 400, 400
      self.player.bullets.clear()
      self.game_active = True

  def endscreen(self):
    font = pygame.font.SysFont("comicsans", 40)
    
    dead_label = font.render(f"You died with a score of {self.score} and with a highscore of {self.high_score}!", 1, (255,255,255))
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
