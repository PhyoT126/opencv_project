import tkinter
from tkinter import *
import time

from customtkinter import *
from PIL import Image,ImageTk
from MainPage import main


root=Tk()
root.title("i-Mage")
root.iconbitmap("Image/favicon.ico")
root.configure(bg="#181818")
width=600
height=400
x=(root.winfo_screenwidth()/2)-(width/2)
y=(root.winfo_screenheight()/2)-(height/2)
root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
root.resizable(width=FALSE,height=FALSE)


def new_win():


    root = CTk()
    root.title("i-Mage")
    root.iconbitmap("Image/favicon.ico")
    width = 900
    height = 600
    x = (root.winfo_screenwidth() / 2) - (width / 2)
    y = (root.winfo_screenheight() / 2) - (height / 2)
    root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
    root.resizable(width=FALSE, height=FALSE)

    backImage = CTkImage(Image.open("Image/landing_bg.png"), size=(900, 600))
    main_Canva = CTkLabel(root, image=backImage, text="")
    main_Canva.pack()
    brand = CTkImage(Image.open("Image/i-logo.png"), size=(190, 78))

    w_Frame = CTkFrame(master=main_Canva, width=500, height=350, bg_color="#2B2B2B", border_width=1,
                       border_color="#00A36C", corner_radius=12)
    w_Frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    logo = CTkLabel(master=w_Frame, image=brand, text="")
    logo.place(x=160, y=10)

    header = CTkLabel(master=w_Frame, text="Welcome", font=("Poppins", 38, "bold"), bg_color="transparent",
                      text_color="#ffffff")
    header.place(x=160, y=120)

    subHeader = CTkLabel(master=w_Frame,
                         text=" A program to provide image processing services\n for a wide range of users",
                         font=("Poppins", 16), text_color="#ffffff")

    subHeader.place(x=50, y=184)
    def goToMain():
        root.destroy()
        main()

    startButton = CTkButton(master=w_Frame, text="Get Started", fg_color="#00A36C", width=160, height=50,
                            font=("Poppins", 16), hover_color="#00A36C",command=goToMain)
    startButton.place(x=175, y=260)

    root.mainloop()


Frame(root,width=800,height=600,bg="#181818").place(x=0,y=0)
brand=CTkImage(Image.open("Image/i-logo.png"), size=(350, 130))
logo=CTkLabel(master=root,image=brand,text="")
logo.place(x=126,y=80)


loading=Label(master=root,text="loading...",bg='#181818',fg="white",font=("Poppins", 16))
loading.place(x=20,y=350)

image_a=ImageTk.PhotoImage(Image.open("Image/c1.png"), size=(70, 70))
image_b=ImageTk.PhotoImage(Image.open("Image/c2.png"), size=(70, 70))

# for i in range(2):
#     i1=Label(bg,text="",image=image_a,bg="#181818").place(x=240,y=200)
#     i2 =Label(bg, text="", image=image_b,bg="#181818").place(x=270, y=200)
#     i3 = Label(bg, text="", image=image_b,bg="#181818").place(x=300, y=200)
#     i4 = Label(bg, text="", image=image_b,bg="#181818").place(x=330, y=200)
#     root.update_idletasks()
#     time.sleep(0.5)
#
#     i1 = Label(bg, text="", image=image_b, bg="#181818").place(x=240, y=200)
#     i2 = Label(bg, text="", image=image_a, bg="#181818").place(x=270, y=200)
#     i3 = Label(bg, text="", image=image_b, bg="#181818").place(x=300, y=200)
#     i4 = Label(bg, text="", image=image_b, bg="#181818").place(x=330, y=200)
#     root.update_idletasks()
#     time.sleep(0.5)
#
#     i1 = Label(bg, text="", image=image_b, bg="#181818").place(x=240, y=200)
#     i2 = Label(bg, text="", image=image_b, bg="#181818").place(x=270, y=200)
#     i3 = Label(bg, text="", image=image_a, bg="#181818").place(x=300, y=200)
#     i4 = Label(bg, text="", image=image_b, bg="#181818").place(x=330, y=200)
#     root.update_idletasks()
#     time.sleep(0.5)
#
#     i1 = Label(bg, text="", image=image_b, bg="#181818").place(x=240, y=200)
#     i2 = Label(bg, text="", image=image_b, bg="#181818").place(x=270, y=200)
#     i3 = Label(bg, text="", image=image_b, bg="#181818").place(x=300, y=200)
#     i4 = Label(bg, text="", image=image_a, bg="#181818").place(x=330, y=200)
#     root.update_idletasks()
#     time.sleep(0.5)
for i in range(2):
    i1=Label(root,text="",image=image_a,bg="#181818").place(x=250,y=220)
    i2 =Label(root, text="", image=image_b,bg="#181818").place(x=280, y=220)
    i3 = Label(root, text="", image=image_b,bg="#181818").place(x=310, y=220)
    i4 = Label(root, text="", image=image_b,bg="#181818").place(x=340, y=220)
    root.update_idletasks()
    time.sleep(0.5)

    i1 = Label(root, text="", image=image_b, bg="#181818").place(x=250, y=220)
    i2 = Label(root, text="", image=image_a, bg="#181818").place(x=280, y=220)
    i3 = Label(root, text="", image=image_b, bg="#181818").place(x=310, y=220)
    i4 = Label(root, text="", image=image_b, bg="#181818").place(x=340, y=220)
    root.update_idletasks()
    time.sleep(0.5)

    i1 = Label(root, text="", image=image_b, bg="#181818").place(x=250, y=220)
    i2 = Label(root, text="", image=image_b, bg="#181818").place(x=280, y=220)
    i3 = Label(root, text="", image=image_a, bg="#181818").place(x=310, y=220)
    i4 = Label(root, text="", image=image_b, bg="#181818").place(x=340, y=220)
    root.update_idletasks()
    time.sleep(0.5)

    i1 = Label(root, text="", image=image_b, bg="#181818").place(x=250, y=220)
    i2 = Label(root, text="", image=image_b, bg="#181818").place(x=280, y=220)
    i3 = Label(root, text="", image=image_b, bg="#181818").place(x=310, y=220)
    i4 = Label(root, text="", image=image_a, bg="#181818").place(x=340, y=220)
    root.update_idletasks()
    time.sleep(0.5)


root.destroy()
new_win()
root.mainloop()

