import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Bullets from the spaceship """
    def __init__(self,ai_settings,screen,ship):
        """ create bullet object in location of the spaceship"""
        super().__init__()
        self.screen = screen
        #在左上角绘制子弹矩形 并将其放置飞船上中位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_weight,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #储存当前子弹y轴位置
        self.y = float(self.rect.y)
        #设置颜色
        self.color = ai_settings.bullet_color
        #设置速度
        self.speed_factor = ai_settings.bullet_speedy_factor

    def update(self):
        """子弹向上飞出"""
        #向上移动子弹位置
        self.y -= self.speed_factor
        #将子弹y坐标赋予子弹对象
        self.rect.y = self.y

    def draw_bullet(self):
        """屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)
