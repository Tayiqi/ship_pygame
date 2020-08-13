import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,ai_settings, screen):
        """初始化外星人并设置初始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #加载外星人图像，并获取其外接矩形
        self.image = pygame.image.load(self.ai_settings.alien_image).convert()
        self.rect = self.image.get_rect()

        #将每个外星人初始位置都在左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """绘制外星人"""
        self.screen.blit(self.image,self.rect);

    def update(self):
        """更新外星人位置"""
        self.x += self.ai_settings.alien_speedx_factor*self.ai_settings.alien_relative_x
        self.rect.x = self.x   #更新外星人x位置

    def check_edges(self):
        """检测是否到达边缘"""
        screen_rect = self.screen.get_rect()
        if self.rect.left <=0:
            #print(self.rect.left)
            return True
        elif self.rect.right >=screen_rect.right:
            #print(self.rect.right)
              return True
        else:
            return False
