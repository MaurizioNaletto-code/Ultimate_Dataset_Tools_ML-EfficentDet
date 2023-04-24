#Developed in 15 Minutes by Maurizio Naletto www.aied.studio 04/04/2023
#MIT License - Feel free to use & improve.
#Check 7

import tkinter
import tkinter as tk
from tkinter import filedialog
from PIL import Image


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

            for filename in self.filenames:
                img = Image.open(filename)
                resized_img = img.resize((width, height), Image.ANTIALIAS)
                new_filename = filename.split("/")[-1].split(".")[0] + "_resized.png"
                output_path = self.output_folder + "/" + new_filename
                resized_img.save(output_path)

            self.file_label.config(text="Images resized successfully!", fg='green')
        except:
            self.file_label.config(text="Error: could not resize images.", fg='red')

root = tk.Tk()
app = ImageResizerGUI(root)

#root.iconbitmap(r"insert your root path for image.ico")



root.mainloop()