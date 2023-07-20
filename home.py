import tkinter
from tkinter import *
import time

# from customtkinter import *
from PIL import Image,ImageTk


root=Tk()
root.title("Splash")
root.configure(bg="#181818")
width=600
height=400
x=(root.winfo_screenwidth()/2)-(width/2)
y=(root.winfo_screenheight()/2)-(height/2)
root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")


def new_win():
    q=Tk()
    q.title("Main Page")
    q.mainloop()

Frame(root,width=800,height=600,bg="#181818").place(x=0,y=0)
l=Label(root,text="iMAGE",bg='#181818',fg="#06D37D",font=("Poppins",50))
l.place(x=200,y=70)


loading=Label(root,text="loading...",bg='#181818',fg="white",font=("Poppins", 18))
loading.place(x=24,y=320)

image_a=ImageTk.PhotoImage(Image.open("c1.png"),size=(130,130))
image_b=ImageTk.PhotoImage(Image.open("c2.png"),size=(130,130))

for i in range(5):
    i1=Label(root,text="",image=image_a,bg="#181818").place(x=240,y=160)
    i2 =Label(root, text="", image=image_b,bg="#181818").place(x=270, y=160)
    i3 = Label(root, text="", image=image_b,bg="#181818").place(x=300, y=160)
    i4 = Label(root, text="", image=image_b,bg="#181818").place(x=330, y=160)
    root.update_idletasks()
    time.sleep(0.5)

    i1 = Label(root, text="", image=image_b, bg="#181818").place(x=240, y=160)
    i2 = Label(root, text="", image=image_a, bg="#181818").place(x=270, y=160)
    i3 = Label(root, text="", image=image_b, bg="#181818").place(x=300, y=160)
    i4 = Label(root, text="", image=image_b, bg="#181818").place(x=330, y=160)
    root.update_idletasks()
    time.sleep(0.5)

    i1 = Label(root, text="", image=image_b, bg="#181818").place(x=240, y=160)
    i2 = Label(root, text="", image=image_b, bg="#181818").place(x=270, y=160)
    i3 = Label(root, text="", image=image_a, bg="#181818").place(x=300, y=160)
    i4 = Label(root, text="", image=image_b, bg="#181818").place(x=330, y=160)
    root.update_idletasks()
    time.sleep(0.5)

    i1 = Label(root, text="", image=image_b, bg="#181818").place(x=240, y=160)
    i2 = Label(root, text="", image=image_b, bg="#181818").place(x=270, y=160)
    i3 = Label(root, text="", image=image_b, bg="#181818").place(x=300, y=160)
    i4 = Label(root, text="", image=image_a, bg="#181818").place(x=330, y=160)
    root.update_idletasks()
    time.sleep(0.5)



root.destroy()
new_win()
root.mainloop()

