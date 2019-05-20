'''Circle Fractal
This one rotates!'''

def setup():
    size(600,600)
    noFill()
    global t
    t=0
    
def draw():
    global t
    background(255)
    translate(width/2, height/2)
    circleThing(150,7,t)
    t += 0.1
    
def circleThing(diam,level,t):
    if level > 0:
        fill(255)
        ellipse(0,0,diam,diam)
        for i in range(3):
            pushMatrix()
            rotate(radians(120*i+t))
            translate(0,0.75*diam)
            circleThing(diam/2,level-1,t)
            popMatrix()
