from tkinter import *
window = Tk()
def draw_oval(event):
    canvas.create_rectangle(event.x,event.y,event.x+20,event.y+20,fill="green")

Wel_label = Label(window,text ="Click and hold the mouse to draw",fg="blue",bg="orange")
Wel_label.pack(fill=X)
canvas = Canvas(window,width=500,height=300)
canvas.bind("<Button-1>",draw_oval)
canvas. bind("<B1-Motion>",draw_oval)
canvas.pack()
window.mainloop()
