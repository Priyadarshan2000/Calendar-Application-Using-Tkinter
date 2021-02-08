# priyadarshan Ghosh
from tkinter import *
from tkcalendar import *
win=Tk()
win.geometry("200x200")
win.title("Calendar")
win.configure(bg="yellow")
def calendar():
    def grabdate():
        global date1
        date1=cal.get_date()
        top.destroy()
        Label(win,text="Date Selected",fg="green",font=("elephant",11)).pack()
        Label(win,text=date1,fg="green",font=("elephant",11)).pack()
    top=Toplevel(win)
    cal=Calendar(top,selectmode="day",year=2020,month=7,day=11)
    cal.pack()
    cbutton=Button(top,text="OK",command=grabdate).pack()
Label(win,text="Select Date",font=("calibri",20)).pack()
Button(win,text="See Calendar",command=calendar).pack(padx=10,pady=10)
win.mainloop()