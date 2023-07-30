

import customtkinter
from customtkinter import *

from tkinter import messagebox
from PIL import Image,ImageTk







def main():
    root = CTk()
    root.title("I-mage")
    root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

    customtkinter.set_appearance_mode("System")
    # customtkinter.set_default_color_theme("green")
    # imgLbl=CTkImage(Image.open("R.jpg"),size=(800,800))
    # lbl=CTkLabel(root,image=imgLbl)
    # lbl.pack()
    def addImage():

        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
        if file_path:
            image = Image.open(file_path)
            # image_resize=image.resize((300*3, 300*3), Image.LANCZOS)
            photo = CTkImage(Image.open(file_path), size=(600, 400))

            image_label.configure(image=photo)

            image_label.image = photo
            addPhoto.destroy()
    imageFrame = CTkFrame(root, width=800, height=470, bg_color="#121212")
    imageFrame.place(x=450, y=80)

    uploadPhoto = CTkImage(Image.open("upload.png"), size=(30, 30))
    downloadPhoto = CTkImage(Image.open("download.png"), size=(28, 28))

    # addPhoto=CTkButton(image_label,text="Browse Image",image=editPhoto,compound="right",anchor="end", fg_color="#00A36C")
    # addPhoto.place(x=55,y=32)

    image_label = CTkLabel(imageFrame, text="", width=700, height=300)
    image_label.place(x=55, y=32)

    def saveToDirectory():
        if image_label.image is NONE:
            t = CTkToplevel(root)
            t.title("Alert")

            t.configure(bg="#121212")
            t.transient([root])
            width = 400
            height = 300
            x = (t.winfo_screenwidth() / 2) - (width / 2)
            y = (t.winfo_screenheight() / 2) - (height / 2)
            t.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

            alertLabel1 = CTkLabel(t, text="No Image Available", font=("Poppins", 22), text_color="white",
                                   bg_color="transparent")
            alertLabel1.place(x=120, y=30)
            alertLabel2 = CTkLabel(t, text="Please select your image first", font=("Poppins", 16),
                                   text_color="#777", bg_color="transparent")
            alertLabel2.place(x=120, y=80)
            t.mainloop()
        else:
            print("HEHEH")

    addPhoto = CTkButton(image_label, text="Browse Your Image ", font=("Poppins", 16), image=uploadPhoto,
                         fg_color="transparent", hover_color="null", compound="top", anchor="end", text_color="#EDEADE",
                         corner_radius=32, command=addImage)
    addPhoto.place(x=258, y=166)

    download_Button = CTkButton(root, image=downloadPhoto, text="", bg_color="transparent", fg_color="transparent",
                                hover_color="", width=20, command=saveToDirectory)
    download_Button.place(x=1260, y=500)

    generate_Button = CTkButton(root, text="Generate", font=("Poppins", 20), border_width=0, corner_radius=32,
                                fg_color="#00A36C", width=796, height=40, hover_color="null")
    generate_Button.place(x=450, y=580)

    sideFrame = CTkFrame(root, width=230, height=200, bg_color="#121212")
    # sideFrame.place(x=20,y=30)
    sideFrame.pack(side="left", fill="y", padx='5')

    sideFrame_Label = CTkLabel(sideFrame, text="iMAGE", text_color="#00A36C", font=("Poppins", 22, "bold"))
    sideFrame_Label.place(x=28, y=30)

    home = CTkButton(sideFrame, text="Image-to-Cartoon    ", font=("Poppins", 14), hover_color="#00A36C",
                     bg_color="transparent", fg_color="transparent", corner_radius=32, state=NORMAL)
    home.place(x=12, y=80)

    images = CTkButton(sideFrame, text="Image-to-Text   ", font=("Poppins", 14), hover_color="#00A36C",
                       bg_color="transparent", fg_color="transparent", corner_radius=32)
    images.place(x=12, y=130)

    setting = CTkButton(sideFrame, text="Brightness            ", font=("Poppins", 14), hover_color="#00A36C",
                        bg_color="transparent", fg_color="transparent", corner_radius=32)
    setting.place(x=12, y=180)

    logout = CTkButton(sideFrame, text="Effect                  ", font=("Poppins", 14), hover_color="#00A36C",
                       bg_color="transparent", fg_color="transparent", corner_radius=32)
    logout.place(x=12, y=230)

    root.mainloop()