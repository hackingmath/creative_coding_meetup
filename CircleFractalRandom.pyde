

def setup():
  global diam
  size(800,800)
  background(255)
  diam = 300
  #stroke(255)
  noStroke()
  translate(width/2, height/2)
  fill(255,random(255),
    random(255),70)#noFill()
  fractal(0,0,diam,8)
  
def draw():
  pass
  #global diam
  #background(0)
  #translate to the center of the screen
  #translate(width/2, height/2)
  #fractal(0,0,diam,8)
  
def fractal(x,y,diam,level):
  if level > 0:
    angle = map(mouseX,0,width,0,180)
    #draw an ellipse in the center
    
    ellipse(x,y,diam,diam)
    #draw two smaller ellipses on the big one
    
    for i in range(3):
      pushMatrix() #"Save this location/orientation"
      rotate(random(TWO_PI))
      translate(x-diam/2.0,0)
      fractal(0,0,diam*0.5,level - 1)
      popMatrix() #return to saved location
