from tkinter import * 
from random import *

# Game Size
h = 500
w = 500
seg_size = 20

# Create Snake And Navigate
snake = [(240, 240), (220, 240), (200, 240)]
direction = 'Right'

# Food Variable
food = None

# Create Random Food
def create_food():
    global food
    
    if food:
        can.delete(food)
    x = randint(0, (w // seg_size - 1)) * seg_size
    y = randint(0, (h // seg_size - 1)) * seg_size
    food = can.create_oval(x, y, x + seg_size, y + seg_size, fill='lightgreen', outline='red', width=2)

# Do we have a crash or not?
def check(head):
    x, y = head
    if x < 0 or x >= w or y < 0 or y >= h or head in snake[1:]:
        return True
    return False

# Message
def end_game():
    can.create_text(w // 2, h // 2, text='Game over', fill='red', font=('Comic Sans MS', 17, 'bold'))

# Create Keypress Direction
def change_direction(event):
    global direction
    new_direction = event.keysym
    all_directions = {'Right': 'Left', 'Left': 'Right', 'Up': 'Down', 'Down': 'Up'}
    if new_direction in all_directions and all_directions[new_direction] != direction:
        direction = new_direction

def snake_movement():
    global snake
    x, y = snake[0]
    if direction == "Up":
        y -= seg_size
    elif direction == "Down":
        y += seg_size
    elif direction == "Left":
        x -= seg_size
    elif direction == "Right":
        x += seg_size
    new_head = (x, y)
    if check(new_head):
        end_game()
        return
    # تصحیح مقایسه مختصات هدف با سر مار
    food_coords = can.coords(food)
    if food_coords[0:2] == [new_head[0], new_head[1]]:
        snake = [new_head] + snake
        create_food()
    else:
        snake = [new_head] + snake[:-1]
    can.delete('snake')
    for seg in snake:
        can.create_oval(seg[0], seg[1], seg[0] + seg_size, seg[1] + seg_size, fill='green', outline='yellow', tags='snake')
            
    root.after(100, snake_movement)

# Initialize GUI
root = Tk()
root.title('Snake Game')
can = Canvas(root, width=w, height=h, bg='black')
can.pack()
can.bind_all("<KeyPress>", change_direction)

create_food()
snake_movement()

root.mainloop()
