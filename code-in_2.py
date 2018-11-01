import turtle        

sammy= turtle.Turtle()  

sammy.speed(100)
sammy.setpos(0,1)
sammy.setx(0)
sammy.sety(0)
sammy.goto(0,1)
sammy.color("orange", "yellow")   
sammy.getscreen().bgcolor("gray") 

sammy.begin_fill()   

for i in range(144):      
    sammy.forward(200)
    sammy.left(554)
    
for i in range(25):
        sammy.right(47)
        sammy.forward(20)
        sammy.left(16)
        sammy.forward(20)
        
   
sammy.end_fill()

