from Tkinter import *
import tkMessageBox
import subprocess
from threading import Timer
root = Tk()
root.title('Five in a row')
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

intersections = [[40, 40], [40, 80], [40, 120], [40, 160], [40, 200], [40, 240], [40, 280], [40, 320], [40, 360], [40, 400], [40, 440], [40, 480], [40, 520], [40, 560], [40, 600], [40, 640], [40, 680], [40, 720], [40, 760], [80, 40], [80, 80], [80, 120], [80, 160], [80, 200], [80, 240], [80, 280], [80, 320], [80, 360], [80, 400], [80, 440], [80, 480], [80, 520], [80, 560], [80, 600], [80, 640], [80, 680], [80, 720], [80, 760], [120, 40], [120, 80], [120, 120], [120, 160], [120, 200], [120, 240], [120, 280], [120, 320], [120, 360], [120, 400], [120, 440], [120, 480], [120, 520], [120, 560], [120, 600], [120, 640], [120, 680], [120, 720], [120, 760], [160, 40], [160, 80], [160, 120], [160, 160], [160, 200], [160, 240], [160, 280], [160, 320], [160, 360], [160, 400], [160, 440], [160, 480], [160, 520], [160, 560], [160, 600], [160, 640], [160, 680], [160, 720], [160, 760], [200, 40], [200, 80], [200, 120], [200, 160], [200, 200], [200, 240], [200, 280], [200, 320], [200, 360], [200, 400], [200, 440], [200, 480], [200, 520], [200, 560], [200, 600], [200, 640], [200, 680], [200, 720], [200, 760], [240, 40], [240, 80], [240, 120], [240, 160], [240, 200], [240, 240], [240, 280], [240, 320], [240, 360], [240, 400], [240, 440], [240, 480], [240, 520], [240, 560], [240, 600], [240, 640], [240, 680], [240, 720], [240, 760], [280, 40], [280, 80], [280, 120], [280, 160], [280, 200], [280, 240], [280, 280], [280, 320], [280, 360], [280, 400], [280, 440], [280, 480], [280, 520], [280, 560], [280, 600], [280, 640], [280, 680], [280, 720], [280, 760], [320, 40], [320, 80], [320, 120], [320, 160], [320, 200], [320, 240], [320, 280], [320, 320], [320, 360], [320, 400], [320, 440], [320, 480], [320, 520], [320, 560], [320, 600], [320, 640], [320, 680], [320, 720], [320, 760], [360, 40], [360, 80], [360, 120], [360, 160], [360, 200], [360, 240], [360, 280], [360, 320], [360, 360], [360, 400], [360, 440], [360, 480], [360, 520], [360, 560], [360, 600], [360, 640], [360, 680], [360, 720], [360, 760], [400, 40], [400, 80], [400, 120], [400, 160], [400, 200], [400, 240], [400, 280], [400, 320], [400, 360], [400, 400], [400, 440], [400, 480], [400, 520], [400, 560], [400, 600], [400, 640], [400, 680], [400, 720], [400, 760], [440, 40], [440, 80], [440, 120], [440, 160], [440, 200], [440, 240], [440, 280], [440, 320], [440, 360], [440, 400], [440, 440], [440, 480], [440, 520], [440, 560], [440, 600], [440, 640], [440, 680], [440, 720], [440, 760], [480, 40], [480, 80], [480, 120], [480, 160], [480, 200], [480, 240], [480, 280], [480, 320], [480, 360], [480, 400], [480, 440], [480, 480], [480, 520], [480, 560], [480, 600], [480, 640], [480, 680], [480, 720], [480, 760], [520, 40], [520, 80], [520, 120], [520, 160], [520, 200], [520, 240], [520, 280], [520, 320], [520, 360], [520, 400], [520, 440], [520, 480], [520, 520], [520, 560], [520, 600], [520, 640], [520, 680], [520, 720], [520, 760], [560, 40], [560, 80], [560, 120], [560, 160], [560, 200], [560, 240], [560, 280], [560, 320], [560, 360], [560, 400], [560, 440], [560, 480], [560, 520], [560, 560], [560, 600], [560, 640], [560, 680], [560, 720], [560, 760], [600, 40], [600, 80], [600, 120], [600, 160], [600, 200], [600, 240], [600, 280], [600, 320], [600, 360], [600, 400], [600, 440], [600, 480], [600, 520], [600, 560], [600, 600], [600, 640], [600, 680], [600, 720], [600, 760], [640, 40], [640, 80], [640, 120], [640, 160], [640, 200], [640, 240], [640, 280], [640, 320], [640, 360], [640, 400], [640, 440], [640, 480], [640, 520], [640, 560], [640, 600], [640, 640], [640, 680], [640, 720], [640, 760], [680, 40], [680, 80], [680, 120], [680, 160], [680, 200], [680, 240], [680, 280], [680, 320], [680, 360], [680, 400], [680, 440], [680, 480], [680, 520], [680, 560], [680, 600], [680, 640], [680, 680], [680, 720], [680, 760], [720, 40], [720, 80], [720, 120], [720, 160], [720, 200], [720, 240], [720, 280], [720, 320], [720, 360], [720, 400], [720, 440], [720, 480], [720, 520], [720, 560], [720, 600], [720, 640], [720, 680], [720, 720], [720, 760], [760, 40], [760, 80], [760, 120], [760, 160], [760, 200], [760, 240], [760, 280], [760, 320], [760, 360], [760, 400], [760, 440], [760, 480], [760, 520], [760, 560], [760, 600], [760, 640], [760, 680], [760, 720], [760, 760]]

canvas = Canvas(root, width = 800, height = 800)
is_white_turn = False
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
    if is_white_turn == False:
        color = "black"
        one_or_two = 2
    else:
        color = "white"
        one_or_two = 1

    if [rounded(event.y),rounded(event.x)] not in intersections or not valid_position(go_grid,y,x):
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
