import arcade

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720


arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Tanks")
arcade.set_background_color(arcade.color.LIGHT_KHAKI)

arcade.start_render()

blue_tank = arcade.Sprite("assets/tank_blue.png")
blue_tank.center_x = 100
blue_tank.center_y = SCREEN_HEIGHT / 2
blue_tank.angle = 90
blue_tank.draw()

green_tank = arcade.Sprite("assets/tank_green.png")
green_tank.center_x = SCREEN_WIDTH - 100
green_tank.center_y = SCREEN_HEIGHT / 2
green_tank.angle = 270
green_tank.draw()

arcade.finish_render()
arcade.run()
