from tkinter import ttk, Tk, Frame, Label, Entry, StringVar, Button, Toplevel, Scrollbar, Canvas
from window_add_info import AddInfo
from window_change_weapon import ChangeWeapon
from window_change_class import ChangeClass
from pandas import DataFrame
from functools import partial


class CharacterInfo(Toplevel):
    def __init__(self, master, change_class_func, change_level_func, change_weapon_func, add_info_func,
                 classs, level, att1, att2, additional=DataFrame()):
        super().__init__(master)
        self.ui = 2

        self.title("Character info")
        self.minsize(200, 200)
        self.resizable(False, True)

        self.grid = ttk.Frame(self)
        self.grid.pack(side='left', fill='both', padx=10, pady=10)

        self.change_class_func = change_class_func
        self.change_level_func = change_level_func
        self.change_weapon_func = change_weapon_func
        self.add_info_func = add_info_func
        self.additional = additional
        self.classs = StringVar()
        self.level = StringVar()
        self.att1 = StringVar()
        self.att2 = StringVar()
        self.perks = StringVar()
        self.spells = StringVar()
        self.item = StringVar()

        self.classs.set(classs)
        self.level.set(level)
        self.att1.set(att1)
        self.att2.set(att2)

        self.frame_basic_info = Frame(self.grid)
        self.frame_basic_info.pack(expand=True, padx=self.ui, pady=self.ui)
        self.title_class = Label(self.frame_basic_info, text='Klasa:')
        self.title_class.grid(row=0, column=0, sticky='we', padx=self.ui, pady=self.ui)
        self.label_class = Label(self.frame_basic_info, textvariable=self.classs)
        self.label_class.grid(row=0, column=1, sticky='we', padx=self.ui, pady=self.ui)
        self.button_class = Button(self.frame_basic_info, text='Zmień', command=self.call_change_class)
        self.button_class.grid(row=0, column=2, sticky='we', padx=self.ui, pady=self.ui)
        self.title_level = Label(self.frame_basic_info, text='Poziom:')
        self.title_level.grid(row=1, column=0, sticky='we', padx=self.ui, pady=self.ui)
        self.label_level = Label(self.frame_basic_info, textvariable=self.level)
        self.label_level.grid(row=1, column=1, sticky='we', padx=self.ui, pady=self.ui)
        self.button_level = Button(self.frame_basic_info, text='Zmień', command=self.call_change_weapon)
        self.button_level.grid(row=1, column=2, sticky='we', padx=self.ui, pady=self.ui)
        self.title_w1 = Label(self.frame_basic_info, text='Broń 1:')
        self.title_w1.grid(row=2, column=0, sticky='we', padx=self.ui, pady=self.ui)
        self.label_w1 = Label(self.frame_basic_info, textvariable=self.att1)
        self.label_w1.grid(row=2, column=1, sticky='we', padx=self.ui, pady=self.ui)
        self.button_w1 = Button(self.frame_basic_info, text='Zmień', command=partial(self.call_change_weapon, 1))
        self.button_w1.grid(row=2, column=2, sticky='we', padx=self.ui, pady=self.ui)
        self.title_w2 = Label(self.frame_basic_info, text='Broń 2:')
        self.title_w2.grid(row=3, column=0, sticky='we', padx=self.ui, pady=self.ui)
        self.label_w2 = Label(self.frame_basic_info, textvariable=self.att2)
        self.label_w2.grid(row=3, column=1, sticky='we', padx=self.ui, pady=self.ui)
        self.button_w2 = Button(self.frame_basic_info, text='Zmień', command=partial(self.call_change_weapon, 2))
        self.button_w2.grid(row=3, column=2, columnspan=2, sticky='we', padx=self.ui, pady=self.ui)

        self.sep = ttk.Separator(self.grid, orient='horizontal')
        self.sep.pack(fill='x', padx=self.ui, pady=self.ui)

        self.frame_perks = Frame(self.grid)
        self.frame_perks.pack(fill='both', padx=self.ui, pady=self.ui)
        self.title_perks = Label(self.frame_perks, text='Atuty')
        self.title_perks.pack(side='left', fill='both', padx=self.ui, pady=self.ui)
        self.button_perks = Button(self.frame_perks, text='Dodaj atuty', command=self.call_add_perk)
        self.button_perks.pack(side='right', fill='both', padx=self.ui, pady=self.ui)
        self.label_perks = Label(self.grid, textvariable=self.perks)
        self.label_perks.pack(fill='both', padx=self.ui, pady=self.ui)

        self.sep = ttk.Separator(self.grid, orient='horizontal')
        self.sep.pack(fill='x', padx=self.ui, pady=self.ui)

        self.frame_spells = Frame(self.grid)
        self.frame_spells.pack(fill='both', padx=self.ui, pady=self.ui)
        self.title_spells = Label(self.frame_spells, text='Zaklęcia')
        self.title_spells.pack(side='left', fill='both', padx=self.ui, pady=self.ui)
        self.button_spells = Button(self.frame_spells, text='Dodaj zaklęcia', command=self.call_add_skill)
        self.button_spells.pack(side='right', fill='both', padx=self.ui, pady=self.ui)
        self.label_spells = Label(self.grid, textvariable=self.spells)
        self.label_spells.pack(fill='both', padx=self.ui, pady=self.ui)

        self.sep = ttk.Separator(self.grid, orient='horizontal')
        self.sep.pack(fill='x', padx=self.ui, pady=self.ui)

        self.frame_item = Frame(self.grid)
        self.frame_item.pack(fill='both', padx=self.ui, pady=self.ui)
        self.title_item = Label(self.frame_item, text='Przedmioty')
        self.title_item.pack(side='left', fill='both', padx=self.ui, pady=self.ui)
        self.button_item = Button(self.frame_item, text='Dodaj przedmioty', command=self.call_add_item)
        self.button_item.pack(side='right', fill='both', padx=self.ui, pady=self.ui)
        self.label_item = Label(self.grid, textvariable=self.item)
        self.label_item.pack(fill='both', padx=self.ui, pady=self.ui)

        self.display_additional()

    def display_additional(self):
        perk_str = '\n'
        spell_str = '\n'
        item_str = '\n'
        for index, row in self.additional.iterrows():
            # print(row)
            if row.loc['Typ'] == 'Atut':
                perk_str += (str(row['Nazwa']) + ' -> ' + str(row['Info'])
                             + '\n\tAtt mod/Dmg mod -> ' + str(row['Att_mod']) + '/' + str(row['Dmg_mod']) + '\n\n')
            elif row.loc['Typ'] == 'Zaklęcie':
                spell_str += row + 'W.I.P.'
            else:
                item_str += (str(row['Nazwa']) + ' -> ' + str(row['Info']) + '\n\n')

            self.perks.set(perk_str)
            self.spells.set(spell_str)
            self.item.set(item_str)

    def call_change_class(self):
        win = ChangeClass(self, self.change_class)

    def change_class(self, classs):
        self.classs.set(classs)
        self.change_class_func(self.classs.get())

    def call_change_weapon(self, num):
        win = ChangeWeapon(self, self.change_weapon, num)

    def change_weapon(self, name, num):
        if num == 1:
            self.att1.set(name)
        elif num == 2:
            self.att2.set(name)
        self.change_weapon_func(self.att1.get(), self.att2.get())

    def call_add_perk(self):
        win = AddInfo(self, self.add_info, 'perk')

    def call_add_skill(self):
        print('W.I.P.')

    def call_add_item(self):
        win = AddInfo(self, self.add_info, 'item')

    def add_info(self, row):
        self.additional = self.additional.append(row)
        self.add_info_func(row)
        self.display_additional()



