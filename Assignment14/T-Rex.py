# import random
# import arcade
# import time
# from kaktoos import cactus
# from dinosaur import Dinosaur
# from ground import Ground
# from loud import Cloud
#
#
# class Game(arcade.Window):
#     def __init__(self):
#         super().__init__(width=1000, height=500, title="Snake Game")
#         arcade.set_background_color(arcade.color.WHITE)
#
#         self.w = 1000
#         self.h = 700
#         self.gravity = 0.2
#
#         self.t1 = time.time()
#         self.me = Dinosaur()
#         self.cactus_list = arcade.SpriteList()
#         self.ground_list = arcade.SpriteList()
#         self.cloud_list = arcade.SpriteList()
#         self.physic_engin = arcade.PhysicsEnginePlatformer(self.me, self.ground_list, gravity_constant=self.gravity)
#         self.enemy_physic_engin_list = []
#
#         for i in range(0, 1000, 500):
#             r = Ground()
#             self.ground_list.append(r)
#
#         for i in range(100, 1000, random.randint(100,500)):
#             ca = cactus(i, 235)
#             self.ground_list.append(ca)
#
#         for i in range(100,1000, random.randint(100,500)):
#             cloud = Cloud(i,400)
#             self.cloud_list.append(cloud)
#
#
#     def on_draw(self):
#         arcade.start_render()
#         # arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.background_color)
#         self.cloud_list.draw()
#         self.me.draw()
#         self.cactus_list.draw()
#         self.ground_list.draw()
#
#
#
# def on_update(self, delta_time: float):
#     self.me.update_animation()
#     self.physic_engin.update()
#
# def on_key_press(self, symbol: int, modifiers: int):
#
#         if symbol == arcade.key.RIGHT:
#             self.me.change_x = 1 * self.me.speed
#         elif symbol == arcade.key.UP:
#             if self.physic_engin.can_jump():
#                 self.me.change_y = 10
#         elif symbol == arcade.key.DOWN:
#             if self.physic_engin.can_jump():
#                 self.me.change_y = -10
#
# def on_key_release(self, symbol: int, modifiers: int):
#         self.me.change_x = 0
#         self.me.change_y = 0
#
#
# game = Game()
# arcade.run()
import random
import time
import arcade
from kaktoos import Cactus
from bird import Bird
from dinosaur import Dino
from ground import Ground


DEFAULT_FONT_SIZE = 36
class Game(arcade.Window):
    def __init__(self):
        self.w = 800
        self.h = 600
        self.gravity = 0.3
        super().__init__(self.w , self.h ,"T-rex runner")
        self.backeground_night_image = arcade.load_texture("images/background_night.png")
        self.backeground_day_image = arcade.load_texture("images/background_day.png")
        self.gameOver = False
        self.night = True
        self.cactus_list = arcade.SpriteList()
        self.cactus_speed = -4
        self.bird_speed = -5
        self.time_score = time.time()
        self.time_cactus = time.time()
        self.time_bird = time.time()
        self.time_backgroundChange = time.time()
        self.bird_list = arcade.SpriteList()
        self.dino = Dino()
        self.moon = arcade.Sprite('images/moon.png')
        self.moon.center_x = self.w
        self.moon.center_y = random.randint(400, 600)
        self.moon.change_x = -0.5
        self.moon.change_y = 0
        self.star = arcade.Sprite('images/star.png')
        self.star.center_x = self.w
        self.star.center_y = random.randint(250, 750)
        self.star.change_x = -1
        self.star.change_y = 0
        self.cloud = arcade.Sprite('images/cloud_night.png')
        self.cloud.center_x = self.w
        self.cloud.center_y = random.randint(350, 750)
        self.cloud.change_x = -1.5
        self.cloud.change_y = 0
        self.ground_list = arcade.SpriteList()
        for i in range(0, self.w, 64):
            ground = Ground(i ,100)
            self.ground_list.append(ground)
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.dino, self.ground_list, self.gravity)

    def on_draw(self):
        self.time_now = time.time()
        if self.gameOver:
            if self.night:
                arcade.draw_text('YOU Lose', self.w//2-200, self.h//2, arcade.color.WHITE, DEFAULT_FONT_SIZE, width=400, font_name='Kenney Mini Square', align='center')
                # arcade.draw_text('Press Enter for reset game', self.w//2-200, self.h//2-100, arcade.color.WHITE, DEFAULT_FONT_SIZE//2, width=400, font_name='Kenney Mini Square', align='center')
            else:
                arcade.draw_text('YOU Lose', self.w//2-200, self.h//2, arcade.color.BLACK, DEFAULT_FONT_SIZE, width=400, font_name='Kenney Mini Square', align='center')
                # arcade.draw_text('Press Enter for reset game', self.w//2-200, self.h//2-100, arcade.color.BLACK, DEFAULT_FONT_SIZE//2, width=400, font_name='Kenney Mini Square', align='center')
        else:
            arcade.start_render()
            if self.time_now - self.time_backgroundChange > 15:
                self.time_backgroundChange = time.time()
                if self.night:
                    self.night = False
                else:
                    self.night = True
            if self.night:
                arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.backeground_night_image)
            else:
                arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.backeground_day_image)
            for ground in self.ground_list:
                ground.draw()
            for cactus in self.cactus_list:
                cactus.draw()
            for bird in self.bird_list:
                bird.draw()
            self.moon.draw()
            self.cloud.draw()
            self.star.draw()
            self.dino.draw()
            if self.night:
                arcade.draw_text('HI  %s  %s' %(str(self.dino.lastscore).zfill(5), str(self.dino.score).zfill(5)), self.w-220, self.h-30, arcade.color.WHITE, DEFAULT_FONT_SIZE//2, width=400, font_name='Kenney Mini Square', align='left')
            else:
                arcade.draw_text('HI  %s  %s' %(str(self.dino.lastscore).zfill(5), str(self.dino.score).zfill(5)), self.w-220, self.h-30, arcade.color.BLACK, DEFAULT_FONT_SIZE//2, width=400, font_name='Kenney Mini Square', align='left')

    def on_update(self, delta_time: float):
        self.time_now = time.time()
        if not self.gameOver:
            self.dino.score = int(self.time_now-self.time_score)
        if self.dino.score-self.dino.score_speed > 15:
            self.dino.score_speed += 15
            self.cactus_speed -= 0.3
            self.bird_speed -= 0.5
        self.physics_engine.update()
        for bird in self.bird_list:
            bird.update_animation()
        if not self.dino.down:
            self.dino.update_animation()
        else:
            self.dino.manual_walkDown_animation()
            self.dino.down_frame += 1
        for ground in self.ground_list:
            if ground.center_x<0:
                self.ground_list.remove(ground)
                gr = Ground(self.w-64 ,100)
                self.ground_list.append(gr)
        if self.time_now - self.time_cactus > 4 :
            new_cactus = Cactus(self.w, 200, self.cactus_speed)
            self.cactus_list.append(new_cactus)
            self.time_cactus = time.time()
        if self.time_now - self.time_bird > 10 :
            new_bird = Bird(self.w, 200, self.bird_speed)
            self.bird_list.append(new_bird)
            self.time_bird = time.time()
        for cactus in self.cactus_list:
            cactus.update()
            if cactus.center_x < 0:
                self.cactus_list.remove(cactus)
        for bird in self.bird_list:
            bird.update()
            if bird.center_x<0:
                self.bird_list.remove(bird)
        if self.moon.center_x<0 or not self.moon:
            self.moon.center_x = self.w
            self.moon.center_y = random.randint(400, 600)
        if self.star.center_x<300 or not self.star:
            self.star.center_x = self.w
            self.star.center_y = random.randint(250, 750)
        if self.cloud.center_x<50 or not self.cloud:
            self.cloud.center_x = self.w
            self.cloud.center_y = random.randint(350, 750)
        self.moon.update()
        self.star.update()
        self.cloud.update()
        self.dino.set_x()
        for cactus in self.cactus_list:
            if arcade.check_for_collision(self.dino, cactus):
                self.gameOver = True
                arcade.exit()
        for bird in self.bird_list:
            if arcade.check_for_collision(self.dino, bird):
                self.gameOver = True
                arcade.exit()


    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.dino.change_y = 12
                # self.dino.jump_sound()
        elif key == arcade.key.DOWN:
            self.dino.down = True
        elif key == arcade.key.ENTER and self.gameOver:
            self.gameOver = False
            if self.dino.score > self.dino.lastscore:
                self.dino.lastscore = self.dino.score
            self.dino.write_lastscore()
            self.dino.score = 0
            self.time_score = time.time()
            self.cactus_speed = -4
            self.bird_speed = -5


    def on_key_release(self, key, modifiers):
        if key == arcade.key.DOWN:
            self.dino.down = False

game = Game()
arcade.run()
