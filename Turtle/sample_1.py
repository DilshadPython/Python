from turtle import *
color('blue', 'gold')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 2:
        break
end_fill()
done()