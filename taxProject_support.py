import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import taxProject

def main(*args):

    global root
    root = tk.Tk()
    root.iconbitmap("icon2.ico")
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)

    global _top1, _w1
    _top1 = root
    _w1 = taxProject.Toplevel1(_top1)
    root.mainloop()

if __name__ == '__main__':
    taxProject.start_up()
