from tkinter import ttk, Tk, Frame, Label, Entry, StringVar, Button, Toplevel
from functools import partial
from pandas import read_csv


class AddInfo(Toplevel):
    def __init__(self, master, func, info_type):
        super().__init__(master)
        self.ui_spacing = 2

        self.title("Add info")
        self.minsize(200, 100)

        self.func = func

        if info_type == 'perk':
            self.info_df = read_csv('tables/perks.csv', sep=';')
        elif info_type == 'spell':
            pass
        else:
            self.info_df = read_csv('tables/consumables.csv', sep=';')

        self.grid = Frame(self)
        self.grid.pack(fill='both', padx=10, pady=10)

        for index, row in self.info_df.iterrows():
            desc = ''
            if info_type == 'perk':
                desc += str(row['Nazwa']) + ' -> ' + str(row['Info'])
                desc += '\tAtt mod/Dmg mod -> ' + str(row['Att_mod']) + '/' + str(row['Dmg_mod'])
            elif info_type == 'spell':
                pass
            else:
                desc = str(row['Nazwa']) + ' -> ' + str(row['Info'])

            frame_item = Frame(self.grid)
            frame_item.pack(fill='x', padx=self.ui_spacing, pady=self.ui_spacing)
            label_item = Label(frame_item, text=desc)
            label_item.pack(side='left', fill='both', padx=self.ui_spacing, pady=self.ui_spacing)
            button_item = Button(frame_item, text='Dodaj', command=partial(self.func, row))
            button_item.pack(side='right', fill='both', padx=self.ui_spacing, pady=self.ui_spacing)
