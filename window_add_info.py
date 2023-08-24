from tkinter import ttk, Tk, Frame, Label, Entry, StringVar, Button, Toplevel
from functools import partial
from pandas import read_csv


class AddInfo(Toplevel):
    def __init__(self, master, func, info_type):
        super().__init__(master)
        self.ui = 2
        self.height_limit = 15

        self.title("Add info")
        self.minsize(200, 100)

        self.func = func

        if info_type == 'Atut':
            self.info_df = read_csv('tables/perks.csv', sep=';')
        elif info_type == 'Czar':
            self.info_df = read_csv('tables/spells.csv', sep=';')
        else:
            self.info_df = read_csv('tables/consumables.csv', sep=';')

        self.grid = Frame(self)
        self.grid.pack(fill='both', padx=10, pady=10)

        self.x = 0
        self.y = 0
        for index, row in self.info_df.iterrows():
            desc = ''
            if info_type == 'Atut':
                desc += str(row['Nazwa']) + ' -> ' + str(row['Info'])
                desc += '\tAtt mod/Dmg mod -> ' + str(row['Att_mod']) + '/' + str(row['Dmg_mod'])
            elif info_type == 'Czar':
                desc = str(row['Klasa']) + ' - ' + str(row['Nazwa']) + ' -> ' + str(row['Info'])
            else:
                desc = str(row['Nazwa']) + ' -> ' + str(row['Info'])

            frame_item = Frame(self.grid)
            frame_item.grid(column=self.x, row=self.y, sticky='we', padx=self.ui, pady=self.ui)
            label_item = Label(frame_item, text=desc)
            label_item.pack(side='left', fill='both', padx=self.ui, pady=self.ui)
            button_item = Button(frame_item, text='Dodaj', command=partial(self.func, row['ID'], info_type))
            button_item.pack(side='right', padx=self.ui, pady=self.ui)
            if self.y >= self.height_limit:
                self.x += 1
                self.y = 0
            else:
                self.y += 1
