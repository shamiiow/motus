from tkinter import *
from random import randint

main = Tk()
main.title("motus")
main.geometry("531x531")

long = 3

list = [[f'{i}{j}' for j in range(long+2)] for i in range(long+2)]

for i in range(long+2):
    list[0][i], list[long + 1][i], list[i][0], list[i][long + 1] = 100, 100, 100, 100

img = {}
for i in range(long):
    for j in range(long):
        img[f"{i+1}{j+1}"] = PhotoImage(file = f"img/{i}{j}.png")


def update():
    for i in range(long):
        for j in range(long):
            button[i][j].config(image=img[f"{list[i+1][j+1]}"])
    print("-"*25)
    for i in range(long + 2):
        print(list[i])


button = [[0 for j in range(long)] for i in range(long)]

# melange
Vi = []

for i in range(long):
    for j in range(long):
        cx = randint(0, 2) + 1
        cy = randint(0, 2) + 1
        if (cx, cy) not in Vi:
            list[i+1][j+1], list[cx][cy] = list[cx][cy], list[i+1][j+1]
            Vi.append((cx, cy))


def move(e, coord):
    x = int(coord[0])
    y = int(coord[1])
    for i in [-1, 1]:
        for j in [-1, 1]:
            if list[x + i][y] == "11":
                list[x][y], list[x + i][y] = list[x + i][y], list[x][y]
            if list[x][y+j] == "11":
                list[x][y], list[x][y+j] = list[x][y+j], list[x][y]

    update()
    check_win()


def check_win():
    for i in range(1, long+1):
        for j in range(1, long+1):
            if list[i][j] != f"{i}{j}":
                return
    print("bravo")


for i in range(long):
    for j in range(long):
        button[i][j] = Button(main, image = img[f"{i+1}{j+1}"], command=lambda e=None, coord=f"{i+1}{j+1}": move(e, coord))
        button[i][j].grid(row=i, column=j)
update()


main.mainloop()
