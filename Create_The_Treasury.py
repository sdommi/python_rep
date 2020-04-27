from tkinter import *
import random
window = Tk()
def guess_coor(event):
    print("You clicked at x:{} and y:{}. You are {} away from x and {} away from y".
          format(event.x,event.y,abs(event.x-x_coor),abs(event.y-y_coor)))
    if abs(event.x-x_coor) < 10 and  abs(event.y - y_coor) < 25:
        print("YOU HAVE FOUND THE TREASUREE YAR!!!")
        welcome_label.config(text="You Have Won!!")

x_coor= random.randint(0,200)
y_coor = random.randint(0,200)
frame =Frame(window,height=200,width=200,bg="orange")
welcome_label = Label(window,text="Please click on the map to search for a measure",fg="blue",bg="yellow")
welcome_label.pack()
frame.bind("<Button-1>",guess_coor)
frame.pack()
window.mainloop()
