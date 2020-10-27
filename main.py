import pygame as pg
import objects as obj
from settings import *

pg.init()

screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption(screen_caption)
pg.display.set_icon(pg.image.load('sine_wave.png'))

# creating two initial waves and getting their x_positions for later
all_sprites = pg.sprite.Group()
wave1 = obj.SineWave(wave1_y_anchor, wave1_color)
all_sprites.add(wave1)
wave2 = obj.SineWave(wave2_y_anchor, wave2_color)
all_sprites.add(wave2)
x_positions = wave1.get_x_positions()

# buttons
buttons = pg.sprite.Group()
change_direction1 = obj.Button('', sidebar_x1, direction_button_y1, 30, 0, wave1.change_direction)
all_sprites.add(change_direction1)
buttons.add(change_direction1)
change_direction2 = obj.Button('', sidebar_x1, direction_button_y2, 30, 0, wave2.change_direction)
all_sprites.add(change_direction2)
buttons.add(change_direction2)
decrease_frequency1 = obj.Button('-', sidebar_x1, frequency_button_y1, 10, 5, wave1.decrease_frequency)
all_sprites.add(decrease_frequency1)
buttons.add(decrease_frequency1)
decrease_frequency2 = obj.Button('-', sidebar_x1, frequency_button_y2, 10, 5, wave2.decrease_frequency)
all_sprites.add(decrease_frequency2)
buttons.add(decrease_frequency2)
increase_frequency1 = obj.Button('+', sidebar_x1 + decrease_frequency1.get_width() + 5, frequency_button_y1, 10, 5, wave1.increase_frequency)
all_sprites.add(increase_frequency1)
buttons.add(increase_frequency1)
increase_frequency2 = obj.Button('+', sidebar_x1 + decrease_frequency2.get_width() + 5, frequency_button_y2, 10, 5, wave2.increase_frequency)
all_sprites.add(increase_frequency2)
buttons.add(increase_frequency2)
decrease_wave_number1 = obj.Button('-', sidebar_x1, wave_number_button_y1, 10, 5, wave1.decrease_wave_number)
all_sprites.add(decrease_wave_number1)
buttons.add(decrease_wave_number1)
decrease_wave_number2 = obj.Button('-', sidebar_x1, wave_number_button_y2, 10, 5, wave2.decrease_wave_number)
all_sprites.add(decrease_wave_number2)
buttons.add(decrease_wave_number2)
increase_wave_number1 = obj.Button('+', sidebar_x1 + decrease_wave_number1.get_width() + 5, wave_number_button_y1, 10, 5, wave1.increase_wave_number)
all_sprites.add(increase_wave_number1)
buttons.add(increase_wave_number1)
increase_wave_number2 = obj.Button('+', sidebar_x1 + decrease_wave_number2.get_width() + 5, wave_number_button_y2, 10, 5, wave2.increase_wave_number)
all_sprites.add(increase_wave_number2)
buttons.add(increase_wave_number2)
decrease_amplitude1 = obj.Button('-', sidebar_x1, amplitude_button_y1, 10, 5, wave1.decrease_amplitude)
buttons.add(decrease_amplitude1)
all_sprites.add(decrease_amplitude1)
increase_amplitude1 = obj.Button('+', sidebar_x1 + decrease_amplitude1.get_width() + 5, amplitude_button_y1, 10, 5, wave1.increase_amplitude)
buttons.add(increase_amplitude1)
all_sprites.add(increase_amplitude1)
decrease_amplitude2 = obj.Button('-', sidebar_x1, amplitude_button_y2, 10, 5, wave2.decrease_amplitude)
buttons.add(decrease_amplitude2)
all_sprites.add(decrease_amplitude2)
increase_amplitude2 = obj.Button('+', sidebar_x1 + decrease_amplitude2.get_width() + 5, amplitude_button_y2, 10, 5, wave2.increase_amplitude)
buttons.add(increase_amplitude2)
all_sprites.add(increase_amplitude2)

# Labels
l1 = obj.Label('Wave 1', 'freesansbold.ttf', 20,
               [sidebar_center_x, 30], red)
l2 = obj.Label('Direction', 'freesansbold.ttf', 16,
               [label_center_x, direction_button_y1 + change_direction1.get_height()/2], white)
l3 = obj.Label('Frequency', 'freesansbold.ttf', 16,
               [label_center_x, frequency_button_y1 + increase_frequency1.get_height()/2], white)
l4 = obj.Label('Wave Number', 'freesansbold.ttf', 16,
               [label_center_x, wave_number_button_y1 + increase_wave_number1.get_height()/2], white)
l5 = obj.Label('Amplitude', 'freesansbold.ttf', 16,
               [label_center_x, amplitude_button_y1 + increase_amplitude1.get_height()/2], white)
l6 = obj.Label('Wave 2', 'freesansbold.ttf', 20,
               [sidebar_center_x, 230], blue)
l7 = obj.Label('Direction', 'freesansbold.ttf', 16,
               [label_center_x, direction_button_y2 + change_direction2.get_height()/2], white)
l8 = obj.Label('Frequency', 'freesansbold.ttf', 16,
               [label_center_x, frequency_button_y2 + increase_frequency2.get_height()/2], white)
l9 = obj.Label('Wave Number', 'freesansbold.ttf', 16,
               [label_center_x, wave_number_button_y2 + increase_wave_number2.get_height()/2], white)
l10 = obj.Label('Amplitude', 'freesansbold.ttf', 16,
                [label_center_x, amplitude_button_y2 + increase_amplitude2.get_height()/2], white)
wave_text = obj.Label(f'Wave Sum: y = {wave1.get_amplitude()}sin({wave1.get_wave_number()}x '
                      f'{wave1.get_direction_sign_string()} {wave1.get_frequency()}t) + '
                      f'{wave2.get_amplitude()}sin({wave2.get_wave_number()}x '
                      f'{wave2.get_direction_sign_string()} {wave2.get_frequency()}t)', 'freesansbold.ttf', 16,
                      [240, 420], white)
labels = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, wave_text]

clock = pg.time.Clock()
frame_count = 0
time_mouse_pressed = pg.time.get_ticks()   # milliseconds since starting the game

run = True
while run:
    frame_count += 1
    clock.tick(fps)
    pos = pg.mouse.get_pos()
    # events and mouse click handling
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.hover(pos):
                    button.click()
                    wave_text.set_text(f'Wave Sum: y = {wave1.get_amplitude()}sin({wave1.get_wave_number()}x '
                                       f'{wave1.get_direction_sign_string()} {wave1.get_frequency()}t) + '
                                       f'{wave2.get_amplitude()}sin({wave2.get_wave_number()}x '
                                       f'{wave2.get_direction_sign_string()} {wave2.get_frequency()}t)')
                    time_mouse_pressed = pg.time.get_ticks()
    if pg.mouse.get_pressed()[0] and frame_count % 6 == 0 and pg.time.get_ticks() - delay_on_click_ms > time_mouse_pressed:
        for button in buttons:
            if button.hover(pos):
                button.click()
                wave_text.set_text(f'Wave Sum: y = {wave1.get_amplitude()}sin({wave1.get_wave_number()}x '
                                   f'{wave1.get_direction_sign_string()} {wave1.get_frequency()}t) + '
                                   f'{wave2.get_amplitude()}sin({wave2.get_wave_number()}x '
                                   f'{wave2.get_direction_sign_string()} {wave2.get_frequency()}t)')
    # drawing
    screen.fill(black)
    for label in labels:
        label.draw(screen)
    all_sprites.update(screen, pos)
    sum_of_y_positions = wave1.sum_waves(wave2)
    obj.sum_of_waves(screen, x_positions, sum_of_y_positions)
    pg.display.flip()
pg.quit()
