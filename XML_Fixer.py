#Developed in X Minutes by Maurizio Naletto www.aied.studio 04/04/2023
#MIT License - Feel free to use & improve.
#Check 12




import xml.etree.ElementTree as ET


import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import os

class XML_Rewrite:
    def __init__(self, master):
        self.master = master
        self.master.title("XML Rewriter")
        self.master.geometry("600x500")
        self.master.config(bg='#e6e6e6')

        # Define labels and buttons
        self.file_label = tk.Label(self.master, text="Choose XML to rewrite:", bg='#e6e6e6', font=("Arial", 10))
        self.file_label.grid(row=0, column=0, padx=10, pady=10)
        self.file_button = tk.Button(self.master, text="Browse", command=self.open_files, bg='#ff6666', font=("Arial", 10))
        self.file_button.grid(row=0, column=1, padx=10, pady=10)

        self.output_label = tk.Label(self.master, text="Choose a folder to save the rewritten XML files:", bg='#e6e6e6', font=("Arial", 10))
        self.output_label.grid(row=3, column=0, padx=10, pady=10)
        self.output_button = tk.Button(self.master, text="Browse", command=self.choose_output_folder, bg='#ff6666', font=("Arial", 10))
        self.output_button.grid(row=3, column=1, padx=10, pady=10)
        self.explain_label = tk.Label(self.master, text="This Script can rewrite a lot of XML files...", bg='#e6e6e6', font=("Arial", 10))
        self.explain_label.grid(row=5, column=0, padx=10, pady=10)

        self.resize_button = tk.Button(self.master, text="REWRITE", command=self.rewrite_xml, bg='#66b3ff', font=("Arial",10))
        self.resize_button.grid(row=4, column=0,  padx=10, pady=10)

    def open_files(self):
        self.filenames = filedialog.askopenfilenames(initialdir="/", title="Select files", filetypes=(("XML files", "*.xml"),))
        self.file_label.config(text="Loaded!!")

    def choose_output_folder(self):
        self.output_folder = filedialog.askdirectory(initialdir="/", title="Select folder")
        self.output_label.config(text="Output folder: " + self.output_folder)

    def rewrite_xml(self):
        try:
            for filename in self.filenames:
                with open(filename, 'r') as file:
                    content = file.read()

                # Replace image formats
                content = content.replace('.png', '.jpeg') \
                    .replace('.tiff', '.jpeg') \
                    .replace('.tif', '.jpeg') \
                    .replace('.webp', '.jpeg')

                new_filename = os.path.split(filename)[-1]
                output_path = os.path.join(self.output_folder, new_filename)

                with open(output_path, 'w') as file:
                    file.write(content)

            self.file_label.config(text="XML rewrited successfully!", fg='green')
            if messagebox.askyesno("Open Output Folder", "XML have been rewrited. Do you want to open the output folder?"):
                os.startfile(self.output_folder)
        except:
            self.file_label.config(text="Error: could not rewrite XML Files.", fg='red')

root = tk.Tk()
app = XML_Rewrite(root)
root.mainloop()

