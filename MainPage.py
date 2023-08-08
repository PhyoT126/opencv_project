import tkinter


import customtkinter
from PIL.ImageTk import PhotoImage
from customtkinter import *

from tkinter import messagebox
from PIL import Image, ImageTk




def main():
    root = CTk()
    root.title("I-mage")
    root.iconbitmap("Image/favicon.ico")
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

    imageFrame = CTkFrame(root, width=680, height=470, bg_color="#121212", border_width=0.6, border_color="#00BB6D")
    imageFrame.place(x=39, y=120)

    resultFrame = CTkFrame(root, width=680, height=470, bg_color="#121212", border_width=1, border_color="#00BB6D")
    resultFrame.place(x=800, y=120)

    arrow = CTkImage(Image.open("Image/arrow_right.png"), size=(40, 40))
    arrow_label = CTkLabel(root, image=arrow, text="", bg_color="transparent")
    arrow_label.place(x=740, y=350)

    uploadPhoto = CTkImage(Image.open("Image/upload.png"), size=(30, 30))
    downloadPhoto = CTkImage(Image.open("Image/download.png"), size=(22, 22))
    logo = CTkImage(Image.open("Image/i-logo.png"), size=(140, 50))

    smile = CTkImage(Image.open("Image/smile.png"), size=(20, 20))

    # addPhoto=CTkButton(image_label,text="Browse Image",image=editPhoto,compound="right",anchor="end", fg_color="#00A36C")
    # addPhoto.place(x=55,y=32)

    image_label = CTkLabel(imageFrame, text="", width=600, height=400)
    image_label.place(x=38, y=32)

    # Result Image
    result_label = CTkLabel(resultFrame, text="", width=600, height=400)
    result_label.place(x=38, y=32)

    smile = CTkImage(Image.open("Image/smile.png"), size=(20, 20))
    resultText = CTkLabel(result_label, text="Result  ", image=smile, compound="right", font=("Poppins", 16),
                          text_color="#EDEADE")
    resultText.place(x=270, y=200)

    def saveToDirectory():
        if not image_label.cget("image"):
            t = CTkToplevel(root)
            t.title("Alert")

            t.iconbitmap("favicon.ico")

            t.configure(bg="#121212")
            t.transient([root])

            width = 380
            height = 220
            x = t.winfo_screenwidth() // 2 - width // 2
            y = t.winfo_screenheight() // 2 - height // 2
            t.geometry(f"{width}x{height}+{x+120}+{y}")

            t.resizable(width=False,height=False)
            icon=CTkImage(Image.open("Image/sad.png"),size=(30,30))
            alertIcon=CTkLabel(t,image=icon,text="")
            alertIcon.place(x=180,y=18)

            alertLabel1 = CTkLabel(t, text="Sorry!Can't Download", font=("Poppins", 22), text_color="#00BB6D",
                                   bg_color="transparent")
            alertLabel1.place(x=74, y=60)
            alertLabel2 = CTkLabel(t, text="Please choose your image first", font=("Poppins", 16),
                                   text_color="#777", bg_color="transparent")
            alertLabel2.place(x=70, y=100)

            closeButton=CTkButton(t,text="Ok",fg_color="transparent",hover_color="null",border_color="#00BB6D",border_width=1,command=t.destroy)
            closeButton.place(x=125,y=150)

            t.mainloop()
        if not result_label.cget("image"):
            t = CTkToplevel(root)
            t.title("Alert")

            t.iconbitmap("Image/favicon.ico")

            t.configure(bg="#121212")
            t.transient([root])

            width = 380
            height = 220
            x = t.winfo_screenwidth() // 2 - width // 2
            y = t.winfo_screenheight() // 2 - height // 2
            t.geometry(f"{width}x{height}+{x+120}+{y}")

            t.resizable(width=False,height=False)
            icon=CTkImage(Image.open("Image/sad.png"),size=(30,30))
            alertIcon=CTkLabel(t,image=icon,text="")
            alertIcon.place(x=180,y=18)

            alertLabel1 = CTkLabel(t, text="Sorry!Can't Download", font=("Poppins", 22), text_color="#00BB6D",
                                   bg_color="transparent")
            alertLabel1.place(x=74, y=60)
            alertLabel2 = CTkLabel(t, text="Please generate your image first", font=("Poppins", 16),
                                   text_color="#777", bg_color="transparent")
            alertLabel2.place(x=65, y=100)

            closeButton=CTkButton(t,text="Ok",fg_color="transparent",hover_color="null",border_color="#00BB6D",border_width=1,command=t.destroy)
            closeButton.place(x=125,y=150)

            t.mainloop()
        elif result_label.cget("image"):
            e=StringVar()
            name=filedialog.asksaveasfilename(typevariable=e,initialfile="All files",filetypes=["Image Type","*.jpg;*.png"],title="Choose directory")
            if result_label.image:
                result_label.image.save(name)

    addPhoto = CTkButton(image_label, text="Browse Your Image ", font=("Poppins", 16), image=uploadPhoto,
                         fg_color="transparent", hover_color="null", compound="top", anchor="end", text_color="#EDEADE",
                         corner_radius=32, command=addImage)
    addPhoto.place(x=208, y=166)

    def generateImage():
        if not image_label.cget("image"):
            t = CTkToplevel(root)
            t.title("Alert")

            t.iconbitmap("Image/favicon.ico")

            t.configure(bg="#121212")
            t.transient([root])

            width = 380
            height = 220
            x = t.winfo_screenwidth() // 2 - width // 2
            y = t.winfo_screenheight() // 2 - height // 2
            t.geometry(f"{width}x{height}+{x + 120}+{y}")

            t.resizable(width=False, height=False)

            icon = CTkImage(Image.open("Image/sad.png"), size=(30, 30))
            alertIcon = CTkLabel(t, image=icon, text="")
            alertIcon.place(x=180, y=18)

            alertLabel1 = CTkLabel(t, text="Sorry!Can't Generate", font=("Poppins", 22), text_color="#00BB6D",
                                   bg_color="transparent")
            alertLabel1.place(x=74, y=60)
            alertLabel2 = CTkLabel(t, text="Please choose your image first", font=("Poppins", 16),
                                   text_color="#777", bg_color="transparent")
            alertLabel2.place(x=65, y=100)

            closeButton = CTkButton(t, text="Ok", fg_color="transparent", hover_color="null", border_color="#00BB6D",
                                    border_width=1, command=t.destroy)
            closeButton.place(x=125, y=150)



            t.mainloop()

    generate_Button = CTkButton(root, text=" Generate", font=("Poppins", 20), border_width=0, corner_radius=32,
                                fg_color="#00BB6D", width=600, height=50, hover_color="null", command=generateImage)
    generate_Button.place(x=460, y=630)

    download_Button = CTkButton(root, text="Download", font=("Poppins", 20), image=downloadPhoto, compound="right",
                                border_width=1, border_color="#00BB6D", corner_radius=32,
                                fg_color="transparent", width=600, height=50, hover_color="null",command=saveToDirectory)
    download_Button.place(x=460, y=696)
    plus=CTkImage(Image.open("Image/plus_icon.png"),size=(20,20))

    def browse():
        if image_label.cget("image"):

            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
            if file_path:
                image = Image.open(file_path)
                # image_resize=image.resize((300*3, 300*3), Image.LANCZOS)
                photo = CTkImage(Image.open(file_path), size=(600, 400))

                image_label.configure(image=photo)

                image_label.image = photo
                addPhoto.destroy()
                # image_label.configure(image="")
            else:
                pass
        elif image_label.cget("image") and result_label.cget("image"):
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
            if file_path:
                image = Image.open(file_path)
                # image_resize=image.resize((300*3, 300*3), Image.LANCZOS)
                photo = CTkImage(Image.open(file_path), size=(600, 400))

                image_label.configure(image=photo)

                image_label.image = photo
                addPhoto.destroy()
                result_label.configure(image="")
            else:
                pass



    browse_new=CTkButton(root,text="Select new image",image=plus,compound="right",text_color="#00BB6D",font=("Poppins",15),hover_color="null",bg_color="transparent",fg_color="transparent",command=browse)
    browse_new.place(x=36, y=600)

    # Logo and Navbar
    brand_logo = CTkLabel(root, image=logo, text="")
    brand_logo.place(x=26, y=26)

    itc = CTkButton(root, text="Image-to-Cartoon", font=("Poppins", 14), border_color="#00BB6D", border_width=1,
                    fg_color="transparent",
                    hover_color="null", corner_radius=32)
    itc.place(x=450, y=45)

    itt = CTkButton(root, text="Image-to-Text", font=("Poppins", 14), border_color="#00BB6D", border_width=1,
                    fg_color="transparent",
                    hover_color="null", corner_radius=32)
    itt.place(x=630, y=45)

    bright = CTkButton(root, text="Brightness", font=("Poppins", 14), border_color="#00BB6D", border_width=1,
                       fg_color="transparent",
                       hover_color="null", corner_radius=32)
    bright.place(x=780, y=45)

    blur = CTkButton(root, text="Effect", font=("Poppins", 14), border_color="#00BB6D", border_width=1,
                     fg_color="transparent",
                     hover_color="null", corner_radius=32)
    blur.place(x=930, y=45)

    link = CTkImage(Image.open("Image/link.png"), size=(20, 20))
    scanner = CTkButton(root, text="Document Scanner", font=("Poppins", 14),
                        fg_color="#00BB6D", image=link, compound="left", height=35,
                        hover_color="null", corner_radius=32)
    scanner.place(x=1280, y=45)

    root.mainloop()
