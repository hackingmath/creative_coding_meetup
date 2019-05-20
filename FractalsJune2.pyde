'''Fractal Exploration for COder School tutorial
June 2, 2018'''

def setup():
    size(800,600)
    
def draw():
    background(255)
    translate(width/2,height-50)
    rotate(PI)
    level = mouseX/40
    angle = mouseY/4.0
    tree(100,angle,level)
    
def tree(sz,angle,level):
    if level > 0:
        strokeWeight(level)
        line(0,0,0,sz)
        translate(0,sz)
        rotate(radians(angle))
        tree(sz*.8,angle,level -1)
        rotate(radians(-2*angle))
        tree(sz*.8,angle,level -1)
        rotate(radians(angle))
        translate(0,-sz)
        
def tree2(sz,level):
    if level > 0:
        line(0,0,0,sz)
        translate(0,sz)
        rotate(radians(30))
        tree(sz*.8,level -1)
        rotate(radians(-50))
        tree(sz*.9,level -1)
        rotate(radians(20))
        translate(0,-sz)
