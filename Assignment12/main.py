import arcade
import random
import time
import math

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


class SpaceShip(arcade.Sprite):
    def __init__(self):
        super(SpaceShip, self).__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.width = 48
        self.height = 48
        self.score = 0
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = 470
        self.angle = 0
        self.speed = 4
        self.change_angle = 0
        self.bullet_list = []
        self.joon = 3

    def fire(self):
        self.bullet_list.append(Bullet(self))
        audio1 = arcade.load_sound(':resources:sounds/lose2.wav')
        arcade.play_sound(audio1, 1.0, -1, False)

    def rotate(self):
        self.angle += self.change_angle * self.speed

    def move(self):
        if self.change_x > 0:
            self.center_x += self.speed
        elif self.change_x < 0:
            self.center_x -= self.speed


class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.width = 48
        self.height = 48
        self.change_x = 0
        self.center_x = random.randint(self.width, SCREEN_WIDTH - self.width)
        self.center_y = 30
        self.speed = 4
        self.collision_list = []

    def move(self):
        self.center_y += self.speed
        self.speed += 0.001


class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.center_x = host.center_x
        self.center_y = host.center_y
        self.speed = 6
        self.angle = host.angle

    def move(self):
        a = math.radians(self.angle)
        self.center_y -= self.speed * math.sin(a)
        self.center_x += self.speed * math.cos(a)


class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, 'Airplane')
        arcade.set_background_color(arcade.color.BLACK)
        self.background_image = arcade.load_texture(':resources:images/backgrounds/stars.png')
        self.me = SpaceShip()
        self.enemy_list = []
        self.start_time = time.time()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background_image)
        self.me.draw()
        for enemy in self.enemy_list:
            enemy.draw()

        for b in self.me.bullet_list:
            b.draw()
        arcade.draw_text('Score : ' + str(self.me.score), 400, 10, arcade.color.RED, bold=True, font_size=14)
        img = arcade.Sprite('img/R.png', scale=0.01, center_x=2, center_y=20)
        for i in range(self.me.joon):
            img.center_x += 31
            img.draw()
        if self.me.joon <= 0:
            arcade.draw_text('GAME OVER !', 150, 250, arcade.color.RED, bold=True, font_size=18)
            arcade.exit()


    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.me.fire()

        if symbol == arcade.key.UP:
            self.me.change_angle = -1

        elif symbol == arcade.key.DOWN:
            self.me.change_angle = 1

        elif symbol == arcade.key.LEFT:
            self.me.change_x = -1

        elif symbol == arcade.key.RIGHT:
            self.me.change_x = 1

    def on_update(self, delta_time: float):
        self.end_time = time.time()

        if self.end_time - self.start_time > random.randint(4, 10):
            self.enemy_list.append(Enemy())
            self.start_time = time.time()

        self.me.rotate()
        self.me.move()

        for enemy in self.enemy_list:
            enemy.move()
            # print(enemy.speed)
        for b in self.me.bullet_list:
            b.move()

        for enemy in self.enemy_list:

            for b in self.me.bullet_list:
                if arcade.check_for_collision(enemy, b):
                    audio = arcade.load_sound(':resources:sounds/upgrade4.wav')
                    arcade.play_sound(audio, 1.0, -1, False)
                    self.enemy_list.remove(enemy)
                    self.me.bullet_list.remove(b)
                    enemy.remove_from_sprite_lists()
                    b.remove_from_sprite_lists()
                    self.me.score += 1
                    break

        for enemy in self.enemy_list:
            if enemy.center_y >= 500:
                enemy.remove_from_sprite_lists()
                self.enemy_list.remove(enemy)
                self.me.joon -= 1
                # print(self.me.joon)

        if 10 >= self.me.center_x or self.me.center_x >= SCREEN_WIDTH:
            self.me.change_x *= -1


class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()
        self.time_taken = 0

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text("Game Over", 240, 400, arcade.color.WHITE, 54)
        arcade.draw_text("Click to restart", 310, 300, arcade.color.WHITE, 24)
        output_total = f"Total Score: {self.me.score}"
        arcade.draw_text(output_total, 10, 10, arcade.color.WHITE, 14)


game = Game()
arcade.run()
