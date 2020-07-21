#This is going outside src for now because Python can't handle ../ and I don't want to import a whole library for basic directory navigation functionality in a programming language.

import pyglet
from pyglet.window import key

window = pyglet.window.Window()
label = pyglet.text.Label('Welcome to Henwen',
                        font_name='Verdana',
                        font_size=36,
                        x=window.width//2, y=window.height//2,
                        anchor_x='center', anchor_y='center')

keys = key.KeyStateHandler()
window.push_handlers(keys)

idlePig = pyglet.resource.image('assets/sprites/pig/pig_idle.png')
pigW1 = pyglet.resource.image('assets/sprites/pig/pig_walk_1.png')
pigW2 = pyglet.resource.image('assets/sprites/pig/pig_walk_2.png')
pigW = [pigW1, pigW2]

pigWA = pyglet.image.Animation.from_image_sequence(pigW, 0.5, True)
# skeleton = pyglet.image.load('assets/spritesheets/skeleton.png')
# skeleton_seq = pyglet.image.ImageGrid(skeleton, 2, 8)

# skel_frame_1 = skeleton_seq[0,0]
# skel_frame_2 = skeleton_seq[0,1]

# start_skel = skeleton_seq[:3]

pigSprite = pyglet.sprite.Sprite(pigWA)

def update(dt):

    if keys[key.D]:
        pigSprite.x += 1/600
    if keys[key.A]:
        pigSprite.x -= 1/600
        

@window.event
def on_draw():
    window.clear()
    label.draw()
    pigSprite.draw()
    pyglet.clock.schedule_interval(update, 1/60.)
    # pig.blit(0,0)

pyglet.app.run()