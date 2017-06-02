import turtle

pen = turtle.Turtle()
wn = turtle.Screen()

pen.speed(0)

def frag(n,sz):
    if(n==1):
        pen.forward(sz)
        pen.left(60)
        pen.forward(sz)
        pen.right(120)
        pen.forward(sz)
        pen.left(60)
        pen.forward(sz)
        return
    frag(n-1,sz/3)
    pen.left(60)
    frag(n-1,sz/3)
    pen.right(120)
    frag(n-1,sz/3)
    pen.left(60)
    frag(n-1,sz/3)
    
frag(4,150)
wn.mainloop()