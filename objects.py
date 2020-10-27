import pygame as pg
import numpy as np
from time import time
from settings import *


class Square(pg.sprite.Sprite):
    # test object
    def __init__(self, size):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface([size, size])
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

    def update(self, screen, pos=(0, 0)):
        self.image.fill(blue)
        screen.blit(self.image, self.rect)


class Button(pg.sprite.Sprite):
    def __init__(self, text, xpos, ypos, ipadx=0, ipady=0, function=None, color=(0, 48, 78), hcolor=(41, 217, 230), fcolor=(0, 0, 255)):
        pg.sprite.Sprite.__init__(self)

        self.font = pg.font.Font('freesansbold.ttf', 20)
        self.text_image = self.font.render(text, True, white, None)
        self.drop_shadow_image = self.font.render(text, True, black, None)

        self.image = pg.Surface((self.text_image.get_width() + 2*ipadx, self.text_image.get_height() + 2*ipady))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.text_rect = self.text_image.get_rect()
        self.text_rect.center = self.rect.center
        self.drop_shadow_rect = self.drop_shadow_image.get_rect()
        self.drop_shadow_rect.x = self.text_rect.x + 2
        self.drop_shadow_rect.y = self.text_rect.y + 2

        self.color = color
        self.deselected_color = color
        self.highlight_color = hcolor
        self.flash_color = fcolor

        self.function = function
        self.time_interacted = time() - button_flash_duration
        self.highlight = False

    def hover(self, pos):
        x, y = self.rect.x, self.rect.y
        if x < pos[0] < x + self.image.get_width() and y < pos[1] < y + self.image.get_height():
            return True
        else:
            return False

    def get_height(self):
        return self.image.get_height()

    def get_width(self):
        return self.image.get_width()

    def set_function(self, function):
        self.function = function

    def click(self):
        self.function()
        self.flash()

    def flash(self):
        self.time_interacted = time()

    def update(self, screen, pos):
        self.color = self.deselected_color
        if time() - button_flash_duration < self.time_interacted:
            self.color = self.flash_color
        elif self.hover(pos):
            self.color = self.highlight_color
        self.image.fill(self.color)
        screen.blit(self.image, self.rect)
        screen.blit(self.drop_shadow_image, self.drop_shadow_rect)
        screen.blit(self.text_image, self.text_rect)


class Label:
    def __init__(self, text, font, font_size, center, text_color, background=None, ipadx=0, ipady=0):
        self.font = pg.font.Font(font, font_size)
        self.pos = center
        self.text = text
        self.text_color = text_color
        self.text_image = self.font.render(self.text, True, self.text_color, None)
        self.text_rect = self.text_image.get_rect()
        self.text_rect.center = self.pos
        self.drop_shadow_image = self.font.render(self.text, True, black, None)
        self.drop_shadow_rect = self.drop_shadow_image.get_rect()
        self.drop_shadow_rect.x = self.text_rect.x + 2
        self.drop_shadow_rect.y = self.text_rect.y + 2

        self.image = pg.Surface((self.text_image.get_width() + ipadx, self.text_image.get_height() + ipady))
        self.rect = self.image.get_rect()
        self.rect.center = center

        self.background = background

    def set_text(self, text):
        self.text = text
        self.text_image = self.font.render(self.text, True, self.text_color, None)
        self.text_rect = self.text_image.get_rect()
        self.text_rect.center = self.pos
        self.drop_shadow_image = self.font.render(self.text, True, black, None)
        self.drop_shadow_rect = self.drop_shadow_image.get_rect()
        self.drop_shadow_rect.x = self.text_rect.x + 2
        self.drop_shadow_rect.y = self.text_rect.y + 2

    def draw(self, screen):
        if self.background:
            self.image.fill(self.background)
        screen.blit(self.image, self.rect)
        screen.blit(self.drop_shadow_image, self.drop_shadow_rect)
        screen.blit(self.text_image, self.text_rect)


class SineWave(pg.sprite.Sprite):
    def __init__(self, y_position, color):
        pg.sprite.Sprite.__init__(self)
        self.x_min = wave_x0
        self.x_max = sidebar_x0
        self.width = self.x_max - self.x_min

        self.y_anchor = y_position
        self.color = color

        self.amplitude = wave_default_amplitude

        self.t = time()
        self.wave_number = wave_default_wave_number
        self.frequency = wave_default_frequency
        self.directional_factor = -1

        self.x_positions = np.array(range(self.x_min, self.x_max))  # positions on screen
        self.x_values = np.linspace(0, 2*np.pi, len(self.x_positions))  # positions in space from 0 to 2pi
        self.y_values = np.zeros(len(self.x_positions))     # y values evaluated in update method

    def change_direction(self):
        self.directional_factor = -1 if self.directional_factor > 0 else 1

    def increase_wave_number(self):
        if round(self.wave_number, 1) < wave_max_wave_number:
            self.wave_number += .2

    def decrease_wave_number(self):
        if round(self.wave_number, 1) > wave_min_wave_number:
            self.wave_number -= .2

    def increase_frequency(self):
        if round(self.frequency, 1) < wave_max_frequency:
            self.frequency += .5

    def decrease_frequency(self):
        if round(self.frequency, 1) > wave_min_frequency:
            self.frequency -= .5

    def increase_amplitude(self):
        if self.amplitude < wave_max_amplitude:
            self.amplitude += 1

    def decrease_amplitude(self):
        if self.amplitude > wave_min_amplitude:
            self.amplitude -= 1

    def get_y_values(self):
        return self.y_values

    def get_x_positions(self):
        return self.x_positions

    def get_amplitude(self):
        return round(self.amplitude, 2)

    def get_wave_number(self):
        return round(self.wave_number, 2)

    def get_frequency(self):
        return round(self.frequency, 2)

    def get_direction_sign_string(self):
        return '+' if self.directional_factor > 0 else '-'

    def sum_waves(self, wave):
        return self.y_values + wave.get_y_values() + wave_sum_anchor

    def update(self, screen, pos):
        self.t = time()
        self.y_values = self.amplitude * np.sin(self.wave_number * self.x_values + self.directional_factor * self.frequency * self.t) + self.amplitude*1.4
        if self.amplitude:
            for value, position in zip(self.y_values, self.x_positions):
                screen.set_at((position, int(value + self.y_anchor)), self.color)
                for i in range(5):  # make the line thick
                    screen.set_at((position, int(value + self.y_anchor) + i), self.color)
                    screen.set_at((position, int(value + self.y_anchor) - i), self.color)


def sum_of_waves(screen, x_positions, y_values):
    for x, y in zip(x_positions, y_values):
        screen.set_at((x, int(y)), sum_color)
        for i in range(7):  # make the line thicc
            screen.set_at((x, int(y) + i), sum_color)
            screen.set_at((x, int(y) - i), sum_color)
