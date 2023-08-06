import tkinter

import customtkinter
from customtkinter import *

from tkinter import messagebox
from PIL import Image,ImageTk







def main():
    root = CTk()
    root.title("I-mage")
    root.iconbitmap("favicon.ico")
    root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

    # customtkinter.set_appearance_mode("System")
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


    imageFrame = CTkFrame(root, width=680, height=470, bg_color="#121212",border_width=0.6,border_color="#00BB6D")
    imageFrame.place(x=39, y=120)





    resultFrame = CTkFrame(root, width=680, height=470, bg_color="#121212", border_width=1, border_color="#00BB6D")
    resultFrame.place(x=800, y=120)

    arrow = CTkImage(Image.open("arrow_right.png"), size=(40, 40))
    arrow_label = CTkLabel(root, image=arrow, text="",bg_color="transparent")
    arrow_label.place(x=740, y=350)





    uploadPhoto = CTkImage(Image.open("upload.png"), size=(30, 30))
    downloadPhoto = CTkImage(Image.open("download.png"), size=(28, 28))
    logo=CTkImage(Image.open("i-logo.png"),size=(140,60))

    smile=CTkImage(Image.open("smile.png"),size=(20,20))

    # addPhoto=CTkButton(image_label,text="Browse Image",image=editPhoto,compound="right",anchor="end", fg_color="#00A36C")
    # addPhoto.place(x=55,y=32)

    image_label = CTkLabel(imageFrame, text="", width=600, height=400)
    image_label.place(x=38, y=32)

    #Result Image
    result_label = CTkLabel(resultFrame, text="", width=600, height=400)
    result_label.place(x=38, y=32)

    smile = CTkImage(Image.open("smile.png"), size=(20, 20))
    resultText = CTkLabel(result_label, text="Result  ", image=smile, compound="right", font=("Poppins", 16),
                          text_color="#EDEADE")
    resultText.place(x=270, y=200)


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
    addPhoto.place(x=208, y=166)



    generate_Button = CTkButton(root, text="Generate", font=("Poppins", 20), border_width=0, corner_radius=32,
                                fg_color="#00BB6D", width=796, height=40, hover_color="null")
    generate_Button.place(x=360, y=610)

    download_Button = CTkButton(root, text="  Download", font=("Poppins", 20),image=downloadPhoto,compound="right", border_width=1,border_color="#00BB6D", corner_radius=32,
                                fg_color="transparent", width=796, height=40, hover_color="null")
    download_Button.place(x=360, y=666)




#Logo and Navbar
    brand_logo = CTkLabel(root, image=logo,text="")
    brand_logo.place(x=26, y=26)

    itc = CTkButton(root, text="Image-to-Cartoon", font=("Poppins", 14), border_color="#00BB6D",border_width=1,fg_color="transparent",
                     hover_color="null", corner_radius=32)
    itc.place(x=450, y=45)

    itt = CTkButton(root, text="Image-to-Text", font=("Poppins", 14), border_color="#00BB6D",border_width=1,fg_color="transparent",
                       hover_color="null", corner_radius=32)
    itt.place(x=630, y=45)

    bright = CTkButton(root, text="Brightness", font=("Poppins", 14), border_color="#00BB6D",border_width=1,fg_color="transparent",
                        hover_color="null", corner_radius=32)
    bright.place(x=780, y=45)

    blur = CTkButton(root, text="Effect", font=("Poppins", 14), border_color="#00BB6D",border_width=1,fg_color="transparent",
                       hover_color="null", corner_radius=32)
    blur.place(x=930, y=45)

    link=CTkImage(Image.open("link.png"),size=(20,20))
    scanner = CTkButton(root, text="Document Scanner", font=("Poppins", 14),
                     fg_color="#00BB6D",image=link,compound="left",
                     hover_color="null", corner_radius=32)
    scanner.place(x=1280, y=45)

    root.mainloop()