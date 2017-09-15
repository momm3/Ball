import pyglet
from pyglet.window import mouse

window = pyglet.window.Window(650,400)
icon1 = pyglet.image.load('16x16.png')
icon2 = pyglet.image.load('32x32.png')
window.set_icon(icon1,icon2)

image=pyglet.image.load('cursor.jpg')
cursor = pyglet.window.ImageMouseCursor(image, 16, 8)
window.set_mouse_cursor(cursor)

image = pyglet.resource.image('paper.png')
sprite = pyglet.sprite.Sprite(image)

###10px=1m
###INIIALS
def initialPush():
    sprite.x = 0
    sprite.dx = 100
    sprite.dy = 0
    sprite.y = 390
    sprite.ay = 981
    sprite.n = 1
#SPRING CONSTANT
    sprite.k = 3/4
initialPush()

def update(dt):
    ground = 0
    sprite.x += sprite.dx * dt
    if (sprite.y)>ground:
        sprite.y -= sprite.dy * dt
        sprite.dy += sprite.ay * dt
    elif (sprite.y)<ground:
        sprite.dy = -(sprite.k**sprite.n)*(sprite.dy)
        sprite.y = 2
        sprite.n += 1
        sprite.dx -= 10
        print(sprite.n-1)
    if (sprite.n == 10):
        sprite.dy = 0
        sprite.ay = 0
        sprite.y = 0
        sprite.dx = 0

pyglet.clock.schedule_interval(update, 1/60.0)

###KEY PRESSs
@window.event
def on_key_press(symbol, modifiers):
    print ("Reset Ball")
    initialPush()
###WINDOW DRAW
@window.event
def on_draw():
    window.clear()
    sprite.draw()

pyglet.app.run()
