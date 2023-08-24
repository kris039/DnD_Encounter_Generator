from tkinter import ttk, Tk, Frame, Label, Entry, StringVar, Button, Toplevel, OptionMenu
from window_add_info import AddInfo
from window_change_weapon import ChangeWeapon
from back_adds_funtions import *
from pandas import DataFrame, read_csv
from functools import partial


class CharacterInfo(Toplevel):
    def __init__(self, master, change_class_func, change_level_func, change_weapon_func, get_info_funcs,
                 classs, level, att1, att2):
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
        self.info_funcs = get_info_funcs
        self.classs = StringVar()
        self.level = StringVar()
        self.att1 = StringVar()
        self.att2 = StringVar()
        self.perk_list = self.info_funcs()[0]()
        self.spell_list = self.info_funcs()[2]()
        self.item_list = self.info_funcs()[4]()
        self.perks = StringVar()
        self.spells = StringVar()
        self.item = StringVar()
        self.class_list = []
        self.fill_classes()

        self.classs.set(classs)
        self.level.set(level)
        self.att1.set(att1)
        self.att2.set(att2)

        self.frame_left = Frame(self.grid)
        self.frame_left.pack(side='left', padx=self.ui, pady=self.ui)
        self.frame_right = Frame(self.grid)
        self.frame_right.pack(side='right', padx=self.ui, pady=self.ui)

        self.frame_basic_info = Frame(self.frame_left, borderwidth=2, relief="groove")
        self.frame_basic_info.pack(padx=self.ui, pady=self.ui)
        self.title_class = Label(self.frame_basic_info, text='Klasa:')
        self.title_class.grid(row=0, column=0, sticky='we', padx=self.ui, pady=self.ui)
        self.label_class = OptionMenu(self.frame_basic_info, self.classs,
                                      *self.class_list, command=self.change_class_func)
        self.label_class.grid(row=0, column=1, columnspan=2, sticky='we', padx=self.ui, pady=self.ui)
        self.title_level = Label(self.frame_basic_info, text='Poziom:')
        self.title_level.grid(row=1, column=0, sticky='we', padx=self.ui, pady=self.ui)
        self.label_level = OptionMenu(self.frame_basic_info, self.level,
                                      *range(1, 21), command=self.change_level_func)
        self.label_level.grid(row=1, column=1, columnspan=2, sticky='we', padx=self.ui, pady=self.ui)
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

        self.frame_perks_q = Frame(self.frame_left, borderwidth=2, relief="groove")
        self.frame_perks_q.pack(fill='both', padx=self.ui, pady=self.ui)
        self.frame_perks = Frame(self.frame_perks_q)
        self.frame_perks.pack(fill='both', padx=self.ui, pady=self.ui)
        self.title_perks = Label(self.frame_perks, text='Atuty')
        self.title_perks.pack(side='left', fill='both', padx=self.ui, pady=self.ui)
        self.button_perks = Button(self.frame_perks, text='Dodaj atuty', command=self.call_add_perk)
        self.button_perks.pack(side='right', fill='both', padx=self.ui, pady=self.ui)
        self.label_perks = Label(self.frame_perks_q, textvariable=self.perks)
        self.label_perks.pack(fill='both', padx=self.ui, pady=self.ui)

        self.frame_spells_q = Frame(self.frame_right, borderwidth=2, relief="groove")
        self.frame_spells_q.pack(fill='both', padx=self.ui, pady=self.ui)
        self.frame_spells = Frame(self.frame_spells_q)
        self.frame_spells.pack(fill='both', padx=self.ui, pady=self.ui)
        self.title_spells = Label(self.frame_spells, text='Zaklęcia')
        self.title_spells.pack(side='left', fill='both', padx=self.ui, pady=self.ui)
        self.button_spells = Button(self.frame_spells, text='Dodaj zaklęcia', command=self.call_add_skill)
        self.button_spells.pack(side='right', fill='both', padx=self.ui, pady=self.ui)
        self.label_spells = Label(self.frame_spells_q, textvariable=self.spells)
        self.label_spells.pack(fill='both', padx=self.ui, pady=self.ui)

        self.frame_item_q = Frame(self.frame_right, borderwidth=2, relief="groove")
        self.frame_item_q.pack(fill='both', padx=self.ui, pady=self.ui)
        self.frame_item = Frame(self.frame_item_q)
        self.frame_item.pack(fill='both', padx=self.ui, pady=self.ui)
        self.title_item = Label(self.frame_item, text='Przedmioty')
        self.title_item.pack(side='left', fill='both', padx=self.ui, pady=self.ui)
        self.button_item = Button(self.frame_item, text='Dodaj przedmioty', command=self.call_add_item)
        self.button_item.pack(side='right', fill='both', padx=self.ui, pady=self.ui)
        self.label_item = Label(self.frame_item_q, textvariable=self.item)
        self.label_item.pack(fill='both', padx=self.ui, pady=self.ui)

        self.display_additional()

    def display_additional(self):
        perk_str = '\n'
        spell_str = '\n'
        item_str = '\n'
        self.perk_list = self.info_funcs()[0]()
        self.spell_list = self.info_funcs()[2]()
        self.item_list = self.info_funcs()[4]()
        for p in self.perk_list:
            perk_row = get_perk_by_id(p)
            perk_str += (str(perk_row['Nazwa']) + ' -> ' + str(perk_row['Info'])
                         + '\n\tAtt mod/Dmg mod -> ' + str(perk_row['Att_mod']) + '/' + str(perk_row['Dmg_mod']) + '\n\n')

        for s in self.spell_list:
            spell_row = get_spell_by_id(s)
            spell_str += (str(spell_row['Nazwa']) + ' -> ' + str(spell_row['Info']) + '\n\n')

        for p in self.item_list:
            item_row = get_item_by_id(p)
            item_str += (str(item_row['Nazwa']) + ' -> ' + str(item_row['Info']) + '\n\n')

        self.perks.set(perk_str)
        self.spells.set(spell_str)
        self.item.set(item_str)

    def call_change_weapon(self, num):
        win = ChangeWeapon(self, self.change_weapon, num)

    def change_weapon(self, name, num):
        if num == 1:
            self.att1.set(name)
        elif num == 2:
            self.att2.set(name)
        self.change_weapon_func(self.att1.get(), self.att2.get())

    def call_add_perk(self):
        win = AddInfo(self, self.add_info, 'Atut')

    def call_add_skill(self):
        win = AddInfo(self, self.add_info, 'Czar')

    def call_add_item(self):
        win = AddInfo(self, self.add_info, 'Przedmiot')

    def add_info(self, info, info_type):
        if info_type == 'Atut':
            self.info_funcs()[1](info)
        elif info_type == 'Czar':
            self.info_funcs()[3](info)
        else:
            self.info_funcs()[5](info)
        self.display_additional()

    def fill_classes(self):
        class_df = read_csv('tables/classes.csv', sep=';')
        self.class_list = class_df['Klasa'].to_list()
