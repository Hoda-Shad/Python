import arcade

arcade.open_window(700, 700, 'Complex Loop')
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

center_x = 200
center_y = 300
width = 16
height = 16

for i in range(10):
    for j in range(10):
        if (i + j) % 2 == 0:
            arcade.draw_rectangle_filled(center_x, center_y, width, height, arcade.color.RED, 45)
        else:
            arcade.draw_rectangle_filled(center_x, center_y, width, height, arcade.color.BLUE, 45)
        center_x += 25

    center_x = 200
    center_y += 25

arcade.finish_render()
arcade.run()
