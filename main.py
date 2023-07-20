import tkinter

from customtkinter import *
from PIL import Image, ImageTk

root = CTk()
root.geometry('600x600')
root.resizable(width=False, height=False)


imgL=CTkImage(Image.open('R.jpg'),size=(600,600))
l1=CTkLabel(root,image=imgL)
l1.pack()

loginFrame = CTkFrame(master=l1, width=300, height=200, corner_radius=12)
loginFrame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
label = CTkLabel(master=loginFrame, text="Login Form")
label.place(x=93, y=10)
e1 = CTkEntry(master=loginFrame, placeholder_text='Username', width=200)
e1.place(x=46, y=50)
e2 = CTkEntry(master=loginFrame, placeholder_text='Password', width=200)
e2.place(x=46, y=96)

    # def main():
    #     loginFrame.destroy()
    #     label.destroy()
    #     e1.destroy()
    #     e2.destroy()
    #     s.destroy()
    #     l2 = CTkLabel(master=l1, text="Welcome", text_color="white")
    #     l2.pack()
    #
    #     def back():
    #         l2.destroy()
    #         b1.destroy()
    #         home()
    #
    #     b1 = CTkButton(master=l1, text="Back",command=back)
    #     b1.pack(pady=20, padx=10)

s = CTkButton(master=loginFrame, text='Submit',command=root.quit)
s.place(x=76, y=137)




root.mainloop()
