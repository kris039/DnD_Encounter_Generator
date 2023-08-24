from tkinter import ttk, Tk, Frame, Label, Entry, StringVar, Button, Toplevel
from functools import partial
from pandas import read_csv


class ChangeWeapon(Toplevel):
    def __init__(self, master, func, num=1):
        super().__init__(master)
        self.ui = 2
        self.height_limit = 15

        self.title("Change weapon")
        self.minsize(200, 100)
        self.resizable(False, False)

        self.func = func
        self.num = num

        self.weapon_df = read_csv('resources/weapons.csv', sep=';')

        self.grid = Frame(self)
        self.grid.pack(fill='both', padx=10, pady=10)

        self.x = 0
        self.y = 0
        for index, row in self.weapon_df.iterrows():
            desc = ''
            desc += str(row['Nazwa']) + ' -> ' + str(row['Obrażenia']) + str(row['Kryt_próg']) + str(row['Kryt_mnożnik'])

            frame_weapon = Frame(self.grid)
            frame_weapon.grid(column=self.x, row=self.y, sticky='we', padx=self.ui, pady=self.ui)
            label_weapon = Label(frame_weapon, text=desc)
            label_weapon.pack(side='left', fill='both', padx=self.ui, pady=self.ui)
            button_weapon = Button(frame_weapon, text='Wybierz', command=partial(self.call_change, row['Nazwa']))
            button_weapon.pack(side='right', padx=self.ui, pady=self.ui)
            if self.y >= self.height_limit:
                self.x += 1
                self.y = 0
            else:
                self.y += 1

    def call_change(self, name):
        self.func(name, self.num)
        self.destroy()
