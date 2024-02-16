from turtle import *
speed(4)
# hideturtle()
setup(800,600)
bgcolor('#353935')
title('Sivalling Design by Mahuley Ji')

def my_goto(x,y):
    pencolor('#4682B4')
    penup()
    goto(x,y)
    pendown()

def round_rectangle(center_x,center_y,
            width,height,cornersize):
    penup()    
    goto(center_x-width/2+cornersize,
         center_y-height/2)
    pendown()
    for _ in range(2):
        fillcolor('#4682B4')
        begin_fill()
        forward(width-2*cornersize)
        circle(cornersize,90)
        forward(height-2*cornersize)
        circle(cornersize,90)
        end_fill()

def round_rectangle(center_x,center_y,
            width,height,cornersize):
    penup()    
    goto(center_x-width/2+cornersize,
         center_y-height/2)
    pendown()
    for _ in range(2):
        pencolor("#4682B4")
        fillcolor('#4682B4')
        begin_fill()
        forward(width-2*cornersize)
        circle(cornersize,90)
        forward(height-2*cornersize)
        circle(cornersize,90)
        end_fill()

round_rectangle(0,0,200,300,80)        

fillcolor('#4682B4')
begin_fill()

goto(-35,40)
penup()
fillcolor('orange')
begin_fill()
forward(80)
left(90)
forward(10)
left(90)
forward(80)
left(90)
forward(10)
left(90)

goto(-35,80)
forward(80)
left(90)
forward(10)
left(90)
forward(80)
left(90)
forward(10)
left(90)

goto(-35,60)
forward(80)
left(90)
forward(10)
left(90)
forward(80)
left(90)
forward(10)
left(90)

pendown()
end_fill()

fillcolor('red')
begin_fill()
goto(5,50)
penup()
r=15
circle(r)
pendown()
end_fill()

penup()
goto(-150,-175)
pencolor('#4682B4')
fillcolor('#4682B4')
begin_fill()

round_rectangle(90,-111,600,70,37)
round_rectangle(90,-160,600,70,37)

penup()
goto(0, 210)
pendown()
speed(1)
color('orange')
style=('Courier',30, 'bold')
write('Om Namah Shivaya', font=style,
         align='center', move=True)

done()

