# window settings
screen_width = 800
screen_height = int(screen_width*9/16)
screen_caption = 'Wave Addition'
fps = 60

# sidebar and button settings
sidebar_width = 220
sidebar_x0 = screen_width - sidebar_width
button_flash_duration = .1
sidebar_x1 = sidebar_x0 + 20
sidebar_center_x = int(sidebar_x1 + ((screen_width - sidebar_x1) / 2))
label_center_x = sidebar_center_x + 30
delay_on_click_ms = 600

direction_button_y1 = 50
frequency_button_y1 = 90
wave_number_button_y1 = 130
amplitude_button_y1 = 170

direction_button_y2 = 250
frequency_button_y2 = 290
wave_number_button_y2 = 330
amplitude_button_y2 = 370

# colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
purple = (255, 0, 255)

# wave settings
wave1_y_anchor = 30
wave2_y_anchor = 130
wave_sum_anchor = 230
wave_default_frequency = 4
wave_max_frequency = 16
wave_min_frequency = .5
wave_default_amplitude = 20
wave_default_wave_number = 20
wave_max_wave_number = 30
wave_min_wave_number = .2
wave_min_amplitude = 0
wave_max_amplitude = 35
wave_x0 = 0
wave_xf = screen_width - sidebar_width
wave1_color = red
wave2_color = blue
sum_color = purple
