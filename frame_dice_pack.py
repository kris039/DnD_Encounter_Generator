import random
from tkinter import ttk, Tk, Frame, Label, Entry, Spinbox, StringVar, Button


class DicePack(Frame):
    def __init__(self, master, add):
        super().__init__(master)
        self.ui_spacing = 2

        self.add = add

        self.grid = Frame(self)
        self.grid.pack()

        self.d2 = Button(self.grid, text='D2', command=self.call_d2)
        self.d2.grid(row=0, column=0, padx=self.ui_spacing, pady=self.ui_spacing, sticky='we')
        self.d4 = Button(self.grid, text='D4', command=self.call_d4)
        self.d4.grid(row=0, column=1, padx=self.ui_spacing, pady=self.ui_spacing, sticky='we')
        self.d6 = Button(self.grid, text='D6', command=self.call_d6)
        self.d6.grid(row=0, column=2, padx=self.ui_spacing, pady=self.ui_spacing, sticky='we')
        self.d8 = Button(self.grid, text='D8', command=self.call_d8)
        self.d8.grid(row=0, column=3, padx=self.ui_spacing, pady=self.ui_spacing, sticky='we')
        self.d10 = Button(self.grid, text='D10', command=self.call_d10)
        self.d10.grid(row=1, column=0, padx=self.ui_spacing, pady=self.ui_spacing, sticky='we')
        self.d12 = Button(self.grid, text='D12', command=self.call_d12)
        self.d12.grid(row=1, column=1, padx=self.ui_spacing, pady=self.ui_spacing, sticky='we')
        self.d20 = Button(self.grid, text='D20', command=self.call_d20)
        self.d20.grid(row=1, column=2, padx=self.ui_spacing, pady=self.ui_spacing, sticky='we')
        self.d100 = Button(self.grid, text='D100', command=self.call_d100)
        self.d100.grid(row=1, column=3, padx=self.ui_spacing, pady=self.ui_spacing, sticky='we')

    def call_d2(self):
        self.add('\nWolny rzut kością D2: ' + str((random.randint(1, 2))))

    def call_d4(self):
        self.add('\nWolny rzut kością D4: ' + str((random.randint(1, 4))))

    def call_d6(self):
        self.add('\nWolny rzut kością D6: ' + str((random.randint(1, 6))))

    def call_d8(self):
        self.add('\nWolny rzut kością D8: ' + str((random.randint(1, 8))))

    def call_d10(self):
        self.add('\nWolny rzut kością D10: ' + str((random.randint(1, 10))))

    def call_d12(self):
        self.add('\nWolny rzut kością D12: ' + str((random.randint(1, 12))))

    def call_d20(self):
        self.add('\nWolny rzut kością D20: ' + str((random.randint(1, 20))))

    def call_d100(self):
        self.add('\nWolny rzut kością D100: ' + str((random.randint(1, 100))))
