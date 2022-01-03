from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("PIL IMG")

image1 = Image.open("./Pict/keyvisual01.jpg")
image1 = image1.resize((400,559), Image.ANTIALIAS)#(height,widht)
my_img1= ImageTk.PhotoImage(image1)

image2 = Image.open("./Pict/keyvisual02.jpg")
image2 = image2.resize((400,559), Image.ANTIALIAS)#(height,widht)
my_img2= ImageTk.PhotoImage(image2)

image3 = Image.open("./Pict/violet3.jpg")
image3 = image3.resize((640,360), Image.ANTIALIAS)#(height,widht)
my_img3= ImageTk.PhotoImage(image3)

image_list=[my_img1,my_img2,my_img3]

image_number = 0  # current image

status = Label(root, text="pitcure "+str(image_number+1)+" of "+str(len(image_list)), bd=1, relief = RIDGE, anchor= E)

my_label = Label(image=my_img1)
my_label.place(x=0,y=0)

def forward():  # forward button
    global image_number
    image_number+=1 # next photo
    updatelabel()
    
def back():  # back button
    global image_number
    image_number-=1  # previous photo
    updatelabel()
    
def updatelabel():  # show current photo
    my_label.configure(image=image_list[image_number]) # show image
    my_label.image = image_list[image_number]  # prevent garbage collection
    button_forward["state"] = "normal"    
    button_back["state"] = "normal"    
    if image_number == len(image_list)-1: # if last image
       button_forward["state"] = "disabled"
    if image_number == 0:    # if first image
       button_back["state"] = "disabled"

    status = Label(root, text="pitcure "+str(image_number +1) +" of "+str(len(image_list)), bd=1, relief = RIDGE, anchor= E)
    status.grid(row=2,column=0,columnspan=3, sticky= W+E)

button_back = Button(root, text="<<", command= lambda : back())
button_forward = Button(root, text=">>",command= lambda:forward())
button_quit= Button(root,text="Exit",command=root.quit)

button_back.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)

my_label.grid(row=0,column=0,columnspan=3, sticky= W+E)
updatelabel()
root.mainloop()