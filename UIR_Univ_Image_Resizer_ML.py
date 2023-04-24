#Developed in X Minutes by Maurizio Naletto www.aied.studio 04/04/2023
#MIT License - Feel free to use & improve.
#Check 10

import tkinter
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import os


class ImageResizerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Resizer")
        self.master.geometry("600x300")
        self.master.config(bg='#e6e6e6')

        # Define labels and buttons
        self.file_label = tk.Label(self.master, text="Choose images to resize:", bg='#e6e6e6', font=("Arial", 10))
        self.file_label.grid(row=0, column=0, padx=10, pady=10)
        self.file_button = tk.Button(self.master, text="Browse", command=self.open_files, bg='#ff6666', font=("Arial", 10))
        self.file_button.grid(row=0, column=1, padx=10, pady=10)

        self.width_label = tk.Label(self.master, text="Width (in pixels):", bg='#e6e6e6', font=("Arial", 10))
        self.width_label.grid(row=1, column=0, padx=10, pady=10)
        self.width_entry = tk.Entry(self.master, bg='#ffffff')
        self.width_entry.grid(row=1, column=1, padx=10, pady=10)

        self.height_label = tk.Label(self.master, text="Height (in pixels):", bg='#e6e6e6', font=("Arial", 10))
        self.height_label.grid(row=2, column=0, padx=10, pady=10)
        self.height_entry = tk.Entry(self.master, bg='#ffffff')
        self.height_entry.grid(row=2, column=1, padx=10, pady=10)

        self.aspect_ratio_var = tk.IntVar()
        self.aspect_ratio_check = tk.Checkbutton(self.master, text="Keep aspect ratio", variable=self.aspect_ratio_var, bg='#e6e6e6', font=("Arial", 10))
        self.aspect_ratio_check.grid(row=2, column=2, padx=10, pady=10)

        self.output_label = tk.Label(self.master, text="Choose a folder to save the resized images:", bg='#e6e6e6', font=("Arial", 10))
        self.output_label.grid(row=3, column=0, padx=10, pady=10)
        self.output_button = tk.Button(self.master, text="Browse", command=self.choose_output_folder, bg='#ff6666', font=("Arial", 10))
        self.output_button.grid(row=3, column=1, padx=10, pady=10)
        self.explain_label = tk.Label(self.master, text="This Script can resize a lot of images...", bg='#e6e6e6', font=("Arial", 10))
        self.explain_label.grid(row=5, column=0, padx=10, pady=10)

        self.resize_button = tk.Button(self.master, text="Resize Images", command=self.resize_images, bg='#66b3ff', font=("Arial",10))
        self.resize_button.grid(row=4, column=0,  padx=10, pady=10)

    def open_files(self):
        self.filenames = filedialog.askopenfilenames(initialdir="/", title="Select files", filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")))
        self.file_label.config(text="Loaded!!")

    def choose_output_folder(self):
        self.output_folder = filedialog.askdirectory(initialdir="/", title="Select folder")
        self.output_label.config(text="Output folder: " + self.output_folder)

    def resize_images(self):
        try:
            width = int(self.width_entry.get())
            height = int(self.height_entry.get())
            keep_aspect_ratio = bool(self.aspect_ratio_var.get())

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

#root.iconbitmap(r"insert your root path for image.ico")



root.mainloop()