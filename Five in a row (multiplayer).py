from Tkinter import *
import tkMessageBox
import subprocess
from threading import Timer

root = Tk()

old_grid = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

go_grid = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

canvas = Canvas(root, width = 800, height = 800)
is_white_turn = True
canvas.pack()

def draw_grid():


    for i in range(40,761,40):
        for j in range(40,761,40):
            canvas.create_line(40, i, 760, i, fill = "black")
            canvas.create_line(j, 40, j, 760, fill = "black")
            if [i,j] == [160,160] or [i,j] == [160,400] or [i,j] == [160,640] or [i,j] == [400,160] or [i,j] == [400,400] or [i,j] == [400,640] or [i,j] == [640,160] or [i,j] == [640,400] or [i,j] == [640,640]:
                canvas.create_oval(i - 3,j - 3,i + 3,j + 3, fill = "black")

def get_background():
    global img
    img = PhotoImage(file="~/Desktop/python/GUI/wood.ppm")
    canvas.create_image(0,0, anchor=NW, image=img)

def rounded(x):
    return int(round(float(x) / 40.0) * 40)

def grid_rounded(x):
    return int(round(float(x) / 40.0) - 1)

def grid_copy(grid):
    new_grid = []
    for i in grid:
        new_grid.append(i[:])
    return new_grid

def horizontal(grid):
    for row in grid:
        for i in range(len(row) - 5):
            if set(row[i:i + 5]) == set([1]):
                return 'white'
            elif set(row[i:i + 5]) == set([2]):
                return 'black'
    return 'no'

def vertical(grid):
    for i in range(len(grid) - 5):
        for j in range(len(grid)):
            column = [grid[i][j]] + [grid[i + 1][j]] + [grid[i + 2][j]] + [grid[i + 3][j]] + [grid[i + 4][j]]
            if set(column) == set([1]):
                return 'white'
            elif set(column) == set([2]):
                return 'black'
    return 'no'

def ltrdiagonal(grid):
    for i in range(len(grid) - 4):
        for j in range(len(grid) - 4):
            diagonal = [grid[i][j]] + [grid[i+ 1][j + 1]] + [grid[i + 2][j + 2]] + [grid[i + 3][j + 3]] + [grid[i + 4][j + 4]]
            if set(diagonal) == set([1]):
                return 'white'
            elif set(diagonal) == set([2]):
                return 'black'
    return 'no'

def rtldiagonal(grid):
    for i in range(4,len(grid)):
        for j in range(len(grid) - 4):
            diagonal = [grid[i][j]] + [grid[i - 1][j + 1]] + [grid[i - 2][j + 2]] + [grid[i - 3][j + 3]] + [grid[i - 4][j + 4]]
            if set(diagonal) == set([1]):
                return 'white'
            elif set(diagonal) == set([2]):
                return 'black'
    return 'no'

def who_wins(grid):
    if horizontal(grid) == 'white':
        tkMessageBox.showinfo("go","White Wins!")
    elif horizontal(grid) == 'black':
        tkMessageBox.showinfo("go","Black Wins!")
    elif vertical(grid) == 'white':
        tkMessageBox.showinfo("go","White Wins!")
    elif vertical(grid) == 'black':
        tkMessageBox.showinfo("go","Black Wins!")
    elif ltrdiagonal(grid) == 'white':
        tkMessageBox.showinfo("go","White Wins!")
    elif ltrdiagonal(grid) == 'black':
        tkMessageBox.showinfo("go","Black Wins!")
    elif rtldiagonal(grid) == 'white':
        tkMessageBox.showinfo("go","White Wins!")
    elif rtldiagonal(grid) == 'black':
        tkMessageBox.showinfo("go","Black Wins!")
    elif is_draw(grid):
        tkMessageBox.showinfo("go","Draw!")

def is_draw(grid):
    for i in grid:
        for j in i:
            if j == 0:
                return False
    return True

def valid_position(grid,x,y):
    if grid[x][y] == 0:
        return True

def play_sound():
    subprocess.call(["afplay","/Users/sam/Desktop/python/GUI/click.wav"])

def play(event):
    global is_white_turn
    global go_grid

    x = grid_rounded(event.x)
    y = grid_rounded(event.y)
    if is_white_turn == True:
        color = "white"
        one_or_two = 1
    else:
        color = "black"
        one_or_two = 2

    if not valid_position(go_grid,y,x):
        tkMessageBox.showinfo("go", "Invalid location")
        return

    go_grid[y][x] = one_or_two
    piece = canvas.create_oval(rounded(event.x) - 17, rounded(event.y) - 17, rounded(event.x) + 17, rounded(event.y) + 17, fill = color)
    t = Timer(0.1,play_sound)
    t.start()
    who_wins(go_grid)
    is_white_turn = not is_white_turn

def reset(event):
    global go_grid
    global is_white_turn
    canvas.delete("all")
    go_grid = grid_copy(old_grid)
    is_white_turn = True
    get_background()
    draw_grid()

canvas.bind("<Button-1>", play)
button1 = Button(root, text = "Reset")
button1.bind("<Button-1>", reset)
button1.pack()

get_background()
draw_grid()

root.mainloop()
