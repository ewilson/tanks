import arcade

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720


arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Tanks")
arcade.set_background_color(arcade.color.LIGHT_KHAKI)

arcade.start_render()
arcade.finish_render()
arcade.run()
