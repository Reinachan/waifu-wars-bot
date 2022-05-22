from PIL import Image
import os

width, height = 225, 350  # w/h of a contestant image


def create_battle_image():
    canvas = Image.new(
        mode="RGB",
        size=(825, height),
        color=(255, 255, 255)
    )

    versus = Image.open('versus.png')
    versus_background = Image.new(
        mode="RGBA",
        size=(versus.size),
        color=(255, 255, 255, 255)
    )
    versus = Image.alpha_composite(versus_background, versus)

    # TODO: exchange the left/right Image.open() with images from the server
    left = Image.open('1.jpg')
    right = Image.open('2.jpg')
    left = left.resize((width, height))
    right = right.resize((width, height))

    canvas.paste(left, (0, 0))
    canvas.paste(versus, (255, 20))
    canvas.paste(right, (600, 0))

    if not os.path.isdir('generated'):
        os.mkdir('generated')

    canvas.save('generated/battle.jpg')
