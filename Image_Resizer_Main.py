#Developed in X Minutes by Maurizio Naletto www.aied.studio 04/04/2023
#MIT License - Feel free to use & improve.
#Check 13

import tkinter
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import os
from tkinter import PhotoImage


class ImageResizerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Resizer")
        self.master.geometry("1600x512")
        self.master.config(bg='#e6e6e6')
        #define radio buttons

        # Define the radio buttons
        self.option_var = tk.StringVar(value="D0")
        #
        #self.option_var = tk.StringVar()
        self.option_label = tk.Label(self.master, text="Choose image size option: (select one)", bg='#e6e6e6', font=("Arial", 10))
        self.option_label.grid(row=2, column=0, padx=10, pady=10)

        self.efficendet_d0_radio = tk.Radiobutton(self.master, text="EfficientDet D0 (512x512)",
                                                  variable=self.option_var, value="D0", bg='#e6e6e6',
                                                  font=("Arial", 10))
        self.efficendet_d0_radio.grid(row=2, column=1, padx=10, pady=10)

        self.efficendet_d1_radio = tk.Radiobutton(self.master, text="EfficientDet D1 (640x640)",
                                                  variable=self.option_var, value="D1", bg='#e6e6e6',
                                                  font=("Arial", 10))
        self.efficendet_d1_radio.grid(row=2, column=2, padx=10, pady=10)

        self.efficendet_d2_radio = tk.Radiobutton(self.master, text="EfficientDet D2 (768x768)",
                                                  variable=self.option_var, value="D2", bg='#e6e6e6',
                                                  font=("Arial", 10))
        self.efficendet_d2_radio.grid(row=2, column=3, padx=10, pady=10)

        self.efficendet_d3_radio = tk.Radiobutton(self.master, text="EfficientDet D3 (896x896)",
                                                  variable=self.option_var, value="D3", bg='#e6e6e6',
                                                  font=("Arial", 10))
        self.efficendet_d3_radio.grid(row=2, column=4, padx=10, pady=10)

        self.efficendet_d4_radio = tk.Radiobutton(self.master, text="EfficientDet D4 (1024x1024)",
                                                  variable=self.option_var, value="D4", bg='#e6e6e6',
                                                  font=("Arial", 10))
        self.efficendet_d4_radio.grid(row=2, column=5, padx=10, pady=10)

        self.custom_radio = tk.Radiobutton(self.master, text="Custom", variable=self.option_var, value="Custom",
                                           bg='#e6e6e6', font=("Arial", 10))
        self.custom_radio.grid(row=2, column=6, padx=10, pady=10)
        self.custom_width_label = tk.Label(self.master, text="Custom Width:", bg='#e6e6e6', font=("Arial", 10))
        self.custom_width_label.grid(row=5, column=4, padx=10, pady=10)
        self.custom_width_entry = tk.Entry(self.master, bg='#ffffff')
        self.custom_width_entry.grid(row=5, column=5, padx=10, pady=10)
        self.custom_height_label = tk.Label(self.master, text="Custom Height:", bg='#e6e6e6', font=("Arial", 10))
        self.custom_height_label.grid(row=6, column=4, padx=10, pady=10)
        self.custom_height_entry = tk.Entry(self.master, bg='#ffffff')
        self.custom_height_entry.grid(row=6, column=5, padx=10, pady=10)

        # ... existing code ...


        # Define labels and buttons
        self.file_label = tk.Label(self.master, text="This script help you to convert images for EfficientDet D0 512x512 ml sessions", bg='#e6e6e6', font=("Arial", 10))
        self.file_label.grid(row=0, column=0, padx=10, pady=10)
        self.file_label = tk.Label(self.master, text="Choose images to resize: (folder)", bg='#e6e6e6', font=("Arial", 10))
        self.file_label.grid(row=1, column=0, padx=10, pady=10)
        self.file_button = tk.Button(self.master, text="Browse", command=self.open_files, bg='#ff6666', font=("Arial", 10))
        self.file_button.grid(row=1, column=1, padx=10, pady=10)



        self.output_label = tk.Label(self.master, text="Choose a folder to save the resized images:", bg='#e6e6e6', font=("Arial", 10))
        self.output_label.grid(row=4, column=0, padx=10, pady=10)
        self.output_button = tk.Button(self.master, text="Browse", command=self.choose_output_folder, bg='#ff6666', font=("Arial", 10))
        self.output_button.grid(row=4, column=1, padx=10, pady=10)
        self.explain_label = tk.Label(self.master, text="This Script can resize a lot of images...", bg='#e6e6e6', font=("Arial", 10))
        self.explain_label.grid(row=6, column=0, padx=10, pady=10)

        self.resize_button = tk.Button(self.master, text="Resize Images (Launch!)", command=self.resize_images, bg='#66b3ff', font=("Arial",10))
        self.resize_button.grid(row=5, column=0,  padx=10, pady=10)


        #image

        # Load the image
        image_path = "Dataset_Fixer.png"  # Replace with the actual image file path
        image = PhotoImage(file=image_path)

        # Resize the image
        resized_image = image.subsample(3)  # Change the subsample value to adjust the size

        # Create a label to display the resized image
        self.image_label = tk.Label(self.master, image=resized_image, bg='#e6e6e6')
        self.image_label.image = resized_image  # Store a reference to the resized image
        self.image_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10,sticky="nsew")

        #end

    def open_files(self):
        self.filenames = filedialog.askopenfilenames(initialdir="/", title="Select files", filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")))
        self.file_label.config(text="Loaded!!")

    def choose_output_folder(self):
        self.output_folder = filedialog.askdirectory(initialdir="/", title="Select folder")
        self.output_label.config(text="Output folder: " + self.output_folder)

    def resize_images(self):
        try:
            selected_option = self.option_var.get()

            if selected_option == "Custom":
                width = int(self.custom_width_entry.get())
                height = int(self.custom_height_entry.get())
                keep_aspect_ratio = False
            elif selected_option == "D0":
                width = 512
                height = 512
                keep_aspect_ratio = False

            elif selected_option == "D1":
                width = 640
                height = 640
                keep_aspect_ratio = False
            elif selected_option == "D2":
                width = 768
                height = 768
                keep_aspect_ratio = False
            elif selected_option == "D3":
                width = 896
                height = 896
                keep_aspect_ratio = False
            elif selected_option == "D4":
                width = 1024
                height = 1024
                keep_aspect_ratio = False
            else:
                raise ValueError("Invalid option selected.")

            for filename in self.filenames:
                img = Image.open(filename)
                if keep_aspect_ratio:
                    img.thumbnail((width, height), Image.ANTIALIAS)
                else:
                    img = img.resize((width, height), Image.ANTIALIAS)
                new_filename = filename.split("/")[-1].split(".")[0] + "_resized.png"
                output_path = self.output_folder + "/" + new_filename
                img.save(output_path)

            self.file_label.config(text="Images resized successfully!", fg='green')
            if messagebox.askyesno("Open Output Folder", "Images have been resized. Do you want to open the output folder?"):
                os.startfile(self.output_folder)
        except:
            self.file_label.config(text="Error: could not resize images.", fg='red')

root = tk.Tk()
app = ImageResizerGUI(root)
root.iconbitmap("logo.ico")  # Replace "icon.ico" with the actual path to your icon file

#root.iconbitmap(r"insert your root path for image.ico")



root.mainloop()