import tkinter

from customtkinter import *
from PIL import Image, ImageTk

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

w_Frame=CTkFrame(master=main_Canva,width=500,height=260,bg_color="#2B2B2B",border_width=1,border_color="#00A36C",corner_radius=12)
w_Frame.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)


header = CTkLabel(master=w_Frame, text="Welcome", font=("Poppins", 38, "bold"), bg_color="transparent",
                  text_color="#ffffff")
header.place(x=155,y=30)

subHeader = CTkLabel(master=w_Frame, text=" A program to provide image processing services\n for a wide range of users",font=("Poppins", 16) ,text_color="#ffffff")

subHeader.place(x=50,y=88)






startButton = CTkButton(master=w_Frame, text="Get Started", fg_color="#00A36C", width=160, height=50,
                        font=("Poppins", 16), hover_color="#00A36C")
startButton.place(x=170, y=166)

root.mainloop()
