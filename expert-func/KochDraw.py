# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2018/10/31 21:06
'''

import turtle

def koch(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)

if __name__ == '__main__':
    turtle.setup(900,900)
    turtle.pencolor('green')
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(1)
    level = 3
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.hideturtle()