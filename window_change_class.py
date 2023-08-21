from tkinter import ttk, Tk, Frame, Label, Entry, StringVar, Button, Toplevel
from functools import partial
from pandas import read_csv


class ChangeClass(Toplevel):
    def __init__(self, master, func):
        super().__init__(master)
        self.ui = 2

        self.title("Change class")
        self.minsize(200, 100)

        self.func = func

        self.class_df = read_csv('tables/classes.csv', sep=';')

        self.grid = Frame(self)
        self.grid.pack(fill='both', padx=10, pady=10)

        for index, row in self.class_df.iterrows():
            desc = str(row['Klasa'])

            frame_class = Frame(self.grid)
            frame_class.pack(fill='x', padx=self.ui, pady=self.ui)
            label_class = Label(frame_class, text=desc)
            label_class.pack(side='left', fill='both', padx=self.ui, pady=self.ui)
            button_class = Button(frame_class, text='Zmień', command=partial(self.call_change, row['Klasa']))
            button_class.pack(side='right', fill='both', padx=self.ui, pady=self.ui)

    def call_change(self, name):
        self.func(name)
        self.destroy()
