from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse
import sys, time, math, os, random
from pyglet.image.codecs.png import PNGImageDecoder
from PIL import Image

try:
    from PIL.Image import open
except ImportError as err:
    from Image import open
window = pyglet.window.Window()
keyboard = pyglet.window.key.KeyStateHandler()
window.push_handlers(keyboard)
glClear(GL_COLOR_BUFFER_BIT)
imagePath = "track.png"
im = Image.open(imagePath) 
pix = im.load()

vel = 6

#label = pyglet.text.Label('Hello, world', font_name='Times New Roman', font_size=36,x=window.width//2,y=window.height//2,anchor_x='center', anchor_y='center')
#@window.event
#def on_draw():
#    window.clear()
#    label.draw()
buffer = 7
if True==False:
    #@window.event 
    #def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('The Key "A" was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow was pressed.')
    elif symbol == key.ENTER:
        print('The enter keywas pressed.')
    #@window.event
    #def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed.')
    #window.push_handlers(pyglet.window.event.WindowEventLogger())
    #pyglet.app.run()

class Square:
    def __init__(self, height, width, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.xvel = 0
        self.yvel = 0
        self.angle = 90
        self.size = 1
        self.width = width
        self.height = height
        self.color = (0,255,0)
        x = width/2.0
        y = height/2.0
        self.vlist = pyglet.graphics.vertex_list(4, ('v2f', [-x,-y, x,-y, -x,y, x,y]), ('t2f', [0,0, 1,0, 0,1, 1,1]))
        self.x = [0] * 5
        self.y = [0] * 5
        self.pixel = [0] * 5
        self.scr = 0
        self.scg = 0
        self.scb = 0
    def draw(self):
        if(self.angle>=360):
            self.angle -= 360
        if(self.angle<=0):
            self.angle += 360
        self.xvel=(math.sin(math.radians(self.angle + 90)) * vel)
        self.yvel=-(math.cos(math.radians(self.angle + 90)) * vel)
        glPushMatrix()
        glTranslatef(self.xpos, self.ypos, 0)
        glRotatef(self.angle, 0, 0, 1)
        glScalef(self.size, self.size, self.size)
        glColor3f(self.scr,self.scg,self.scb)
        self.vlist.draw(GL_TRIANGLE_STRIP)
        glPopMatrix()
    def forward(self):
        #self.xvel = self.xvel + math.sin(math.radians(self.angle+90)) * (keyboard[pyglet.window.key.A] + keyboard[pyglet.window.key.D]) * .1
        #self.yvel = self.yvel + math.cos(math.radians(self.angle+90)) * (keyboard[pyglet.window.key.A] + keyboard[pyglet.window.key.D]) * -1 * .1
        #self.xpos += self.xvel
        #self.ypos += self.yvel
        if ((self.xvel > 0 and self.xvel + self.xpos + self.width/2 * self.size + buffer < window.width) or (self.xvel < 0 and self.xvel + self.xpos - buffer - self.width/2 * self.size> 0)):
            self.xpos += self.xvel
        if ((self.yvel > 0 and self.yvel + self.ypos + self.width/2 * self.size + buffer < window.height) or (self.yvel < 0 and self.yvel + self.ypos - buffer - self.width/2 * self.size> 0)):
            self.ypos += self.yvel
    def backward(self):
        if ((-self.xvel > 0 and -self.xvel/2 + self.xpos + self.width/2 * self.size + buffer < window.width) or (-self.xvel < 0 and -self.xvel/2 + self.xpos - buffer - self.width/2 * self.size > 0)):
            self.xpos -= self.xvel/2
        if ((-self.yvel > 0 and -self.yvel/2 + self.ypos + self.width/2 * self.size + buffer < window.height) or (-self.yvel < 0 and -self.yvel/2 + self.ypos - buffer - self.width/2 * self.size> 0)):
            self.ypos -= self.yvel/2
    def Dots(self):
        self.angle1 = math.degrees(math.atan((self.width/2)/(self.height/2)))
        self.angle2 = self.angle/self.angle1 - self.angle1/100 - math.pi/100
        self.angle3 = self.angle/self.angle1 + self.angle1/100
        self.lengthy = math.hypot((self.width/2),(self.height/2)) * self.size
        self.x[1] = self.lengthy*math.cos(self.angle2) + self.xpos
        self.y[1] = self.lengthy*math.sin(self.angle2) + self.ypos
        self.x[2] = -self.lengthy*math.cos(self.angle2) + self.xpos
        self.y[2] = -self.lengthy*math.sin(self.angle2) + self.ypos
        self.x[3] = self.lengthy*math.cos(self.angle3) + self.xpos
        self.y[3] = self.lengthy*math.sin(self.angle3) + self.ypos
        self.x[4] = -self.lengthy*math.cos(self.angle3) + self.xpos
        self.y[4] = -self.lengthy*math.sin(self.angle3) + self.ypos
 
        #print("X2 " + str(self.x1))
        #print("X1 " + str(self.y1))
        #print("L " + str(self.lengthy))
        #print("A1 " + str(self.angle1))
        #print("A2 " + str(self.angle2))
        glPushMatrix()
        glColor3f(1,1,1)
        for i in range(1, len(self.x)):
            pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
            ('v2f', (self.x[i], self.y[i])),
            ('c3B', self.color )
            )
        glPopMatrix()
        self.Dead()
    def Dead(self):
        dead = False
        for i in range(1, len(self.x)):
            self.pixel[i] = pix[self.x[i],window.height-self.y[i]][1]
            if(self.pixel[i] <= 200):
                dead = True
        if(dead == True):
            self.scr = 255
        else:
            self.scr = 0


square1 = Square(20, 30, 300, 200)


#@window.event
#def on_mouse_press(mousex, mousey, button, modifiers):


def update(dummy):
    global square1
    
    if keyboard[pyglet.window.key.A]:
        square1.angle += 5
    if keyboard[pyglet.window.key.D]:
        square1.angle -= 5
    if keyboard[pyglet.window.key.W]:
        square1.forward()
    if keyboard[pyglet.window.key.S]:
        square1.backward()
    if keyboard[pyglet.window.key.UP]:
        square1.size *= 1.1
    if keyboard[pyglet.window.key.DOWN]:
        square1.size /= 1.1
    if keyboard[pyglet.window.key.LEFT]:
        square1.angle += 5
    if keyboard[pyglet.window.key.RIGHT]:
        square1.angle -= 5
image = pyglet.image.load(imagePath)

def main():
    batch = pyglet.graphics.Batch()
    background = pyglet.graphics.OrderedGroup(0)
    sprites = pyglet.sprite.Sprite(image, batch=batch)
    sprites.scale = 1
    @window.event
    def on_draw():
        window.clear()
        batch.draw()
        square1.draw()
        square1.Dots()
    pyglet.app.run()

pyglet.clock.schedule_interval(update,1/60.0)

if __name__ == '__main__':
  main()