import pygame
from sys import exit
from pygame.locals import *
from bullet import Bullet
from alien import Alien
import threading
import time
import random

def check_events(ship,ai_settings,screen,bullets):
    """ 响应案件和鼠标事件"""
    for event in pygame.event.get():

        if event.type == pygame.QUIT:  
                exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_q :
                exit()
            check_keydown_event(event,ship,ai_settings,screen,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)

def check_keydown_event(event,ship,ai_settings,screen,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True

    elif event.key == pygame.K_SPACE:
        #创建一颗子弹 并添加到bullets组中
        fire_bullet(ai_settings,screen,ship,bullets);     

def check_keyup_event(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False 

def update_screen(ai_settings,screen,ship,bullets,aliens):
    """更新图像上的图案，并更新新屏幕"""
    screen.fill(ai_settings.bg_color)
    #绘制所有子弹
    if len(bullets) <= ai_settings.bullet_limit:
        for bullet in bullets.sprites():
            bullet.draw_bullet()  

    ship.blitme()

    aliens.draw(screen)

    pygame.display.flip()

def fire_bullet(ai_settings,screen,ship,bullets):
    """fire bullet"""
    new_bullet = Bullet(ai_settings,screen,ship)
    bullets.add(new_bullet)   

def update_bullets(bullets,aliens,ai_settings,screen,ship):
    """update bullet position"""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet) 

    #检测是否与外星人碰撞
    check_bullets_aliens_collision(bullets,aliens,ai_settings,screen,ship)

def check_bullets_aliens_collision(bullets,aliens,ai_settings,screen,ship):
    """check_bullets_aliens_collision"""
    collision = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if len(aliens) == 0:
        bullets.empty()
        create_aliens_fleet(ai_settings,screen,aliens,ship)

def create_aliens_fleet(ai_settings,screen,aliens,ship):
    """create aliens fleet"""
    alien = Alien(ai_settings,screen)
    #x轴能容纳的外星人数
    alien_width = alien.rect.width
    aliens_number_x = int((ai_settings.size[0] - 2*alien_width)/(alien_width *2))

    #y轴能容纳的外星人数
    alien_height = alien.rect.height
    alien_number_y = int((ai_settings.size[1] - 10*alien_height - ship.rect.height)/(alien_height *2))

    #创建一群外星人
    for row_num in range(alien_number_y):
        for alien_num in range(aliens_number_x):
            alien = Alien(ai_settings,screen)
            alien.x = alien_width + alien_width*alien_num*2 + random.uniform(-20,20)
            alien.rect.x = alien.x
            alien.y = alien_height +alien_height*row_num*3 + random.uniform(-5,5)
            alien.rect.y = alien.y
            aliens.add(alien)

def update_aliens(ai_settings,aliens,ship,stats,screen,bullets):
    """更新外星人群位置"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)

    

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    stats.ship_left -=1

    aliens.empty()
    bullets.empty()

    create_aliens_fleet(ai_settings,screen,aliens,ship)
    ship.center_ship()

    time.sleep(1)


    
    
def check_fleet_direction(ai_settings,aliens):
    """将外星人统一下移一行，转变运动方向"""
    for alien in aliens:
        alien.y += ai_settings.alien_speedy_factor
        alien.rect.y = alien.y
    ai_settings.alien_relative_x *= -1

def check_fleet_edges(ai_settings,aliens):
    """检测到有外星人移动到x边界时，下移并转变方向"""
    for alien in aliens.sprites():
        if alien.check_edges():
            check_fleet_direction(ai_settings,aliens)
            break
