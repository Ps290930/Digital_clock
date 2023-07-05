from tkinter import Tk
from tkinter import Label
from time import strftime

clock=Tk()
clock.title("Digital clock")
clock.focus_displayof()

def disp_time():
    st=strftime("%I : %M : %S : %p")
    disp.config(text=st)
    disp.after(1000,disp_time)

disp=Label(clock,font=("calibri",80),bg="White",fg="black")
disp.pack(anchor="center")
disp_time()

disp.mainloop()