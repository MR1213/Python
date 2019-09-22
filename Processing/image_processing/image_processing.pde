PImage img;
int smallPoint, largePoint;

void setup() {
  
  img = loadImage("ball.jpg");
  size(870,1370);
   smallPoint = 1;
   largePoint = 10;
  imageMode(CENTER);
  noStroke();
  background(255);
}

void draw() { 
  for(int i = 0; i<150000; i++){
    float pointillize = map(mouseX, 0, width, smallPoint, largePoint);
    int x = int(random(img.width));
    int y = int(random(img.height));
    color pix = img.get(x, y);
    fill(pix, 128);
    ellipse(x, y, pointillize, pointillize);
  }

}
