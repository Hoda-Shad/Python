import arcade
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height = 16
        self.color_1 = arcade.color.GREEN
        self.color_2 = arcade.color.DARK_GREEN
        # direction of move
        self.change_x = 0
        self.change_y = 0
        self.score = 0
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2
        self.speed = 3
        self.body = []

    def eat(self, mode):
        if mode == 1:
            self.score += 1
        elif mode == 2:
            self.score -= 2
        elif mode == 3:
            self.score -= 1

    def move(self, appleX, appleY):
        # add old position of head.Because the position of current head will be the posiotion of its rest body
        self.body.append((self.center_x, self.center_y))
        if len(self.body) > self.score:
            self.body.pop(0)
        # if self.change_x > 0:
        #     self.center_x += self.speed
        # elif self.change_x < 0:
        #     self.center_x -= self.speed
        # elif self.change_y > 0:
        #     self.center_y += self.speed
        # elif self.change_y < 0:
        #     self.center_y -= self.speed
        #
        # if self.center_x > appleX:
        #     self.change_x -= 1
        #     self.center_x -= self.speed
        # elif self.center_x < appleX:
        #     self.change_x += 1
        #     self.center_x += self.speed
        # elif self.center_x == appleX:
        #     self.change_x = 0
        #     if self.center_y > appleY:
        #         self.change_y -= 1
        #         self.center_y -= self.speed
        #     elif self.center_y < appleY:
        #         self.change_y += 1
        #         self.center_y += self.speed
        #     elif self.center_y == appleY:
        #         self.change_y = 0

        if self.center_x > appleX:
            self.change_x = -1
        if self.center_x < appleX:
            self.change_x = 1
        if self.center_x == appleX:
            self.change_x = 0
        if self.center_y > appleY:
            self.change_y = -1
        if self.center_y < appleY:
            self.change_y = 1
        if self.center_y == appleY:
            self.change_y = 0

        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y


    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color_1)
        for i in range(len(self.body)):
            if i % 2 == 0:
                arcade.draw_rectangle_filled(self.body[i][0], self.body[i][1], self.width, self.height, self.color_1)
            else:
                arcade.draw_rectangle_filled(self.body[i][0], self.body[i][1], self.width, self.height, self.color_2)


class Pear(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height = 16
        # self.center_x = random.randint(20, SCREEN_WIDTH-20)
        # self.center_y = random.randint(20, SCREEN_HEIGHT-20)
        # self.color = arcade.color.GREEN_YELLOW
        # self.r = 6
        self.mySprite3 = arcade.Sprite('img/pear.png', scale=0.11)
        self.mySprite3.center_x = random.randint(10, SCREEN_WIDTH - 10)
        self.mySprite3.center_y = random.randint(10, SCREEN_HEIGHT - 10)

    def draw(self):
        self.mySprite3.draw()
        # arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color)


class Lol(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height = 16
        # self.center_x = random.randint(20, SCREEN_WIDTH-20)
        # self.center_y = random.randint(20, SCREEN_HEIGHT-20)
        self.color = arcade.color.BROWN
        # self.r = 6
        self.mySprite2 = arcade.Sprite('img/poop.png', scale=0.05)
        self.mySprite2.center_x = random.randint(10, SCREEN_WIDTH - 10)
        self.mySprite2.center_y = random.randint(10, SCREEN_HEIGHT - 10)

    def draw(self):
        self.mySprite2.draw()
        # arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color)


class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height = 16
        # self.color = arcade.color.RED
        # self.r = 8
        # self.center_x = random.randint(20, SCREEN_WIDTH-20)
        # self.center_y = random.randint(20, SCREEN_HEIGHT-20)
        self.mySprite1 = arcade.Sprite('img/apple.png', scale=0.025)
        self.mySprite1.center_x = random.randint(10, SCREEN_WIDTH - 10)
        self.mySprite1.center_y = random.randint(10, SCREEN_HEIGHT - 10)

    def draw(self):
        # arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color)
        self.mySprite1.draw()


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="Snake Game")
        arcade.set_background_color(arcade.color.SAND)
        self.snake = Snake()
        self.apple = Apple()
        self.pear = Pear()
        self.lol = Lol()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text('Score : ' + str(self.snake.score),
                         2,
                         480,
                         arcade.color.BLACK, 14, 1000, 'left')
        self.snake.draw()
        self.apple.draw()
        self.pear.draw()
        self.lol.draw()

        if self.snake.score < 0 or self.snake.center_x <= 0 or self.snake.center_x >= SCREEN_WIDTH or self.snake.center_y <= 0 or self.snake.center_y >= SCREEN_WIDTH:
            arcade.draw_text('GAME OVER !', 150, 250, arcade.color.RED, bold=True, font_size=18)
            arcade.exit()

    # تمام منطق بازی در این قسمت پیاده ساز ی می شود (تمام اتفاقات بازی )
    def on_update(self, delta_time: float):
        self.snake.move(self.apple.mySprite1.center_x , self.apple.mySprite1.center_y)
        if arcade.check_for_collision(self.snake, self.apple.mySprite1):
            mode = 1
            self.apple = Apple()
            self.snake.eat(mode)

        if arcade.check_for_collision(self.snake, self.lol.mySprite2):
            mode = 2
            self.lol = Lol()
            self.snake.eat(mode)

        if arcade.check_for_collision(self.pear.mySprite3, self.snake):
            mode = 3
            self.pear = Pear()
            self.snake.eat(mode)

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0
        elif key == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif key == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif key == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1


mygame = Game()
arcade.run()
