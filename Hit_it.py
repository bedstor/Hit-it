from turtle import *


def main():
    class Sprite(Turtle):
        def __init__(self, x, y, step=10, shape='circle', color='orange'):
            super().__init__()
            self.penup()
            self.speed(0)
            self.goto(x,y)
            self.shape(shape)
            self.color(color)
            self.step = step
        def move_left(self):
            self.goto(self.xcor() - self.step, self.ycor())
        def move_up(self):
            self.goto(self.xcor(), self.ycor() + self.step)
        def move_right(self):
            self.goto(self.xcor() + self.step, self.ycor())
        def move_down(self):
            self.goto(self.xcor(), self.ycor() - self.step)
        def is_collide(self, sprite):
            dist = self.distance(sprite.xcor(), sprite.ycor())
            if dist < 30:
                return True
            else:
                return False
        def set_move(self, xstart, ystart, xend, yend):
            self.xstart = xstart
            self.ystart = ystart
            self.xend = xend
            self.yend = yend
            self.goto(xstart, ystart)
            self.setheading(self.towards(xend, yend))
        def make_step(self):
            self.forward(self.step)
            if self.distance(self.xend, self.yend) < self.step:
                self.set_move(self.xend,self.yend,self.xstart,self.ystart)
    
    
    
    player = Sprite(0,-150)
    enemy = Sprite(-200,-50, 30, 'square', 'red')
    enemy.set_move(-200,-50,200,-50)
    enemy2 = Sprite(200,50, 30, 'square', 'red')
    enemy2.set_move(200,50,-200,50)
    finish = Sprite(0,150, 10, 'triangle', 'green')
    t = Turtle()
    t.penup()
    t.goto(-10,200)
    t.pendown()
    t.hideturtle()
    
    
    scr = player.getscreen()
    scr.listen()
    scr.onkey(player.move_left, 'Left')
    scr.onkey(player.move_down, 'Down')
    scr.onkey(player.move_right, 'Right')
    scr.onkey(player.move_up, 'Up')
    
    total_score = 0
    while total_score < 3:
        enemy.make_step()
        enemy2.make_step()
        if player.is_collide(finish):
            player.goto(0, -150)
            total_score += 1
            t.clear()
        if player.is_collide(enemy) or player.is_collide(enemy2):
            finish.hideturtle()
            break
        t.write(str(total_score), font =('Arial', 30, 'bold'))
    
    if total_score >= 3:
        enemy.hideturtle()
        enemy2.hideturtle()


if __name__ == '__main__':
    main()


    
        
        


