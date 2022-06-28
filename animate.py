from gturtle import *
import time
time_delay = 0.5


makeTurtle()
hideTurtle()

def snake_head():
    repeat 4:
        fd(50)
        rt(90)
            
def snake_body_part(n): 
    fd(n)
    
    repeat 4:
        fd(50)
        rt(90)   

def create_body(n ,k):
    i = 0
    while i != n:
        snake_body_part(k)
        i += 1
        
def snake_head_move():
    setPenColor("white")
    snake_head()
    fd(50)
    
    setPenColor("red")
    snake_head()

def body_move_fd(n): 
    time.sleep(time_delay)
    setPenColor("white")
    fd(-50)
    create_body(n, 50)
    fd(50)
    
    snake_head_move()
    setPenColor("red")
    
    setPenColor("blue")
    create_body(n, -50)

    