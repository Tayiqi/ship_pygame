import pygame

class Ship():
    def __init__(self, screen,ai_settings):
        """初始化玩家飞船并设置初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        #加载飞船图像，并获取其外接矩形
        self.image = pygame.image.load(self.ai_settings.ship_image).convert()
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志 更新飞船位置"""
        if self.moving_right == True and self.moving_left == False:  #左右移动
            if self.rect.centerx <780: 
                self.centerx += self.ai_settings.ship_speedx_factor
        elif self.moving_right == False and self.moving_left == True:
            if self.rect.centerx >20:
                self.centerx -= self.ai_settings.ship_speedx_factor
        self.rect.centerx = self.centerx

        if self.moving_down == True and self.moving_up == False:  #上下移动
            if self.rect.centery <510: 
                self.centery += self.ai_settings.ship_speedy_factor 
        elif self.moving_down == False and self.moving_up == True:
            if self.rect.centery >350:
                self.centery -= self.ai_settings.ship_speedy_factor 
        self.rect.centery = self.centery

    def blitme(self):
        """"在屏幕绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
