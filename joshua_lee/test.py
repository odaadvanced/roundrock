from oled_text import OledText


# Create the display, pass its pixel dimensions
oled = OledText(i2c, 128, 64)

# Write to the oled
oled.text("Hello ...", 1)  # Line 1
oled.text("... world!", 2)  # Line 2