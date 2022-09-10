import sys
import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
from tkinter import messagebox
from tkinter.constants import *
from taxFunctions import *


import taxProject_support



class Toplevel1:
    def __init__(self, top=None):

        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9'
        _ana2color = '#ececec'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x385+317+139")
        top.minsize(800, 520)
        top.maxsize(1370, 749)
        top.resizable(0,  0)
        top.title("Tax - Canada 2022")
        top.configure(borderwidth="1")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#2f005e")
        top.configure(highlightcolor="black")

        self.top = top
        self.combobox = tk.StringVar()

        self.Label_Enter_Income = tk.Label(self.top)
        self.Label_Enter_Income.place(x=30, y=50, height=27, width=204)
        self.Label_Enter_Income.configure(activebackground="#f9f9f9")
        self.Label_Enter_Income.configure(activeforeground="#000000")
        self.Label_Enter_Income.configure(anchor='w')
        self.Label_Enter_Income.configure(background="#ffffff")
        self.Label_Enter_Income.configure(compound='left')
        self.Label_Enter_Income.configure(cursor="fleur")
        self.Label_Enter_Income.configure(disabledforeground="#a3a3a3")
        self.Label_Enter_Income.configure(font="-family {Malgun Gothic} -size 9")
        self.Label_Enter_Income.configure(foreground="#230046")
        self.Label_Enter_Income.configure(highlightbackground="#d9d9d9")
        self.Label_Enter_Income.configure(highlightcolor="black")
        self.Label_Enter_Income.configure(text='''Enter your annual gross income:''')

        self.Label_Enter_rrsp = tk.Label(self.top)
        self.Label_Enter_rrsp.place(x=30, y=125, height=27, width=204)
        self.Label_Enter_rrsp.configure(activebackground="#f9f9f9")
        self.Label_Enter_rrsp.configure(activeforeground="#000000")
        self.Label_Enter_rrsp.configure(anchor='w')
        self.Label_Enter_rrsp.configure(background="#ffffff")
        self.Label_Enter_rrsp.configure(compound='left')
        self.Label_Enter_rrsp.configure(cursor="fleur")
        self.Label_Enter_rrsp.configure(disabledforeground="#a3a3a3")
        self.Label_Enter_rrsp.configure(font="-family {Malgun Gothic} -size 9")
        self.Label_Enter_rrsp.configure(foreground="#230046")
        self.Label_Enter_rrsp.configure(highlightbackground="#d9d9d9")
        self.Label_Enter_rrsp.configure(highlightcolor="black")
        self.Label_Enter_rrsp.configure(text='''Enter your RRSP contribution:''')

        self.Label_Enter_taxPaid = tk.Label(self.top)
        self.Label_Enter_taxPaid.place(x=30, y=200, height=27, width=204)
        self.Label_Enter_taxPaid.configure(activebackground="#f9f9f9")
        self.Label_Enter_taxPaid.configure(activeforeground="#000000")
        self.Label_Enter_taxPaid.configure(anchor='w')
        self.Label_Enter_taxPaid.configure(background="#ffffff")
        self.Label_Enter_taxPaid.configure(compound='left')
        self.Label_Enter_taxPaid.configure(cursor="fleur")
        self.Label_Enter_taxPaid.configure(disabledforeground="#a3a3a3")
        self.Label_Enter_taxPaid.configure(font="-family {Malgun Gothic} -size 9")
        self.Label_Enter_taxPaid.configure(foreground="#230046")
        self.Label_Enter_taxPaid.configure(highlightbackground="#d9d9d9")
        self.Label_Enter_taxPaid.configure(highlightcolor="black")
        self.Label_Enter_taxPaid.configure(text='''Enter your tax paid:''')

        self.Label_Heading = tk.Label(self.top)
        self.Label_Heading.place(x=30, y=5, height=50, width=500)
        self.Label_Heading.configure(activebackground="#f9f9f9")
        self.Label_Heading.configure(activeforeground="#000000")
        self.Label_Heading.configure(anchor='w')
        self.Label_Heading.configure(background="#ffffff")
        self.Label_Heading.configure(compound='left')
        self.Label_Heading.configure(disabledforeground="#a3a3a3")
        self.Label_Heading.configure(font="-family {Malgun Gothic} -size 23")
        self.Label_Heading.configure(foreground="#230046")
        self.Label_Heading.configure(highlightbackground="#d9d9d9")
        self.Label_Heading.configure(highlightcolor="black")
        self.Label_Heading.configure(text='''Canada 2022 Tax Refund/Owing''')

        self.Entry_Enter_Income = tk.Entry(self.top)
        self.Entry_Enter_Income.place(x=30, y=80, height=40, width=214)
        self.Entry_Enter_Income.configure(background="white")
        self.Entry_Enter_Income.configure(disabledforeground="#a3a3a3")
        self.Entry_Enter_Income.configure(font="-family {Malgun Gothic} -size 10")
        self.Entry_Enter_Income.configure(foreground="#000000")
        self.Entry_Enter_Income.configure(highlightbackground="#d9d9d9")
        self.Entry_Enter_Income.configure(highlightcolor="black")
        self.Entry_Enter_Income.configure(insertbackground="black")
        self.Entry_Enter_Income.configure(selectbackground="blue")
        self.Entry_Enter_Income.configure(selectforeground="white")
        self.Entry_Enter_Income.insert(0,0)

        self.Entry_Enter_rrsp = tk.Entry(self.top)
        self.Entry_Enter_rrsp.place(x=30, y=155, height=40, width=214)
        self.Entry_Enter_rrsp.configure(background="white")
        self.Entry_Enter_rrsp.configure(disabledforeground="#a3a3a3")
        self.Entry_Enter_rrsp.configure(font="-family {Malgun Gothic} -size 10")
        self.Entry_Enter_rrsp.configure(foreground="#000000")
        self.Entry_Enter_rrsp.configure(highlightbackground="#d9d9d9")
        self.Entry_Enter_rrsp.configure(highlightcolor="black")
        self.Entry_Enter_rrsp.configure(insertbackground="black")
        self.Entry_Enter_rrsp.configure(selectbackground="blue")
        self.Entry_Enter_rrsp.configure(selectforeground="white")
        self.Entry_Enter_rrsp.insert(0,0)

        self.Entry_Enter_capGains = tk.Entry(self.top)
        self.Entry_Enter_capGains.place(x=30, y=300, height=40, width=214)
        self.Entry_Enter_capGains.configure(background="white")
        self.Entry_Enter_capGains.configure(disabledforeground="#a3a3a3")
        self.Entry_Enter_capGains.configure(font="-family {Malgun Gothic} -size 10")
        self.Entry_Enter_capGains.configure(foreground="#000000")
        self.Entry_Enter_capGains.configure(highlightbackground="#d9d9d9")
        self.Entry_Enter_capGains.configure(highlightcolor="black")
        self.Entry_Enter_capGains.configure(insertbackground="black")
        self.Entry_Enter_capGains.configure(selectbackground="blue")
        self.Entry_Enter_capGains.configure(selectforeground="white")
        self.Entry_Enter_capGains.insert(0,0)

        self.Entry_Enter_eDivs = tk.Entry(self.top)
        self.Entry_Enter_eDivs.place(x=260, y=155, height=40, width=214)
        self.Entry_Enter_eDivs.configure(background="white")
        self.Entry_Enter_eDivs.configure(disabledforeground="#a3a3a3")
        self.Entry_Enter_eDivs.configure(font="-family {Malgun Gothic} -size 10")
        self.Entry_Enter_eDivs.configure(foreground="#000000")
        self.Entry_Enter_eDivs.configure(highlightbackground="#d9d9d9")
        self.Entry_Enter_eDivs.configure(highlightcolor="black")
        self.Entry_Enter_eDivs.configure(insertbackground="black")
        self.Entry_Enter_eDivs.configure(selectbackground="blue")
        self.Entry_Enter_eDivs.configure(selectforeground="white")
        self.Entry_Enter_eDivs.insert(0,0)

        self.Entry_Enter_taxPaid = tk.Entry(self.top)
        self.Entry_Enter_taxPaid.place(x=30, y=225, height=40, width=214)
        self.Entry_Enter_taxPaid.configure(background="white")
        self.Entry_Enter_taxPaid.configure(disabledforeground="#a3a3a3")
        self.Entry_Enter_taxPaid.configure(font="-family {Malgun Gothic} -size 10")
        self.Entry_Enter_taxPaid.configure(foreground="#000000")
        self.Entry_Enter_taxPaid.configure(highlightbackground="#d9d9d9")
        self.Entry_Enter_taxPaid.configure(highlightcolor="black")
        self.Entry_Enter_taxPaid.configure(insertbackground="black")
        self.Entry_Enter_taxPaid.configure(selectbackground="blue")
        self.Entry_Enter_taxPaid.configure(selectforeground="white")
        self.Entry_Enter_taxPaid.insert(0,0)

        self.calculateButton = tk.Button(self.top)
        self.calculateButton.place(x=265, y=375, height=44, width=127)
        self.calculateButton.configure(activebackground="#ececec")
        self.calculateButton.configure(activeforeground="#000000")
        self.calculateButton.configure(background="#690f96")
        self.calculateButton.configure(compound='left')
        self.calculateButton.configure(disabledforeground="#a3a3a3")
        self.calculateButton.configure(font="-family {Malgun Gothic} -size 11 -weight bold")
        self.calculateButton.configure(foreground="#ffffff")
        self.calculateButton.configure(highlightbackground="#d9d9d9")
        self.calculateButton.configure(highlightcolor="black")
        self.calculateButton.configure(pady="0")
        self.calculateButton.configure(text='''Calculate''')
        self.calculateButton.configure(command=self.getInput)

        self.textBox_Total_Tax = tk.Text(self.top)
        self.textBox_Total_Tax.place(x=550, y=365, height=60, width=300)
        self.textBox_Total_Tax.configure(background="white")
        self.textBox_Total_Tax.configure(font="-family {Malgun Gothic} -size 20")
        self.textBox_Total_Tax.configure(foreground="black")
        self.textBox_Total_Tax.configure(highlightbackground="#d9d9d9")
        self.textBox_Total_Tax.configure(highlightcolor="black")
        self.textBox_Total_Tax.configure(insertbackground="black")
        self.textBox_Total_Tax.configure(selectbackground="blue")
        self.textBox_Total_Tax.configure(selectforeground="white")
        self.textBox_Total_Tax.configure(wrap="word")
        self.textBox_Total_Tax.configure(highlightthickness = 0, borderwidth=0)

        self.Label_Total_Tax = tk.Label(self.top)
        self.Label_Total_Tax.place(x=550, y=335, height=27, width=150)
        self.Label_Total_Tax.configure(activebackground="#f9f9f9")
        self.Label_Total_Tax.configure(activeforeground="#000000")
        self.Label_Total_Tax.configure(anchor='w')
        self.Label_Total_Tax.configure(background="#ffffff")
        self.Label_Total_Tax.configure(compound='left')
        self.Label_Total_Tax.configure(disabledforeground="#a3a3a3")
        self.Label_Total_Tax.configure(font="-family {Malgun Gothic} -size 11 -weight bold")
        self.Label_Total_Tax.configure(foreground="#230046")
        self.Label_Total_Tax.configure(highlightbackground="#d9d9d9")
        self.Label_Total_Tax.configure(highlightcolor="black")
        self.Label_Total_Tax.configure(text='''Total Tax''')

        self.Label_Income_Tax = tk.Label(self.top)
        self.Label_Income_Tax.place(x=550, y=250, height=27, width=100)
        self.Label_Income_Tax.configure(activebackground="#f9f9f9")
        self.Label_Income_Tax.configure(activeforeground="#000000")
        self.Label_Income_Tax.configure(anchor='w')
        self.Label_Income_Tax.configure(background="#ffffff")
        self.Label_Income_Tax.configure(compound='left')
        self.Label_Income_Tax.configure(disabledforeground="#a3a3a3")
        self.Label_Income_Tax.configure(font="-family {Malgun Gothic} -size 11 -weight bold")
        self.Label_Income_Tax.configure(foreground="#230046")
        self.Label_Income_Tax.configure(highlightbackground="#d9d9d9")
        self.Label_Income_Tax.configure(highlightcolor="black")
        self.Label_Income_Tax.configure(text='''Income Tax''')

        self.Label_Tax_Credit = tk.Label(self.top)
        self.Label_Tax_Credit.place(x=550, y=100, height=27, width=100)
        self.Label_Tax_Credit.configure(activebackground="#f9f9f9")
        self.Label_Tax_Credit.configure(activeforeground="#000000")
        self.Label_Tax_Credit.configure(anchor='w')
        self.Label_Tax_Credit.configure(background="#ffffff")
        self.Label_Tax_Credit.configure(compound='left')
        self.Label_Tax_Credit.configure(disabledforeground="#a3a3a3")
        self.Label_Tax_Credit.configure(font="-family {Malgun Gothic} -size 11 -weight bold")
        self.Label_Tax_Credit.configure(foreground="#230046")
        self.Label_Tax_Credit.configure(highlightbackground="#d9d9d9")
        self.Label_Tax_Credit.configure(highlightcolor="black")
        self.Label_Tax_Credit.configure(text='''Tax Credits''')

        self.textBox_eDiv = tk.Text(self.top)
        self.textBox_eDiv.place(x=690, y=130, height=24, width=150)
        self.textBox_eDiv.configure(background="white")
        self.textBox_eDiv.configure(font="TkTextFont")
        self.textBox_eDiv.configure(foreground="black")
        self.textBox_eDiv.configure(highlightbackground="#d9d9d9")
        self.textBox_eDiv.configure(highlightcolor="black")
        self.textBox_eDiv.configure(insertbackground="black")
        self.textBox_eDiv.configure(selectbackground="blue")
        self.textBox_eDiv.configure(selectforeground="white")
        self.textBox_eDiv.configure(wrap="word")
        self.textBox_eDiv.configure(highlightthickness = 0, borderwidth=0)

        self.Label_eDiv = tk.Label(self.top)
        self.Label_eDiv.place(x=550, y=125, height=27, width=100)
        self.Label_eDiv.configure(activebackground="#f9f9f9")
        self.Label_eDiv.configure(activeforeground="#000000")
        self.Label_eDiv.configure(anchor='w')
        self.Label_eDiv.configure(background="#ffffff")
        self.Label_eDiv.configure(compound='left')
        self.Label_eDiv.configure(disabledforeground="#a3a3a3")
        self.Label_eDiv.configure(font="-family {Malgun Gothic} -size 9")
        self.Label_eDiv.configure(foreground="#230046")
        self.Label_eDiv.configure(highlightbackground="#d9d9d9")
        self.Label_eDiv.configure(highlightcolor="black")
        self.Label_eDiv.configure(text='''Eligible dividends: ''')

        self.textBox_nonEdiv = tk.Text(self.top)
        self.textBox_nonEdiv.place(x=690, y=155, height=24, width=150)
        self.textBox_nonEdiv.configure(background="white")
        self.textBox_nonEdiv.configure(font="TkTextFont")
        self.textBox_nonEdiv.configure(foreground="black")
        self.textBox_nonEdiv.configure(highlightbackground="#d9d9d9")
        self.textBox_nonEdiv.configure(highlightcolor="black")
        self.textBox_nonEdiv.configure(insertbackground="black")
        self.textBox_nonEdiv.configure(selectbackground="blue")
        self.textBox_nonEdiv.configure(selectforeground="white")
        self.textBox_nonEdiv.configure(wrap="word")
        self.textBox_nonEdiv.configure(highlightthickness = 0, borderwidth=0)

        self.Label_nonEdiv = tk.Label(self.top)
        self.Label_nonEdiv.place(x=550, y=150, height=27, width=130)
        self.Label_nonEdiv.configure(activebackground="#f9f9f9")
        self.Label_nonEdiv.configure(activeforeground="#000000")
        self.Label_nonEdiv.configure(anchor='w')
        self.Label_nonEdiv.configure(background="#ffffff")
        self.Label_nonEdiv.configure(compound='left')
        self.Label_nonEdiv.configure(disabledforeground="#a3a3a3")
        self.Label_nonEdiv.configure(font="-family {Malgun Gothic} -size 9")
        self.Label_nonEdiv.configure(foreground="#230046")
        self.Label_nonEdiv.configure(highlightbackground="#d9d9d9")
        self.Label_nonEdiv.configure(highlightcolor="black")
        self.Label_nonEdiv.configure(text='''Non eligible dividends: ''')

        self.textBox_Tuition_Credit = tk.Text(self.top)
        self.textBox_Tuition_Credit.place(x=690, y=185, height=24, width=150)
        self.textBox_Tuition_Credit.configure(background="white")
        self.textBox_Tuition_Credit.configure(font="TkTextFont")
        self.textBox_Tuition_Credit.configure(foreground="black")
        self.textBox_Tuition_Credit.configure(highlightbackground="#d9d9d9")
        self.textBox_Tuition_Credit.configure(highlightcolor="black")
        self.textBox_Tuition_Credit.configure(insertbackground="black")
        self.textBox_Tuition_Credit.configure(selectbackground="blue")
        self.textBox_Tuition_Credit.configure(selectforeground="white")
        self.textBox_Tuition_Credit.configure(wrap="word")
        self.textBox_Tuition_Credit.configure(highlightthickness = 0, borderwidth=0)

        self.Label_Tuition_Credit = tk.Label(self.top)
        self.Label_Tuition_Credit.place(x=550, y=180, height=27, width=130)
        self.Label_Tuition_Credit.configure(activebackground="#f9f9f9")
        self.Label_Tuition_Credit.configure(activeforeground="#000000")
        self.Label_Tuition_Credit.configure(anchor='w')
        self.Label_Tuition_Credit.configure(background="#ffffff")
        self.Label_Tuition_Credit.configure(compound='left')
        self.Label_Tuition_Credit.configure(disabledforeground="#a3a3a3")
        self.Label_Tuition_Credit.configure(font="-family {Malgun Gothic} -size 9")
        self.Label_Tuition_Credit.configure(foreground="#230046")
        self.Label_Tuition_Credit.configure(highlightbackground="#d9d9d9")
        self.Label_Tuition_Credit.configure(highlightcolor="black")
        self.Label_Tuition_Credit.configure(text='''Tuition: ''')

        self.textBox_Dono_Credit = tk.Text(self.top)
        self.textBox_Dono_Credit.place(x=690, y=215, height=24, width=150)
        self.textBox_Dono_Credit.configure(background="white")
        self.textBox_Dono_Credit.configure(font="TkTextFont")
        self.textBox_Dono_Credit.configure(foreground="black")
        self.textBox_Dono_Credit.configure(highlightbackground="#d9d9d9")
        self.textBox_Dono_Credit.configure(highlightcolor="black")
        self.textBox_Dono_Credit.configure(insertbackground="black")
        self.textBox_Dono_Credit.configure(selectbackground="blue")
        self.textBox_Dono_Credit.configure(selectforeground="white")
        self.textBox_Dono_Credit.configure(wrap="word")
        self.textBox_Dono_Credit.configure(highlightthickness = 0, borderwidth=0)

        self.Label_Dono_Credit = tk.Label(self.top)
        self.Label_Dono_Credit.place(x=550, y=210, height=27, width=130)
        self.Label_Dono_Credit.configure(activebackground="#f9f9f9")
        self.Label_Dono_Credit.configure(activeforeground="#000000")
        self.Label_Dono_Credit.configure(anchor='w')
        self.Label_Dono_Credit.configure(background="#ffffff")
        self.Label_Dono_Credit.configure(compound='left')
        self.Label_Dono_Credit.configure(disabledforeground="#a3a3a3")
        self.Label_Dono_Credit.configure(font="-family {Malgun Gothic} -size 9")
        self.Label_Dono_Credit.configure(foreground="#230046")
        self.Label_Dono_Credit.configure(highlightbackground="#d9d9d9")
        self.Label_Dono_Credit.configure(highlightcolor="black")
        self.Label_Dono_Credit.configure(text='''Charitable Donations: ''')

        self.textBox_Federal_Tax = tk.Text(self.top)
        self.textBox_Federal_Tax.place(x=650, y=305, height=24, width=150)
        self.textBox_Federal_Tax.configure(background="white")
        self.textBox_Federal_Tax.configure(font="-family {Malgun Gothic} -size 10")
        self.textBox_Federal_Tax.configure(foreground="black")
        self.textBox_Federal_Tax.configure(highlightbackground="#d9d9d9")
        self.textBox_Federal_Tax.configure(highlightcolor="black")
        self.textBox_Federal_Tax.configure(insertbackground="black")
        self.textBox_Federal_Tax.configure(selectbackground="blue")
        self.textBox_Federal_Tax.configure(selectforeground="white")
        self.textBox_Federal_Tax.configure(wrap="word")
        self.textBox_Federal_Tax.configure(highlightthickness = 0, borderwidth=0)

        self.Label_Federal_Tax = tk.Label(self.top)
        self.Label_Federal_Tax.place(x=550, y=300, height=27, width=85)
        self.Label_Federal_Tax.configure(activebackground="#f9f9f9")
        self.Label_Federal_Tax.configure(activeforeground="#000000")
        self.Label_Federal_Tax.configure(anchor='w')
        self.Label_Federal_Tax.configure(background="#ffffff")
        self.Label_Federal_Tax.configure(compound='left')
        self.Label_Federal_Tax.configure(disabledforeground="#a3a3a3")
        self.Label_Federal_Tax.configure(font="-family {Malgun Gothic} -size 10")
        self.Label_Federal_Tax.configure(foreground="#230046")
        self.Label_Federal_Tax.configure(highlightbackground="#d9d9d9")
        self.Label_Federal_Tax.configure(highlightcolor="black")
        self.Label_Federal_Tax.configure(text='''Federal Tax:''')

        self.textBox_Provincial_Tax = tk.Text(self.top)
        self.textBox_Provincial_Tax.place(x=650, y=280, height=24, width=150)
        self.textBox_Provincial_Tax.configure(background="white")
        self.textBox_Provincial_Tax.configure(font="TkTextFont")
        self.textBox_Provincial_Tax.configure(foreground="black")
        self.textBox_Provincial_Tax.configure(highlightbackground="#d9d9d9")
        self.textBox_Provincial_Tax.configure(highlightcolor="black")
        self.textBox_Provincial_Tax.configure(insertbackground="black")
        self.textBox_Provincial_Tax.configure(selectbackground="blue")
        self.textBox_Provincial_Tax.configure(selectforeground="white")
        self.textBox_Provincial_Tax.configure(wrap="word")
        self.textBox_Provincial_Tax.configure(highlightthickness = 0, borderwidth=0)

        self.Label_Provincial_Tax = tk.Label(self.top)
        self.Label_Provincial_Tax.place(x=550, y=275, height=27, width=85)
        self.Label_Provincial_Tax.configure(activebackground="#f9f9f9")
        self.Label_Provincial_Tax.configure(activeforeground="#000000")
        self.Label_Provincial_Tax.configure(anchor='w')
        self.Label_Provincial_Tax.configure(background="#ffffff")
        self.Label_Provincial_Tax.configure(compound='left')
        self.Label_Provincial_Tax.configure(disabledforeground="#a3a3a3")
        self.Label_Provincial_Tax.configure(font="-family {Malgun Gothic} -size 9")
        self.Label_Provincial_Tax.configure(foreground="#230046")
        self.Label_Provincial_Tax.configure(highlightbackground="#d9d9d9")
        self.Label_Provincial_Tax.configure(highlightcolor="black")
        self.Label_Provincial_Tax.configure(text='''Provincial Tax:''')

        self.Label_Enter_Province = tk.Label(self.top)
        self.Label_Enter_Province.place(x=250, y=50, height=27, width=204)
        self.Label_Enter_Province.configure(activebackground="#f9f9f9")
        self.Label_Enter_Province.configure(activeforeground="#000000")
        self.Label_Enter_Province.configure(anchor='w')
        self.Label_Enter_Province.configure(background="#ffffff")
        self.Label_Enter_Province.configure(compound='left')
        self.Label_Enter_Province.configure(disabledforeground="#a3a3a3")
        self.Label_Enter_Province.configure(font="-family {Malgun Gothic} -size 9")
        self.Label_Enter_Province.configure(foreground="#230046")
        self.Label_Enter_Province.configure(highlightbackground="#d9d9d9")
        self.Label_Enter_Province.configure(highlightcolor="black")
        self.Label_Enter_Province.configure(text='''What is your province?''')

        self.Label_Enter_capGains = tk.Label(self.top)
        self.Label_Enter_capGains.place(x=30, y=268, height=27, width=204)
        self.Label_Enter_capGains.configure(activebackground="#f9f9f9")
        self.Label_Enter_capGains.configure(activeforeground="#000000")
        self.Label_Enter_capGains.configure(anchor='w')
        self.Label_Enter_capGains.configure(background="#ffffff")
        self.Label_Enter_capGains.configure(compound='left')
        self.Label_Enter_capGains.configure(disabledforeground="#a3a3a3")
        self.Label_Enter_capGains.configure(font="-family {Malgun Gothic} -size 9")
        self.Label_Enter_capGains.configure(foreground="#230046")
        self.Label_Enter_capGains.configure(highlightbackground="#d9d9d9")
        self.Label_Enter_capGains.configure(highlightcolor="black")
        self.Label_Enter_capGains.configure(text='''Enter capital gains:''')

        self.Label_Enter_eDivs = tk.Label(self.top)
        self.Label_Enter_eDivs.place(x=260, y=125, height=27, width=204)
        self.Label_Enter_eDivs.configure(activebackground="#f9f9f9")
        self.Label_Enter_eDivs.configure(activeforeground="#000000")
        self.Label_Enter_eDivs.configure(anchor='w')
        self.Label_Enter_eDivs.configure(background="#ffffff")
        self.Label_Enter_eDivs.configure(compound='left')
        self.Label_Enter_eDivs.configure(disabledforeground="#a3a3a3")
        self.Label_Enter_eDivs.configure(font="-family {Malgun Gothic} -size 9")
        self.Label_Enter_eDivs.configure(foreground="#230046")
        self.Label_Enter_eDivs.configure(highlightbackground="#d9d9d9")
        self.Label_Enter_eDivs.configure(highlightcolor="black")
        self.Label_Enter_eDivs.configure(text='''Enter eligible dividends:''')

        self.Label_Enter_nonEdivs = tk.Label(self.top)
        self.Label_Enter_nonEdivs.place(x=260, y=200, height=27, width=204)
        self.Label_Enter_nonEdivs.configure(activebackground="#f9f9f9")
        self.Label_Enter_nonEdivs.configure(activeforeground="#000000")
        self.Label_Enter_nonEdivs.configure(anchor='w')
        self.Label_Enter_nonEdivs.configure(background="#ffffff")
        self.Label_Enter_nonEdivs.configure(compound='left')
        self.Label_Enter_nonEdivs.configure(disabledforeground="#a3a3a3")
        self.Label_Enter_nonEdivs.configure(font="-family {Malgun Gothic} -size 9")
        self.Label_Enter_nonEdivs.configure(foreground="#230046")
        self.Label_Enter_nonEdivs.configure(highlightbackground="#d9d9d9")
        self.Label_Enter_nonEdivs.configure(highlightcolor="black")
        self.Label_Enter_nonEdivs.configure(text='''Enter non eligible dividends:''')

        self.Entry_Enter_nonEdivs = tk.Entry(self.top)
        self.Entry_Enter_nonEdivs.place(x=260, y=225, height=40, width=214)
        self.Entry_Enter_nonEdivs.configure(background="white")
        self.Entry_Enter_nonEdivs.configure(disabledforeground="#a3a3a3")
        self.Entry_Enter_nonEdivs.configure(font="-family {Malgun Gothic} -size 10")
        self.Entry_Enter_nonEdivs.configure(foreground="#000000")
        self.Entry_Enter_nonEdivs.configure(highlightbackground="#d9d9d9")
        self.Entry_Enter_nonEdivs.configure(highlightcolor="black")
        self.Entry_Enter_nonEdivs.configure(insertbackground="black")
        self.Entry_Enter_nonEdivs.configure(selectbackground="blue")
        self.Entry_Enter_nonEdivs.configure(selectforeground="white")
        self.Entry_Enter_nonEdivs.insert(0,0)

        self.Entry_Enter_Tuition = tk.Entry(self.top)
        self.Entry_Enter_Tuition.place(x=260, y=300, height=40, width=214)
        self.Entry_Enter_Tuition.configure(background="white")
        self.Entry_Enter_Tuition.configure(disabledforeground="#a3a3a3")
        self.Entry_Enter_Tuition.configure(font="-family {Malgun Gothic} -size 10")
        self.Entry_Enter_Tuition.configure(foreground="#000000")
        self.Entry_Enter_Tuition.configure(highlightbackground="#d9d9d9")
        self.Entry_Enter_Tuition.configure(highlightcolor="black")
        self.Entry_Enter_Tuition.configure(insertbackground="black")
        self.Entry_Enter_Tuition.configure(selectbackground="blue")
        self.Entry_Enter_Tuition.configure(selectforeground="white")
        self.Entry_Enter_Tuition.insert(0,0)

        self.Label_Enter_Tuition = tk.Label(self.top)
        self.Label_Enter_Tuition.place(x=260, y=268, height=27, width=204)
        self.Label_Enter_Tuition.configure(activebackground="#f9f9f9")
        self.Label_Enter_Tuition.configure(activeforeground="#000000")
        self.Label_Enter_Tuition.configure(anchor='w')
        self.Label_Enter_Tuition.configure(background="#ffffff")
        self.Label_Enter_Tuition.configure(compound='left')
        self.Label_Enter_Tuition.configure(disabledforeground="#a3a3a3")
        self.Label_Enter_Tuition.configure(font="-family {Malgun Gothic} -size 9")
        self.Label_Enter_Tuition.configure(foreground="#230046")
        self.Label_Enter_Tuition.configure(highlightbackground="#d9d9d9")
        self.Label_Enter_Tuition.configure(highlightcolor="black")
        self.Label_Enter_Tuition.configure(text='''Enter tuition paid:''')

        self.Label_Enter_Dono = tk.Label(self.top)
        self.Label_Enter_Dono.place(x=30, y=345, height=27, width=204)
        self.Label_Enter_Dono.configure(activebackground="#f9f9f9")
        self.Label_Enter_Dono.configure(activeforeground="#000000")
        self.Label_Enter_Dono.configure(anchor='w')
        self.Label_Enter_Dono.configure(background="#ffffff")
        self.Label_Enter_Dono.configure(compound='left')
        self.Label_Enter_Dono.configure(disabledforeground="#a3a3a3")
        self.Label_Enter_Dono.configure(font="-family {Malgun Gothic} -size 9")
        self.Label_Enter_Dono.configure(foreground="#230046")
        self.Label_Enter_Dono.configure(highlightbackground="#d9d9d9")
        self.Label_Enter_Dono.configure(highlightcolor="black")
        self.Label_Enter_Dono.configure(text='''Enter charitable donations:''')

        self.Entry_Enter_Dono = tk.Entry(self.top)
        self.Entry_Enter_Dono.place(x=30, y=375, height=40, width=214)
        self.Entry_Enter_Dono.configure(background="white")
        self.Entry_Enter_Dono.configure(disabledforeground="#a3a3a3")
        self.Entry_Enter_Dono.configure(font="-family {Malgun Gothic} -size 10")
        self.Entry_Enter_Dono.configure(foreground="#000000")
        self.Entry_Enter_Dono.configure(highlightbackground="#d9d9d9")
        self.Entry_Enter_Dono.configure(highlightcolor="black")
        self.Entry_Enter_Dono.configure(insertbackground="black")
        self.Entry_Enter_Dono.configure(selectbackground="blue")
        self.Entry_Enter_Dono.configure(selectforeground="white")
        self.Entry_Enter_Dono.insert(-1,0)

        self.Label_Enter_sin = tk.Label(self.top)
        self.Label_Enter_sin.place(x=265, y=425, height=27, width=204)
        self.Label_Enter_sin.configure(activebackground="#f9f9f9")
        self.Label_Enter_sin.configure(activeforeground="#000000")
        self.Label_Enter_sin.configure(anchor='w')
        self.Label_Enter_sin.configure(background="#ffffff")
        self.Label_Enter_sin.configure(compound='left')
        self.Label_Enter_sin.configure(disabledforeground="#a3a3a3")
        self.Label_Enter_sin.configure(font="-family {Malgun Gothic} -size 9 -weight bold")
        self.Label_Enter_sin.configure(foreground="#230046")
        self.Label_Enter_sin.configure(highlightbackground="#d9d9d9")
        self.Label_Enter_sin.configure(highlightcolor="black")
        self.Label_Enter_sin.configure(text='''Enter SIN:''')

        self.Entry_Enter_sin = tk.Entry(self.top)
        self.Entry_Enter_sin.place(x=265, y=450, height=40, width=214)
        self.Entry_Enter_sin.configure(background="white")
        self.Entry_Enter_sin.configure(disabledforeground="#a3a3a3")
        self.Entry_Enter_sin.configure(font="-family {Malgun Gothic} -size 10")
        self.Entry_Enter_sin.configure(foreground="#000000")
        self.Entry_Enter_sin.configure(highlightbackground="#d9d9d9")
        self.Entry_Enter_sin.configure(highlightcolor="black")
        self.Entry_Enter_sin.configure(insertbackground="black")
        self.Entry_Enter_sin.configure(selectbackground="blue")
        self.Entry_Enter_sin.configure(selectforeground="white")

        self.saveButton = tk.Button(self.top)
        self.saveButton.place(x=265, y=450, height=0, width=0)
        self.saveButton.configure(activebackground="#ececec")
        self.saveButton.configure(activeforeground="#000000")
        self.saveButton.configure(background="#690f96")
        self.saveButton.configure(compound='left')
        self.saveButton.configure(disabledforeground="#a3a3a3")
        self.saveButton.configure(font="-family {Malgun Gothic} -size 11 -weight bold")
        self.saveButton.configure(foreground="#ffffff")
        self.saveButton.configure(highlightbackground="#d9d9d9")
        self.saveButton.configure(highlightcolor="black")
        self.saveButton.configure(pady="0")
        self.saveButton.configure(text='''Save''')
        self.saveButton.configure(command=self.saveData)

        self.loadButton = tk.Button(self.top)
        self.loadButton.place(x=510, y=450, height=44, width=127)
        self.loadButton.configure(activebackground="#ececec")
        self.loadButton.configure(activeforeground="#000000")
        self.loadButton.configure(background="#690f96")
        self.loadButton.configure(compound='left')
        self.loadButton.configure(disabledforeground="#a3a3a3")
        self.loadButton.configure(font="-family {Malgun Gothic} -size 11 -weight bold")
        self.loadButton.configure(foreground="#ffffff")
        self.loadButton.configure(highlightbackground="#d9d9d9")
        self.loadButton.configure(highlightcolor="black")
        self.loadButton.configure(pady="0")
        self.loadButton.configure(text='''Load''')
        self.loadButton.configure(command=self.loadData)

        self.Combo_Enter_Province = ttk.Combobox(self.top)
        self.Combo_Enter_Province.place(x=260, y=80, height=31, width=143)
        self.value_list = ['Alberta', 'British Columbia', 'Manitoba', 'New Brunswick'
        , 'Newfoundland', 'Nova Scotia', 'Ontario', 'Prince Edward Island',
         'Quebec','Saskatchewan']
        self.Combo_Enter_Province.configure(values=self.value_list)
        self.Combo_Enter_Province.configure(textvariable=self.combobox)
        self.Combo_Enter_Province.configure(takefocus="")
        self.Combo_Enter_Province.configure(cursor="fleur")
        self.Combo_Enter_Province.insert(END,"Ontario")

        self.fedIncome = [14398,50197,100392,155625,221708]
        self.fedBracket = [0,0.15,0.205,0.26,0.29,0.33]

        self.Dono = 200
        self.fedDonoBracket =[0.15,0.29]

        self.fedEdivTaxCred = 0.150198
        self.grossUpEdiv = 1.38

        self.fedNonEdivTaxCred = 0.090301
        self.grossUpNonEdiv = 1.15

        self.fedTuTaxCred = 0.15

        self.albIncome = [19369, 131220, 157464, 209952,314929]
        self.albBracket = [0,0.1,.12,.13,.14,.15]
        self.albEdivTaxCred = 0.0812
        self.albNonEdivTaxCred = 0.0218
        self.albDonoBracket = [0.1,0.21]

        self.bcIncome = [11302,43070,86141,98901,120094,162832,227091]
        self.bcBracket = [0,0.0506,0.077,0.105,0.1229,0.147,0.168,0.205]
        self.bcEdivTaxCred = 0.12
        self.bcNonEdivTaxCred = 0.0196
        self.bcDonoBracket =[0.0506,0.1680]

        self.manIncome = [10145,34431,74416]
        self.manBracket = [0,0.108,0.1275,0.174]
        self.manEdivTaxCred = 0.08
        self.manNonEdivTaxCred = 0.007835
        self.manDonoBracket = [0.1080,0.1740]

        self.nbIncome = [10817,44887,89775,145995,166280]
        self.nbBracket = [0,0.094,0.1482,0.1652,0.1784,0.203]
        self.nbEdivTaxCred = 0.14
        self.nbNonEdivTaxCred = 0.0275
        self.nbDonoBracket = [0.0968,0.1795]

        self.nfIncome = [9804,39147,78294,139780,195693,250000,500000,1000000]
        self.nfBracket = [0,0.087,0.145,0.156,0.178,0.198,0.208,0.213,0.218]
        self.nfEdivTaxCred = 0.063
        self.nfNonEdivTaxCred = 0.032
        self.nfDonoBracket = [0.0870,0.1830]

        self.nsIncome = [11481,29590,59180,93000,150000]
        self.nsBracket = [0,0.0879,0.1495,0.1667,0.175,0.21]
        self.nsEdivTaxCred  = 0.0885
        self.nsNonEdivTaxCred = 0.0299
        self.nsDonoBracket = [0.0879,0.21]

        self.ontIncome = [11141,46226,92454,150000,220000]
        self.ontBracket = [0,0.0505,0.0915,0.1116,0.1216,0.1316]
        self.ontEdivTaxCred = 0.10
        self.ontNonEdivTaxCred = 0.029836
        self.ontDonoBracket = [0.0505,0.1116]

        self.peiIncome = [11250,31984,63696]
        self.peiBracket = [0,0.098,0.138,0.167]
        self.peiEdivTaxCred = 0.105
        self.peiNonEdivTaxCred = 0.0130
        self.peiDonoBracket = [0.098,0.1670]

        self.quIncome = [16143,46295,92580,112655]
        self.quBracket = [0,0.15,0.20,0.24,0.2575]
        self.quEdivTaxCred =0.1170
        self.quNonEdivTaxCred = 0.0342
        self.quDonoBracket = [0.20,0.24]

        self.sasIncome = [16615,46773,133638]
        self.sasBracket =[0,0.105,0.125,0.145]
        self.sasEdivTaxCred = 0.1202
        self.sasNonEdivTaxCred = 0.02105
        self.sasDonoBracket = [0.1050,0.1450]


    def getInput(self):

        try:
            income = float(self.Entry_Enter_Income.get())
            province = self.Combo_Enter_Province.get()
            rrsp = float(self.Entry_Enter_rrsp.get())
            taxPaid = float(self.Entry_Enter_taxPaid.get())
            capGains = float(self.Entry_Enter_capGains.get())
            eDivs = float(self.Entry_Enter_eDivs.get())
            nonEdivs = float(self.Entry_Enter_nonEdivs.get())
            tuitionPaid = float(self.Entry_Enter_Tuition.get())
            donos = float(self.Entry_Enter_Dono.get())
        except:
            messagebox.showerror("Invalid Inputs", "Please enter valid inputs")


        self.calcOutput(income,province,rrsp,taxPaid,capGains,eDivs,nonEdivs,tuitionPaid,donos)
        return income,province,rrsp,taxPaid,capGains,eDivs,nonEdivs,tuitionPaid,donos

    def calcOutput(self,income,province,rrsp,taxPaid,capGains,eDivs,nonEdivs,tuitionPaid,donos):

        income -= rrsp
        income+=capGains/2
        income+=(eDivs*self.grossUpEdiv)
        income+=(nonEdivs*self.grossUpNonEdiv)

        self.textBox_Federal_Tax.delete('1.0', END)
        fedTax = calcTax(income,self.fedIncome,self.fedBracket)
        fedTax = round(fedTax,2)

        if province == 'Alberta':
            provIncome, provBracket = self.albIncome, self.albBracket
            eDivTaxCred = self.albEdivTaxCred
            nonEdivTaxCred = self.albNonEdivTaxCred
            nonEdivTaxCred = self.albNonEdivTaxCred
            provDonoBracket = self.albDonoBracket

        if province == 'British Columbia':
            provIncome, provBracket = self.bcIncome, self.bcBracket
            eDivTaxCred = self.bcEdivTaxCred
            nonEdivTaxCred = self.bcNonEdivTaxCred
            provDonoBracket = self.bcDonoBracket

        if province == 'Manitoba':
            provIncome, provBracket = self.manIncome, self.manBracket
            eDivTaxCred = self.manEdivTaxCred
            nonEdivTaxCred = self.manNonEdivTaxCred
            provDonoBracket = self.manDonoBracket

        if province == 'New Brunswick':
            provIncome, provBracket = self.nbIncome, self.nbBracket
            eDivTaxCred = self.nbEdivTaxCred
            nonEdivTaxCred = self.nbNonEdivTaxCred
            provDonoBracket = self.nbDonoBracket

        if province == 'Newfoundland':
            provIncome, provBracket = self.nfIncome, self.nfBracket
            eDivTaxCred = self.nfEdivTaxCred
            nonEdivTaxCred = self.nfNonEdivTaxCred
            provDonoBracket = self.nfDonoBracket

        if province == 'Nova Scotia':
            provIncome, provBracket = self.nsIncome, self.nsBracket
            eDivTaxCred = self.nsEdivTaxCred
            nonEdivTaxCred = self.nsNonEdivTaxCred
            provDonoBracket = self.nsDonoBracket

        if province == 'Ontario':
            provIncome, provBracket = self.ontIncome, self.ontBracket
            eDivTaxCred = self.ontEdivTaxCred
            nonEdivTaxCred = self.ontNonEdivTaxCred
            provDonoBracket = self.ontDonoBracket

        if province == 'Prince Edward Island':
            provIncome, provBracket = self.peiIncome, self.peiBracket
            eDivTaxCred = self.peiEdivTaxCred
            nonEdivTaxCred = self.peiNonEdivTaxCred
            provDonoBracket = self.peiDonoBracket

        if province == 'Quebec':
            provIncome, provBracket = self.quIncome, self.quBracket
            eDivTaxCred = self.quEdivTaxCred
            nonEdivTaxCred = self.quNonEdivTaxCred
            provDonoBracket = self.quDonoBracket

        if province == 'Saskatchewan':
            provIncome, provBracket = self.sasIncome, self.sasBracket
            eDivTaxCred = self.sasEdivTaxCred
            nonEdivTaxCred = self.sasNonEdivTaxCred
            provDonoBracket = self.sasDonoBracket


        self.textBox_Provincial_Tax.delete('1.0', END)
        try:
            provTax = calcTax(income,provIncome,provBracket)
        except:
            messagebox.showerror("Invalid Inputs", "Please enter valid inputs")

        provTax = round(provTax,2)
        self.textBox_Provincial_Tax.config(state="normal")
        self.textBox_Provincial_Tax.delete('1.0', END)
        self.textBox_Provincial_Tax.insert(END,"$" + str(provTax))
        self.textBox_Provincial_Tax.config(state="disabled")
        self.textBox_Federal_Tax.config(state="normal")
        self.textBox_Federal_Tax.delete('1.0', END)
        self.textBox_Federal_Tax.insert(END,"$" + str(fedTax))
        self.textBox_Federal_Tax.config(state="disabled")

        eDivsCreditFed = calcTaxCredit(eDivs,self.grossUpEdiv,self.fedEdivTaxCred)
        eDivsCreditProv = calcTaxCredit(eDivs,self.grossUpEdiv,eDivTaxCred)
        eDivsCreditTotal = eDivsCreditFed + eDivsCreditProv

        nonEdivsCreditFed = calcTaxCredit(nonEdivs,self.grossUpNonEdiv,self.fedNonEdivTaxCred)
        nonEdivsCreditProv = calcTaxCredit(nonEdivs,self.grossUpNonEdiv,nonEdivTaxCred)
        nonEdivsCreditTotal = nonEdivsCreditFed + nonEdivsCreditProv

        tuitionCredit = calcTuitionCredit(tuitionPaid,self.fedTuTaxCred)

        donoCreditFed = calcDonoCredit(donos,self.Dono,self.fedDonoBracket)
        donoCreditProv = calcDonoCredit(donos,self.Dono,provDonoBracket)
        totalDonoCredit = donoCreditFed + donoCreditProv

        totalTax = fedTax + provTax
        totalTax -= taxPaid
        totalTax -= eDivsCreditTotal
        totalTax -= nonEdivsCreditTotal
        totalTax -= tuitionCredit
        totalTax -= totalDonoCredit
        totalTax = round(totalTax,2)

        eDivsCreditTotal = round(eDivsCreditTotal,2)
        self.textBox_eDiv.config(state="normal")
        self.textBox_eDiv.delete('1.0', END)
        self.textBox_eDiv.insert(END,"$" + str(eDivsCreditTotal))
        self.textBox_eDiv.config(state="disabled")


        nonEdivsCreditTotal = round(nonEdivsCreditTotal,2)
        self.textBox_nonEdiv.config(state="normal")
        self.textBox_nonEdiv.delete('1.0', END)
        self.textBox_nonEdiv.insert(END,"$" + str(nonEdivsCreditTotal))
        self.textBox_nonEdiv.config(state="disabled")


        tuitionCredit = round(tuitionCredit,2)
        self.textBox_Tuition_Credit.config(state="normal")
        self.textBox_Tuition_Credit.delete('1.0', END)
        self.textBox_Tuition_Credit.insert(END,"$" + str(tuitionCredit))
        self.textBox_Tuition_Credit.config(state="disabled")


        totalDonoCredit = round(totalDonoCredit,2)
        self.textBox_Dono_Credit.config(state="normal")
        self.textBox_Dono_Credit.delete('1.0', END)
        self.textBox_Dono_Credit.insert(END,"$" + str(totalDonoCredit))
        self.textBox_Dono_Credit.config(state="disabled")

        if totalTax > 0:

            self.textBox_Total_Tax.configure(foreground="red")
            self.Label_Total_Tax.configure(text='''Total tax due''')
            totalTax = "{:,}".format(totalTax)
            self.textBox_Total_Tax.config(state="normal")
            self.textBox_Total_Tax.delete('1.0', END)
            self.textBox_Total_Tax.insert(END,"-"+"$" + str(totalTax))
            self.textBox_Total_Tax.config(state="disabled")

        else:

            self.textBox_Total_Tax.configure(foreground="green")
            self.Label_Total_Tax.configure(text='''Total tax return''')
            totalTax = "{:,}".format(totalTax)
            totalTax = str(totalTax)
            totalTax = totalTax.replace("-","")
            self.textBox_Total_Tax.config(state="normal")
            self.textBox_Total_Tax.delete('1.0', END)
            self.textBox_Total_Tax.insert(END,"$" + totalTax)
            self.textBox_Total_Tax.config(state="disabled")


        self.saveButton.place(x=650, y=450, height=44, width=127)

        return totalTax

    def saveData(self):

        data = self.getInput()

        try:
            sin = int(self.Entry_Enter_sin.get())

        except:
            messagebox.showerror("Invalid Inputs", "Please enter a valid SIN")


        if len(str(sin)) == 9:
            sin = int(self.Entry_Enter_sin.get())
        else:
            sin = ""
            messagebox.showerror("Invalid Inputs", "Please enter a valid SIN")
            return


        try:
            if messagebox.askyesno("Are you sure?", "Are you sure you want to save?"):
                sqliteConnection = sqlite3.connect('data.db')
                cur = sqliteConnection.cursor()


                cur.execute("insert or replace into DATA values (?,?,?,?,?,?,?,?,?,?)",
                (sin,data[0],data[1],data[2],data[5],data[6],data[3],data[4],data[7],data[8]))
                sqliteConnection.commit()
                messagebox.showinfo("Entry saved","Your information has been updated")


        except:
            messagebox.showerror("Error!","Entry failed to update")

    def loadData(self):


        try:
            sin = int(self.Entry_Enter_sin.get())

        except:
            messagebox.showerror("Invalid Inputs", "Please enter a valid SIN")


        if len(str(sin)) == 9:
            sin = int(self.Entry_Enter_sin.get())
        else:
            sin = ""
            messagebox.showerror("Invalid Inputs", "Please enter a valid SIN")
            return

        try:
            sqliteConnection = sqlite3.connect('data.db')
            cur = sqliteConnection.cursor()
            cur.execute("select * from DATA where SIN =?",
            (sin,))

            rows = cur.fetchall()

            reInsert = self.Entry_Enter_Income.get()
            self.Entry_Enter_Income.delete("0", "end")
            self.Entry_Enter_Income.insert(0,rows[0][1])

            self.Combo_Enter_Province.delete("0", "end")
            self.Combo_Enter_Province.insert(0,rows[0][2])

            self.Entry_Enter_rrsp.delete("0", "end")
            self.Entry_Enter_rrsp.insert(0,rows[0][3])

            self.Entry_Enter_eDivs.delete("0", "end")
            self.Entry_Enter_eDivs.insert(0,rows[0][4])

            self.Entry_Enter_nonEdivs.delete("0", "end")
            self.Entry_Enter_nonEdivs.insert(0,rows[0][5])

            self.Entry_Enter_taxPaid.delete("0", "end")
            self.Entry_Enter_taxPaid.insert(0,rows[0][6])

            self.Entry_Enter_capGains.delete("0", "end")
            self.Entry_Enter_capGains.insert(0,rows[0][7])

            self.Entry_Enter_Tuition.delete("0", "end")
            self.Entry_Enter_Tuition.insert(0,rows[0][8])

            self.Entry_Enter_Dono.delete("0", "end")
            self.Entry_Enter_Dono.insert(0,rows[0][9])


            self.getInput()
            messagebox.showinfo("Sucess","Data loaded sucessfully")


        except:
            messagebox.showerror("Data failed to load","SIN not in database!")
            self.Entry_Enter_Income.insert(0,reInsert)

def start_up():
    taxProject_support.main()

if __name__ == '__main__':
    taxProject_support.main()
