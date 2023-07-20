import tkinter

import customtkinter
from customtkinter import *


from PIL import Image,ImageTk

def checkState():
    Click_home = CTkButton(sideFrame, text="Black and white     ", bg_color="transparent",
                     fg_color="#00A36C", corner_radius=32,command=checkState)
    Click_home.place(x=12, y=80)
def addImage():


    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
    if file_path:
        image = Image.open(file_path)
        # image_resize=image.resize((300*3, 300*3), Image.LANCZOS)
        photo = CTkImage(Image.open(file_path),size=(600,400))

        image_label.configure(image=photo)

        image_label.image = photo
        addPhoto.destroy()


root=CTk()
root.title("I-mage")
root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))



customtkinter.set_appearance_mode("System")
# customtkinter.set_default_color_theme("green")
# imgLbl=CTkImage(Image.open("R.jpg"),size=(800,800))
# lbl=CTkLabel(root,image=imgLbl)
# lbl.pack()


imageFrame = CTkFrame(root, width=800, height=470, bg_color="#121212")
imageFrame.place(x=450,y=80)

editPhoto=CTkImage(Image.open("../pracitce/edit.png"), size=(20, 20))
# addPhoto=CTkButton(image_label,text="Browse Image",image=editPhoto,compound="right",anchor="end", fg_color="#00A36C")
# addPhoto.place(x=55,y=32)

image_label=CTkLabel(imageFrame, text="", width=700, height=300)
image_label.place(x=55,y=32)

addPhoto=CTkButton(image_label,text="Browse Image  ",image=editPhoto,compound="right",anchor="end", fg_color="#00A36C",text_color="black",corner_radius=32,hover_color="#00A36C",command=addImage)
addPhoto.place(x=268,y=176)

sideFrame=CTkFrame(root,width=200,height=200,bg_color="#121212")
# sideFrame.place(x=20,y=30)
sideFrame.pack(side="left",fill="y",padx='5')

sideFrame_Label=CTkLabel(sideFrame,text="Control Panel",text_color="#00A36C",font=("Inter",18))
sideFrame_Label.place(x=28,y=30)

home=CTkButton(sideFrame,text="Black and white     ",hover_color="#00A36C",bg_color="transparent",fg_color="transparent",corner_radius=32,state=NORMAL)
home.place(x=12,y=80)

images=CTkButton(sideFrame,text="Filter                         ",hover_color="#00A36C",command=addImage,bg_color="transparent",fg_color="transparent",corner_radius=32)
images.place(x=12,y=130)


setting=CTkButton(sideFrame,text="Brightness                 ",hover_color="#00A36C",bg_color="transparent",fg_color="transparent",corner_radius=32)
setting.place(x=12,y=180)

logout=CTkButton(sideFrame,text="Effect                        ",hover_color="#00A36C",bg_color="transparent",fg_color="transparent",corner_radius=32)
logout.place(x=12,y=230)






root.mainloop()