from ascii_magic import AsciiArt, from_image

# This:
my_art = AsciiArt.from_image('images\\lion.jpg')
my_art.to_terminal()

# Does the same as this:
my_art = from_image('images\\lion.jpg')
my_art.to_terminal()