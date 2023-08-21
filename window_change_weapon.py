from tkinter import ttk, Tk, Frame, Label, Entry, StringVar, Button, Toplevel
from functools import partial
from pandas import read_csv


class ChangeWeapon(Toplevel):
    def __init__(self, master, func, num=1):
        super().__init__(master)
        self.ui = 2

        self.title("Change weapon")
        self.minsize(200, 100)

        self.func = func
        self.num = num

        self.weapon_df = read_csv('tables/weapons.csv', sep=';')

        self.grid = Frame(self)
        self.grid.pack(fill='both', padx=10, pady=10)

        for index, row in self.weapon_df.iterrows():
            desc = ''
            desc += str(row['Nazwa']) + ' -> ' + str(row['Obrażenia']) + str(row['Kryt_próg']) + str(row['Kryt_mnożnik'])

            frame_weapon = Frame(self.grid)
            frame_weapon.pack(fill='x', padx=self.ui, pady=self.ui)
            label_weapon = Label(frame_weapon, text=desc)
            label_weapon.pack(side='left', fill='both', padx=self.ui, pady=self.ui)
            button_weapon = Button(frame_weapon, text='Zmień', command=partial(self.call_change, row['Nazwa']))
            button_weapon.pack(side='right', fill='both', padx=self.ui, pady=self.ui)

    def call_change(self, name):
        self.func(name, self.num)
        self.destroy()
