from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Calculator")

label_1 = Label(root,text="Enter your numbers")
label_1.pack(pady=20)


entry_1 = Entry(root)
entry_1.pack(pady=10)

entry_2 = Entry(root)
entry_2.pack(pady=10)

def add ():
    number_1 = int(entry_1.get())
    number_2 = int(entry_2.get())
    result = number_1+number_2
    label_3.config(text="Result:"+str(result))

b1 = Button(root,text = "Add",bg="light green",command= add)
b1.pack(pady=10)



label_3 = Label(root,text="Result:")
label_3.pack(pady=10)

root.mainloop()