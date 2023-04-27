import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import *
from PIL import Image
import os
import imghdr




class ImageFormatConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Format Converter")
        self.master.geometry("600x500")
        self.master.config(bg='#e6e6e6')

        # Define labels and buttons
        self.folder_label = tk.Label(self.master, text="Choose folder containing images:", bg='#e6e6e6', font=("Arial", 10))
        self.folder_label.grid(row=0, column=0, padx=10, pady=10)
        self.folder_button = tk.Button(self.master, text="Browse", command=self.choose_folder, bg='#ff6666', font=("Arial", 10))
        self.folder_button.grid(row=0, column=1, padx=10, pady=10)

        self.format_label = tk.Label(self.master, text="Choose output format (e.g. jpeg, png):", bg='#e6e6e6', font=("Arial", 10))
        self.format_label.grid(row=1, column=0, padx=10, pady=10)
        self.format_entry = tk.Entry(self.master)
        self.format_entry.grid(row=1, column=1, padx=10, pady=10)

        self.convert_button = tk.Button(self.master, text="Convert", command=self.convert_images, bg='#66b3ff', font=("Arial",10))
        self.convert_button.grid(row=2, column=0,  padx=10, pady=10)

    def choose_folder(self):
        self.folder_path = filedialog.askdirectory(initialdir="/", title="Select folder")
        self.folder_label.config(text="Folder: " + self.folder_path)

    def convert_images(self):
        output_format = self.format_entry.get()
        if not output_format:
            messagebox.showerror("Error", "Please enter an output format.")
            return

        try:
            for file in os.listdir(self.folder_path):
                file_path = os.path.join(self.folder_path, file)

                #########

                if os.path.isfile(file_path):
                    img_type = imghdr.what(file_path) #control if is an image or not
                    if img_type: #
                        img = Image.open(file_path)
                        file_name, _ = os.path.splitext(file)
                        new_file_path = os.path.join(self.folder_path, f"{file_name}.{output_format}")
                        img.save(new_file_path)
                    else:
                        print("Not an image file, moving to the next file.")




                # if os.path.isfile(file_path):
                #     img = Image.open(file_path)
                #     file_name, _ = os.path.splitext(file)
                #     new_file_path = os.path.join(self.folder_path, f"{file_name}.{output_format}")
                #     img.save(new_file_path)

            messagebox.showinfo("Success", "Images converted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Could not convert images: {e}")



root = tk.Tk()

root.iconbitmap("logo.ico")

app = ImageFormatConverter(root)
root.mainloop()



