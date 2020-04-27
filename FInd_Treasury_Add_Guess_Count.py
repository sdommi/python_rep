from tkinter import *
import random
window = Tk()
x_coord = random.randint(0,200)
y_coord = random.randint(0,200)
button_counter=1
counter = 0


def guess_treasure(event):
    global counter
    counter +=1
    if counter >10:
        global  button_counter
        if button_counter == 1:
            button = Button(window,text="Parraot Search",bg="Red")
            button.bind("<Button-1>",parraot)
            button.pack()

    print("You Clicked at x:{} and y:{}. you are {} away from x and {} away from y".
          format(event.x,event.y,abs(event.x-x_coord),abs(event.y-y_coord)))
    if abs(event.x-x_coord) <20 and abs(event.y-y_coord) <20:
        print("Hurrry You found the Ttreasareeeeeee..Yar")
        Welcome_label.config(text="You found the treasary in{} clicks".format(text=counter))
def parraot(event):
    print("Parraot Search")
    global button_counter
    button_counter -=1
    print("You Clicked at x:{} and y:{}. you are {} away from x and {} away from y".
          format(event.x, event.y, abs(event.x - x_coord), abs(event.y - y_coord)))
    if abs(event.x - x_coord) < 20 and abs(event.y - y_coord) < 20:
        print("Hurrry You found the Ttreasareeeeeee..Yar")
        Welcome_label.config(text="You found the treasary in{} clicks".format(text=counter))

frame = Frame(window,bg="orange",height=200,width=200)
frame.bind("<Button-1>",guess_treasure)
Welcome_label = Label(window,text="PLease click on the map and  search for treasury",bg="yellow")
Welcome_label.pack()
frame.pack()
window.mainloop()
