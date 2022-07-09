import random

import arcade


class Cloud(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("images/cloud.png")
        self.width = 30
        self.height = 10
        self.center_x = x
        self.center_y = y
