import arcade

import motion

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720
TANK_SPEED = 3


class Tank(arcade.Sprite):

    def __init__(self, sprite_file):
        super().__init__(sprite_file)

    def on_update(self):
        self.angle += self.d_theta
        self._move()

    def _move(self):
        delta_x, delta_y = motion.move(self.speed, self.angle)
        self.center_x += delta_x
        self.center_y += delta_y


class BlueTank(Tank):

    def __init__(self):
        super().__init__("assets/tank_blue.png")
        self.center_x = 100
        self.center_y = SCREEN_HEIGHT / 2
        self.angle = 90
        self.draw()
        self.d_theta = 0
        self.speed = 0

    def on_key_press(self, key):
        if key == arcade.key.A:
            self.d_theta += 4
        if key == arcade.key.D:
            self.d_theta -= 4
        if key == arcade.key.W:
            self.speed += TANK_SPEED

    def on_key_release(self, key):
        if key == arcade.key.A:
            self.d_theta -= 4
        if key == arcade.key.D:
            self.d_theta += 4
        if key == arcade.key.W:
            self.speed -= TANK_SPEED


class GreenTank(Tank):

    def __init__(self):
        super().__init__("assets/tank_green.png")
        self.center_x = SCREEN_WIDTH - 100
        self.center_y = SCREEN_HEIGHT / 2
        self.angle = 270
        self.d_theta = 0
        self.speed = 0
        self.draw()

    def on_key_press(self, key):
        if key == arcade.key.LEFT:
            self.d_theta += 4
        if key == arcade.key.RIGHT:
            self.d_theta -= 4
        if key == arcade.key.UP:
            self.speed += TANK_SPEED

    def on_key_release(self, key):
        if key == arcade.key.LEFT:
            self.d_theta -= 4
        if key == arcade.key.RIGHT:
            self.d_theta += 4
        if key == arcade.key.UP:
            self.speed -= TANK_SPEED


class TanksWindow(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Tanks")
        arcade.set_background_color(arcade.color.LIGHT_KHAKI)
        arcade.start_render()
        self.blue_tank = BlueTank()
        self.green_tank = GreenTank()

    def on_draw(self):
        arcade.start_render()
        self.blue_tank.draw()
        self.green_tank.draw()

    def on_key_press(self, key, modifiers):
        self.blue_tank.on_key_press(key)
        self.green_tank.on_key_press(key)

    def on_key_release(self, key, modifiers):
        self.blue_tank.on_key_release(key)
        self.green_tank.on_key_release(key)

    def on_update(self, delta_time: float):
        self.blue_tank.on_update()
        self.green_tank.on_update()


TanksWindow()
arcade.run()
