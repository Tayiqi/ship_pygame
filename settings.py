class Settings():
    def __init__(self):

        # screen attribute
        self.size = width,height = (880,550)
        self.bg_color = (245,245,245)
        self.bg_image = 'image/image1.jpg'
        self.title = 'alien invasion'
       
        #ship attribute
        self.ship_image = 'image/ships/ship0.bmp'
        self.ship_speedx_factor = 0.5
        self.ship_speedy_factor = 0.3
        self.ship_limit = 3

        #bullet attribute
        self.bullet_speedy_factor = 0.5
        self.bullet_weight = 4
        self.bullet_height = 8
        self.bullet_color = 60,60,60
        self.bullet_limit = 6

        #alien attribute
        self.alien_image = 'image/ships/ship1.bmp'
        self.alien_speedx_factor = 0.1
        self.alien_speedy_factor = 30
        self.alien_relative_x =1


