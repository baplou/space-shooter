#!/usr/bin/env python3
import pygame
import sys

class Game(object):
  def __init__(self):
    self.WIDTH = 800
    self.HEIGHT = 800
    self.FPS = 60
    self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
    self.clock = pygame.time.Clock()
    
    self.game_active = True
    self.mainloop()

  def play(self):
    pass

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

      self.main()

      pygame.display.update()
      self.clock.tick(self.FPS)

if __name__ == "__main__":
  g = Game()
