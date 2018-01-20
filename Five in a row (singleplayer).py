from Tkinter import *
import tkMessageBox
import random
import time
from threading import Timer
import subprocess

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

def two_h(grid):
    x = []
    for i in range(len(grid)):
        for j in range(len(grid) - 2):
            row = grid[i][j:j + 2]
            if set(row) == set([2]):
                x.append([1,[i,j]])

    return x

def two_v(grid):
    x = []
    for i in range(len(grid) - 2):
        for j in range(len(grid)):
            column = [grid[i][j]] + [grid[i + 1][j]]
            if set(column) == set([2]):
                x.append([2,[i,j]])
                print(x)

    return x

def two_ltr(grid):
    x = []
    for i in range(len(grid) - 1):
        for j in range(len(grid) - 1):
            diagonal = [grid[i][j]] + [grid[i+ 1][j + 1]]
            if set(diagonal) == set([2]):
                x.append([3,[i,j]])

    return x

def two_rtl(grid):
    x = []
    for i in range(1,len(grid)):
        for j in range(len(grid) - 1):
            diagonal = [grid[i][j]] + [grid[i - 1][j + 1]]
            if set(diagonal) == set([2]):
                x.append([4,[i,j]])

    return x

def if_two(grid):
    s = 0
    if len(two_h(grid)) >= 1:
        s = 1

    elif len(two_v(grid)) >= 1:
        s = 2

    elif len(two_ltr(grid)) >= 1:
        s = 3

    elif len(two_rtl(grid)) >= 1:
        s = 4

    return s

def three_h(grid):
    x = []
    for i in range(len(grid)):
        for j in range(len(grid) - 3):
            row = grid[i][j:j + 3]
            if set(row) == set([2]):
                x.append([1,[i,j + 1]])

    return x

def three_v(grid):
    x = []
    for i in range(len(grid) - 3):
        for j in range(len(grid)):
            column = [grid[i][j]] + [grid[i + 1][j]] + [grid[i + 2][j]]
            if set(column) == set([2]):
                x.append([2,[i + 1,j]])

    return x

def three_ltr(grid):
    x = []
    for i in range(len(grid) - 2):
        for j in range(len(grid) - 2):
            diagonal = [grid[i][j]] + [grid[i+ 1][j + 1]] + [grid[i + 2][j + 2]]
            if set(diagonal) == set([2]):
                x.append([3,[i+ 1,j + 1]])

    return x

def three_rtl(grid):
    x = []
    for i in range(2,len(grid)):
        for j in range(len(grid) - 2):
            diagonal = [grid[i][j]] + [grid[i - 1][j + 1]] + [grid[i - 2][j + 2]]
            if set(diagonal) == set([2]):
                x.append([4,[i - 1,j + 1]])

    return x

def if_three(grid):
    s = 0
    if len(three_h(grid)) >= 1:
        s = 1

    elif len(three_v(grid)) >= 1:
        s = 2

    elif len(three_ltr(grid)) >= 1:
        s = 3

    elif len(three_rtl(grid)) >= 1:
        s = 4

    return s

def blockable_spaces_two(lst):
    global go_grid

    a = lst[0]
    x = lst[1][0]
    y = lst[1][1]

    if a == 1:
        return [[x,y - 1],[x,y + 2]]
    elif a == 2:
        return[[x - 1,y],[x + 2,y]]
    elif a == 3:
        return [[x + 2,y + 2],[x - 1, y - 1]]
    else:
        return [[x - 2,y + 2],[x + 1,y - 1]]

def blockable_spaces_three(lst):
    global go_grid

    a = lst[0]
    x = lst[1][0]
    y = lst[1][1]

    if a == 1:
        return [[x,y - 2],[x,y + 2]]
    elif a == 2:
        return[[x - 2,y],[x + 2,y]]
    elif a == 3:
        return [[x + 2,y + 2],[x - 2, y - 2]]
    else:
        return [[x - 2,y + 2],[x + 2,y - 2]]

def is_unblocked(lst,grid):
    for j in blockable_spaces_three(lst):
        if grid[j[0]][j[1]] != 0:
            return False
    return True

def how_many_unblocked_threes(grid):
    x = 0
    for i in how_many_threes(grid):
        if is_unblocked(i,grid):
            x += 1
    return x

def is_double_threes(worb,grid):
    s = 0
    if worb == 'white':
        s = 1
    elif worb == 'black':
        s = 2

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0 and surrounding(grid,i,j):
                grid[i][j] = s
                if how_many_unblocked_threes(grid) == 2:
                    grid[i][j] = 0
                    return [i,j]
                else:
                    grid[i][j] = 0
                    continue
            else:
                continue
    return [0]

def four_h_white(grid):
    for i in range(len(grid)):
        for j in range(len(grid) - 4):
            row = grid[i][j:j + 4]
            if set(row) == set([1]) and grid[i][j - 1] == 0 and grid[i][j + 4] == 0:
                print(1)
                return True

def four_v_white(grid):
    for i in range(len(grid) - 4):
        for j in range(len(grid)):
            column = [grid[i][j]] + [grid[i + 1][j]] + [grid[i + 2][j]] + [grid[i + 3][j]]
            if set(column) == set([1]) and grid[i - 1][j] == 0 and grid[i + 4][j] == 0:
                return True

def four_ltr_white(grid):
    for i in range(len(grid) - 3):
        for j in range(len(grid) - 3):
            diagonal = [grid[i][j]] + [grid[i+ 1][j + 1]] + [grid[i + 2][j + 2]] + [grid[i + 3][j + 3]]
            if set(diagonal) == set([1]) and grid[i - 1][j - 1] == 0 and grid[i + 4][j + 4] == 0:
                return True

def four_rtl_white(grid):
    for i in range(3,len(grid)):
        for j in range(len(grid) - 3):
            diagonal = [grid[i][j]] + [grid[i - 1][j + 1]] + [grid[i - 2][j + 2]] + [grid[i - 3][j + 3]]
            if set(diagonal) == set([1]) and grid[i + 1][j - 1] == 0 and grid[i - 4][j + 4] == 0:
                return True

def is_unblocked_four_white(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0 and surrounding(grid,i,j):
                grid[i][j] = 1
                if four_h_white(grid) or four_v_white(grid) or four_ltr_white(grid) or four_rtl_white(grid):
                    grid[i][j] = 0
                    return [i,j]
                else:
                    grid[i][j] = 0
                    continue
            else:
                continue
    return [0]

def is_white_five(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0 and surrounding(grid,i,j):
                grid[i][j] = 1
                if horizontal(grid) == 'white' or vertical(grid) == 'white' or ltrdiagonal(grid) == 'white' or rtldiagonal(grid) == 'white':
                    grid[i][j] = 0
                    return [i,j]
                else:
                    grid[i][j] = 0
                    continue
            else:
                continue
    return [0]

def is_black_five(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0 and surrounding(grid,i,j):
                grid[i][j] = 2
                if horizontal(grid) == 'black' or vertical(grid) == 'black' or ltrdiagonal(grid) == 'black' or rtldiagonal(grid) == 'black':
                    grid[i][j] = 0
                    return [i,j]
                else:
                    grid[i][j] = 0
                    continue
            else:
                continue
    return [0]

def four_and_three(worb,grid):
    s = 0
    if worb == 'white':
        s = 1
    elif worb == 'black':
        s = 2
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0 and surrounding(grid,i,j):
                grid[i][j] = s
                if how_many_unblocked_threes(grid) == 1:
                    if semi_four_h_black(grid) or semi_four_v_black(grid) or semi_four_ltr_black(grid) or semi_four_rtl_black(grid):
                        grid[i][j] = 0
                        return [i,j]
                    else:
                        grid[i][j] = 0
                        continue
                else:
                    grid[i][j] = 0
                    continue
    return [0]

def semi_four_h_black(grid):
    for i in range(len(grid)):
        for j in range(len(grid) - 4):
            row = grid[i][j:j + 4]
            if set(row) == set([2]):
                if grid[i][j - 1] == 0 or grid[i][j + 4] == 0:
                    return True

def semi_four_v_black(grid):
    for i in range(len(grid) - 4):
        for j in range(len(grid)):
            column = [grid[i][j]] + [grid[i + 1][j]] + [grid[i + 2][j]] + [grid[i + 3][j]]
            if set(column) == set([2]):
                if grid[i - 1][j] == 0 or grid[i + 4][j] == 0:
                    return True

def semi_four_ltr_black(grid):
    for i in range(len(grid) - 3):
        for j in range(len(grid) - 3):
            diagonal = [grid[i][j]] + [grid[i+ 1][j + 1]] + [grid[i + 2][j + 2]] + [grid[i + 3][j + 3]]
            if set(diagonal) == set([2]):
                if grid[i - 1][j - 1] == 0 and grid[i + 4][j + 4] == 0:
                    return True

def semi_four_rtl_black(grid):
    for i in range(3,len(grid)):
        for j in range(len(grid) - 3):
            diagonal = [grid[i][j]] + [grid[i - 1][j + 1]] + [grid[i - 2][j + 2]] + [grid[i - 3][j + 3]]
            if set(diagonal) == set([2]):
                if grid[i + 1][j - 1] == 0 and grid[i - 4][j + 4] == 0:
                    return True

def four_h_black(grid):
    for i in range(len(grid)):
        for j in range(len(grid) - 4):
            row = grid[i][j:j + 4]
            if set(row) == set([2]) and grid[i][j - 1] == 0 and grid[i][j + 4] == 0:
                return True

def four_v_black(grid):
    for i in range(len(grid) - 4):
        for j in range(len(grid)):
            column = [grid[i][j]] + [grid[i + 1][j]] + [grid[i + 2][j]] + [grid[i + 3][j]]
            if set(column) == set([2]) and grid[i - 1][j] == 0 and grid[i + 4][j] == 0:
                return True

def four_ltr_black(grid):
    for i in range(len(grid) - 3):
        for j in range(len(grid) - 3):
            diagonal = [grid[i][j]] + [grid[i+ 1][j + 1]] + [grid[i + 2][j + 2]] + [grid[i + 3][j + 3]]
            if set(diagonal) == set([2]) and grid[i - 1][j - 1] == 0 and grid[i + 4][j + 4] == 0:
                return True

def four_rtl_black(grid):
    for i in range(3,len(grid)):
        for j in range(len(grid) - 3):
            diagonal = [grid[i][j]] + [grid[i - 1][j + 1]] + [grid[i - 2][j + 2]] + [grid[i - 3][j + 3]]
            if set(diagonal) == set([2]) and grid[i + 1][j - 1] == 0 and grid[i - 4][j + 4] == 0:
                return True

def is_unblocked_four_black(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0 and surrounding(grid,i,j):
                grid[i][j] = 2
                if four_h_black(grid) or four_v_black(grid) or four_ltr_black(grid) or four_rtl_black(grid):
                    grid[i][j] = 0
                    return [i,j]
                else:
                    grid[i][j] = 0
                    continue
            else:
                continue
    return [0]

def who_wins(grid):
    s = 0
    if horizontal(grid) == 'white':
        s = 1
    elif horizontal(grid) == 'black':
        s = 2
    elif vertical(grid) == 'white':
        s = 1
    elif vertical(grid) == 'black':
        s = 2
    elif ltrdiagonal(grid) == 'white':
        s = 1
    elif ltrdiagonal(grid) == 'black':
        s = 2
    elif rtldiagonal(grid) == 'white':
        s = 1
    elif rtldiagonal(grid) == 'black':
        s = 2
    elif is_draw(grid):
        s = 3
    return s

def show_win_result(grid):
    s = who_wins(grid)
    if s != 0:
        ss = ""
        if s == 1:
            ss = "White Wins!"
        elif s == 2:
            ss = "Black Wins!"
        else:
            ss == "Draw!"
        tkMessageBox.showinfo("Five in a row",ss)

def is_draw(grid):
    for i in grid:
        for j in i:
            if j == 0:
                return False
    return True

def index_adjacent(x,y):

    surround = [[x - 1,y - 1],[x,y - 1],[x + 1, y - 1],[x - 1,y],[x + 1,y],[x - 1, y + 1],[x,y + 1],[x + 1,y + 1]]
    s1 = grid_copy(surround)

    for i in s1:
        for j in i:
            if j == -1 or j == 19:
                surround.remove(i)
                break
    return surround

def surrounding(grid,x,y):
    lst = []
    for i in index_adjacent(x,y):
        lst.append(grid[i[0]][i[1]])
    if set(lst) != set([0]):
        return True

def play_sound():
    subprocess.call(["afplay","/Users/sam/Desktop/python/GUI/click.wav"])

def play_piece(worb,x,y):
    if worb == 'white':
        canvas.create_oval(x - 17, y - 17, x + 17, y + 17, fill = "white")
    if worb == 'black':
        canvas.create_oval(x - 17, y - 17, x + 17, y + 17, fill = "black")
    t = Timer(0.1,play_sound)
    t.start()

def valid_position(grid,x,y):
    if grid[x][y] == 0:
        return True

def random_spaces(x,y):
    global intersections
    global go_grid

    while True:
        i = random.choice(index_adjacent(x,y))
        if [(i[1] + 1) * 40,(i[0] + 1) * 40] in intersections and valid_position(go_grid,i[0],i[1]):
            return i
        else:
            continue

def how_many_twos(grid):
    y = two_h(grid) + two_v(grid) + two_ltr(grid) + two_rtl(grid)
    return y

def how_many_threes(grid):
    y = three_h(grid) + three_v(grid) + three_ltr(grid) + three_rtl(grid)
    return y

def copy(lst):
    x = []
    for i in lst:
        x.append(i)
    return x

def AI(x,y):
    global go_grid
    global intersections

    h = how_many_twos(go_grid)
    h1 = copy(h)
    h2 = how_many_threes(go_grid)
    h3 = copy(h2)

    if if_two(go_grid) == 0 and if_three(go_grid) == 0:
        return random_spaces(x,y)
#COMPLETE CHECK OF EVERYTHING BELOW HERE
    elif len(is_white_five(go_grid)) == 2:
        return is_white_five(go_grid)

    elif len(is_black_five(go_grid)) == 2:
        return is_black_five(go_grid)

    elif len(is_unblocked_four_white(go_grid)) == 2:
        return is_unblocked_four_white(go_grid)

    elif len(is_unblocked_four_black(go_grid)) == 2:
        return is_unblocked_four_black(go_grid)

    elif len(four_and_three('white',go_grid)) == 2:
        return four_and_three('white',go_grid)

    elif len(four_and_three('black',go_grid)) == 2:
        return four_and_three('black',go_grid)

    elif len(is_double_threes('white',go_grid)) == 2:
        return is_double_threes('white',go_grid)

    elif len(is_double_threes('black',go_grid)) == 2:
        return is_double_threes('black',go_grid)

    elif if_three(go_grid) != 0:
        while True:
            i = random.choice(h3)
            j = blockable_spaces_three(i)

            if valid_position(go_grid,j[0][0],j[0][1]) or valid_position(go_grid,j[1][0],j[1][1]):
                k = random.choice(j)
                if [(k[1] + 1) * 40,(k[0] + 1) * 40] in intersections and valid_position(go_grid,k[0],k[1]):
                    return k
                else:
                    continue
            elif valid_position(go_grid,j[0][0],j[0][1]) != True and valid_position(go_grid,j[1][0],j[1][1]) != True and len(h3) > 1:
                h3.remove(i)
                continue

            elif not valid_position(go_grid,j[0][0],j[0][1]) and not valid_position(go_grid,j[1][0],j[1][1]) and len(h3) == 1:
                return random_spaces(x,y)

    else:
        while True:
            c = random.choice(h1)
            a = blockable_spaces_two(c)

            if valid_position(go_grid,a[0][0],a[0][1]) or valid_position(go_grid,a[1][0],a[1][1]):
                b = random.choice(a)
                if [(b[1] + 1) * 40,(b[0] + 1) * 40] in intersections and valid_position(go_grid,b[0],b[1]):
                    return b
                else:
                    continue
            elif valid_position(go_grid,a[0][0],a[0][1]) != True and valid_position(go_grid,a[1][0],a[1][1]) != True and len(h1) > 1:
                h1.remove(c)
                continue

            elif not valid_position(go_grid,a[0][0],a[0][1]) and not valid_position(go_grid,a[1][0],a[1][1]) and len(h1) == 1:
                return random_spaces(x,y)


def Ai_play(y,x):
    global go_grid

    i = AI(y,x)
    go_grid[i[0]][i[1]] = 1
    play_piece('white',(i[1] + 1) * 40,(i[0] + 1) * 40)
    show_win_result(go_grid)

def play(event):
    global go_grid
    global intersections

    x = grid_rounded(event.x)
    y = grid_rounded(event.y)
    i = 0
    if [rounded(event.x),rounded(event.y)] in intersections:
        if valid_position(go_grid,y,x):
            go_grid[y][x] = 2
            play_piece('black',rounded(event.x),rounded(event.y))
            i = 1
        else:
            if i == 0:
                tkMessageBox.showinfo("go", "Invalid location")
                return
            else:
                tkMessageBox.showinfo("go", "Invalid location")

        if who_wins(go_grid) == 0:
            t = Timer(1.0,Ai_play,[y,x])
            t.start()

        else:
            show_win_result(go_grid)

    else:
        return

def reset(event):
    global go_grid
    canvas.delete("all")
    go_grid = grid_copy(old_grid)
    get_background()
    draw_grid()

canvas.bind("<Button-1>", play)
button1 = Button(root, text = "Reset")
button1.bind("<Button-1>", reset)
button1.pack()

get_background()
draw_grid()

root.mainloop()
