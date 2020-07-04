import turtle
wn=turtle.Screen()
wn.title("Ball game")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer()

score_a=0
score_b=0

paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('red')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('blue')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

Ball=turtle.Turtle()
Ball.speed(0)
Ball.shape('circle')
Ball.color('yellow')
Ball.penup()
Ball.goto(0,0)
Ball.dx=2
Ball.dy=2

pen=turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player 1:0 || Player 2:0",align='center',font=('Courier',24,'normal'))

def paddle_a_up():
    y=paddle_a.ycor()
    y=y+20
    paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor()
    y=y-20
    paddle_a.sety(y)
def paddle_b_up():
    y=paddle_b.ycor()
    y=y+20
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor()
    y=y-20
    paddle_b.sety(y)
wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down,'s')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')

while True:
    wn.update()
    Ball.setx(Ball.xcor()+Ball.dx)
    Ball.sety(Ball.ycor()+Ball.dy)
    if(Ball.ycor()>290):
        Ball.sety(290)
        Ball.dy=Ball.dy *-1 
    if(Ball.ycor()<-290):
        Ball.sety(-290)
        Ball.dy=Ball.dy *-1 
    if(Ball.xcor()>390):
        Ball.goto(0,0)
        Ball.dx=Ball.dx *-1
        pen.clear()
        score_a=score_a+1
        pen.write("player 1:{} || Player 2:{}".format(score_a,score_b),align='center',font=('Courier',24,'normal'))

    if(Ball.xcor()<-390):
        Ball.goto(0,0)
        Ball.dx=Ball.dx *-1
        pen.clear()
        score_b=score_b+1
        pen.write("player 1:{} || Player 2:{}".format(score_a,score_b),align='center',font=('Courier',24,'normal'))


    if(Ball.xcor()>340 and Ball.xcor()<350)and(Ball.ycor()<paddle_b.ycor() + 50 and Ball.ycor()> paddle_b.ycor() - 50):
        Ball.setx(340)
        Ball.dx=Ball.dx *-1
    if(Ball.xcor()<-340 and Ball.xcor()>-350)and(Ball.ycor()<paddle_a.ycor() + 50 and Ball.ycor()> paddle_a.ycor() - 50):
        Ball.setx(-340)
        Ball.dx=Ball.dx *-1
    
