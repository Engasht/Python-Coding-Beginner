def turn_right():
    turn_left()
    turn_left()
    turn_left()

'''
while front_is_clear():
    move()
turn_left()
'''

rotation = 0
while not at_goal():
    if rotation == 4:
        turn_left()
        rotation = 0
    if right_is_clear():
        turn_right()
        rotation += 1
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        rotation -= 1