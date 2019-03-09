import arcade

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720


arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Tanks")
arcade.set_background_color(arcade.color.LIGHT_KHAKI)

arcade.start_render()


class BlueTank(arcade.Sprite):

    def __init__(self):
        super().__init__("assets/tank_blue.png")
        self.center_x = 100
        self.center_y = SCREEN_HEIGHT / 2
        self.angle = 90
        self.draw()


class GreenTank(arcade.Sprite):

    def __init__(self):
        super().__init__("assets/tank_green.png")
        self.center_x = SCREEN_WIDTH - 100
        self.center_y = SCREEN_HEIGHT / 2
        self.angle = 270
        self.draw()


blue_tank = BlueTank()
green_tank = GreenTank()

arcade.finish_render()
arcade.run()
