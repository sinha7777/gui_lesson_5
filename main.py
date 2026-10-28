from tkinter import *
import calendar


root = Tk()
root.title("Calendar")

def show_calendar():
    root_1 = Tk()
    root_1.title("Calendar")
    root_1.geometry("800x800")
    root_1.config(bg="white")
    year = int(year_entry.get())
    content = calendar.calendar(year)
    label_3 = Label(root_1,text= content,font=("Courier New",10),justify=LEFT,anchor="nw",bg="white")
    label_3.grid(row = 0,column=0,padx=20,pady=20,sticky="nw")
    root_1.mainloop()
    

label_1 = Label(root,text="CALENDAR",bg="grey")
label_1.grid(row = 1,column=1)

label_2 = Label(root,text="Enter Year",bg="light green")
label_2.grid(row=2,column=1)

year_entry = Entry(root)
year_entry.grid(row=3,column=1)

b1= Button(root,text="Show Calendar",bg="red",command= show_calendar)
b1.grid(row=4,column=1)

b2 = Button(root,text="Exit",bg="red",command=root.destroy)
b2.grid(row=5,column=1)


root.mainloop()