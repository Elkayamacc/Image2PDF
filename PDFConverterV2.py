from PIL import Image
import os
from tkinter import filedialog
import tkinter as tk



def convert_pdf():
    index = 0
    path_picture = filedialog.askdirectory()
    dire = 'Converted'
    path_pdf = os.path.join(path_picture , dire)
    os.mkdir(path_pdf)

    my_list = os.listdir(path_picture)
    for i in my_list:
        image = Image.open(r'' + path_picture+'//' + i)
        im = image.convert('RGB')
        im.save(r''+ path_pdf+'//' + i[:-4] +'.pdf', quality=15, optimze=True)
        index = index + 1

root = tk.Tk()
convert_pdf()
tk.mainloop()
