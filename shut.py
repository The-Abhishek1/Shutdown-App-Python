from tkinter import  *
import os   

root = Tk()
root.title()
root.geomtry("400x580")

#First button 
restart_time_button = PhotoImage(file="restart time.png")

first_button =Button(root,image=restart_time_button,borderwidth=0,cursor="hand2")
first_button.place(x=10,y=10)

#Second button
close_button = PhotoImage(file="close.png")

second_button = Button(root,image=close_button,borderwidth=0,cursor="hand2")
second_button.place(x=200,y=10)

root.mainloop()