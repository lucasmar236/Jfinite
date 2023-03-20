from tkinter import *

root = Tk()
canvas = Canvas(root, width=800, height=600)

countQ = 0

x = 0
y = 0
click = False
line = canvas.create_line(x,y,x,y)

def onButtonRelease(event):
    global x,y,click
    click = False
    canvas.create_line(x,y,event.x,event.y)
    canvas.pack()

def onButtonClick(event):
    global x,y,click
    click = True
    x = event.x
    y = event.y

def onMotion(event):
    global x, y, line,click
    if click:
        canvas.delete(line)
        line = canvas.create_line(x,y,event.x,event.y)
        canvas.pack()

def on_click(event):
    global x,y,countQ
    x = event.x
    y = event.y
    canvas.create_oval(event.x - 25, event.y - 25, event.x + 25, event.y + 25, width=1, fill="yellow")
    Label(root, text="q" + str(countQ), bg="yellow", fg="black").place(x=event.x - 10, y=event.y - 10)
    countQ += 1

    canvas.pack()

canvas.bind("<Motion>",onMotion)
canvas.bind("<Button-3>", on_click)
canvas.bind("<Button-1>", onButtonClick)
canvas.bind("<ButtonRelease-1>", onButtonRelease)
canvas.pack()

root.mainloop()
