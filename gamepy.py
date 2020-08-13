import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_states import GameStates

def run_game():
    """游戏主程序"""
    #初始化一个游戏界面
    pygame.init()
    #初始化界面的参数
    ai_settings = Settings()
    screen = pygame.display.set_mode(ai_settings.size)
    pygame.display.set_caption(ai_settings.title)
    bg_color = ai_settings.bg_color
    
    #初始化飞船
    ship = Ship(screen,ai_settings)
    #创建子弹组
    bullets = Group()
    aliens = Group()

    #创建外星人群
    gf.create_aliens_fleet(ai_settings,screen,aliens,ship)

    stats = GameStates(ai_settings)

    #开始游戏主循环
    while True:

        #监控键盘和鼠标
        gf.check_events(ship,ai_settings,screen,bullets)
        
        ship.update()

        gf.update_bullets(bullets,aliens,ai_settings,screen,ship)  
        
        gf.update_aliens(ai_settings,aliens,ship,stats,screen,bullets)

        #刷新界面
        gf.update_screen(ai_settings,screen,ship,bullets,aliens) 
             
run_game()


