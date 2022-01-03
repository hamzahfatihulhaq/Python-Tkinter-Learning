from tkinter import*

root =Tk()
root.title("Besic Calculator")

entryCal = Entry(root, width=45, borderwidth=5)
entryCal.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
f_num = 0
math = ""
def button_click(number):
    current = entryCal.get()
    entryCal.delete(0, END)
    entryCal.insert(0, str(current) + str(number))

def button_clears():
    entryCal.delete(0,END)

def button_adds():
    first_number = entryCal.get()
    global f_num, math
    math = "addition"
    if type(f_num) == float:
        f_num = float(first_number)
    else :
        f_num = int(first_number)
    entryCal.delete(0, END)

def button_equals():
    second_number = entryCal.get()
    entryCal.delete(0,END)
    global f_num
    if math == "addition":
        entryCal.insert(0, f_num + int(second_number))

    if math == "substract":
        entryCal.insert(0, f_num - int(second_number))

    if math == "multiply":
        entryCal.insert(0, f_num * int(second_number))

    if math == "division":
        f_num =f_num / int(second_number)
        entryCal.insert(0, f_num )

def button_substracts():
    first_number = entryCal.get()
    global f_num, math
    math = "substract"
    if type(f_num) == float:
        f_num = float(first_number)
    else :
        f_num = int(first_number)
    entryCal.delete(0, END)

def button_multiplys():
    first_number = entryCal.get()
    global f_num, math
    math = "multiply"
    if type(f_num) == float:
        f_num = float(first_number)
    else :
        f_num = int(first_number)
    entryCal.delete(0, END)

def button_divisions():
    first_number = entryCal.get()
    global f_num, math
    math = "division"
    if type(f_num) == float:
        f_num = float(first_number)
    else :
        f_num = int(first_number)
    entryCal.delete(0, END)

# define buttom
button_1=Button(root, text="1",padx=40,pady=20,command=lambda: button_click(1))
button_2=Button(root, text="2",padx=40,pady=20,command=lambda: button_click(2))
button_3=Button(root, text="3",padx=40,pady=20,command=lambda: button_click(3))
button_4=Button(root, text="4",padx=40,pady=20,command=lambda: button_click(4))
button_5=Button(root, text="5",padx=40,pady=20,command=lambda: button_click(5))
button_6=Button(root, text="6",padx=40,pady=20,command=lambda: button_click(6))
button_7=Button(root, text="7",padx=40,pady=20,command=lambda: button_click(7))
button_8=Button(root, text="8",padx=40,pady=20,command=lambda: button_click(8))
button_9=Button(root, text="9",padx=40,pady=20,command=lambda: button_click(9))
button_0=Button(root, text="0",padx=40,pady=20,command=lambda: button_click(0))
button_add=Button(root, text="+",padx=50,pady=20,command=button_adds)
button_equal = Button(root, text="=",padx=38,pady=20,command=button_equals)
button_clear = Button(root, text="Clear",padx=40,pady=20,command=button_clears)

button_substract=Button(root, text="-",padx=53,pady=20,command=button_substracts)
button_multiply=Button(root, text="x",padx=53,pady=20,command=button_multiplys)
button_division=Button(root, text="/",padx=42,pady=20,command=button_divisions)

# put the button on the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=1,column=3)
button_add.grid(row=2,column=3)
button_substract.grid(row=3,column=3)
button_multiply.grid(row=4,column=3)
button_division.grid(row=4,column=2)
button_equal.grid(row=4,column=1)
root.mainloop()