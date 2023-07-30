import tkinter
from tkinter import *
import time

from customtkinter import *
from PIL import Image,ImageTk
from switch_test import main


root=Tk()
root.title("Splash")
root.configure(bg="#181818")
width=600
height=400
x=(root.winfo_screenwidth()/2)-(width/2)
y=(root.winfo_screenheight()/2)-(height/2)
root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
root.resizable(width=FALSE,height=FALSE)


def new_win():


    root = CTk()
    width = 900
    height = 600
    x = (root.winfo_screenwidth() / 2) - (width / 2)
    y = (root.winfo_screenheight() / 2) - (height / 2)
    root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
    root.resizable(width=FALSE, height=FALSE)

    backImage = CTkImage(Image.open("landing_bg.png"), size=(900, 600))
    main_Canva = CTkLabel(root, image=backImage, text="")
    main_Canva.pack()

    w_Frame = CTkFrame(master=main_Canva, width=500, height=260, bg_color="#2B2B2B", border_width=1,
                       border_color="#00A36C", corner_radius=12)
    w_Frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    header = CTkLabel(master=w_Frame, text="Welcome", font=("Poppins", 38, "bold"), bg_color="transparent",
                      text_color="#ffffff")
    header.place(x=155, y=30)

    subHeader = CTkLabel(master=w_Frame,
                         text=" A program to provide image processing services\n for a wide range of users",
                         font=("Poppins", 16), text_color="#ffffff")

    subHeader.place(x=50, y=88)
    def goToMain():
        root.destroy()
        main()

    startButton = CTkButton(master=w_Frame, text="Get Started", fg_color="#00A36C", width=160, height=50,
                            font=("Poppins", 16), hover_color="#00A36C",command=goToMain)
    startButton.place(x=170, y=166)

    root.mainloop()


Frame(root,width=800,height=600,bg="#181818").place(x=0,y=0)
l=Label(root,text="I-Mage",bg='#181818',fg="#06D37D",font=("Poppins",50,"bold"))
l.place(x=170,y=80)


loading=Label(root,text="loading...",bg='#181818',fg="white",font=("Poppins", 16))
loading.place(x=20,y=350)

image_a=ImageTk.PhotoImage(Image.open("c1.png"),size=(130,130))
image_b=ImageTk.PhotoImage(Image.open("c2.png"),size=(130,130))

for i in range(2):
    i1=Label(root,text="",image=image_a,bg="#181818").place(x=240,y=200)
    i2 =Label(root, text="", image=image_b,bg="#181818").place(x=270, y=200)
    i3 = Label(root, text="", image=image_b,bg="#181818").place(x=300, y=200)
    i4 = Label(root, text="", image=image_b,bg="#181818").place(x=330, y=200)
    root.update_idletasks()
    time.sleep(0.5)

    i1 = Label(root, text="", image=image_b, bg="#181818").place(x=240, y=200)
    i2 = Label(root, text="", image=image_a, bg="#181818").place(x=270, y=200)
    i3 = Label(root, text="", image=image_b, bg="#181818").place(x=300, y=200)
    i4 = Label(root, text="", image=image_b, bg="#181818").place(x=330, y=200)
    root.update_idletasks()
    time.sleep(0.5)

    i1 = Label(root, text="", image=image_b, bg="#181818").place(x=240, y=200)
    i2 = Label(root, text="", image=image_b, bg="#181818").place(x=270, y=200)
    i3 = Label(root, text="", image=image_a, bg="#181818").place(x=300, y=200)
    i4 = Label(root, text="", image=image_b, bg="#181818").place(x=330, y=200)
    root.update_idletasks()
    time.sleep(0.5)

    i1 = Label(root, text="", image=image_b, bg="#181818").place(x=240, y=200)
    i2 = Label(root, text="", image=image_b, bg="#181818").place(x=270, y=200)
    i3 = Label(root, text="", image=image_b, bg="#181818").place(x=300, y=200)
    i4 = Label(root, text="", image=image_a, bg="#181818").place(x=330, y=200)
    root.update_idletasks()
    time.sleep(0.5)



root.destroy()
new_win()
root.mainloop()

