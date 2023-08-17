from tkinter import ttk, Tk, Frame, Label, Entry, StringVar, Button, Toplevel
from window_add_info import AddInfo
from pandas import DataFrame


class CharacterInfo(Toplevel):
    def __init__(self, master, add_info_func, additional=DataFrame()):
        super().__init__(master)
        self.ui_spacing = 2

        self.title("Character info")
        self.minsize(200, 200)

        self.grid = Frame(self)
        self.grid.pack(fill='both', padx=10, pady=10)

        self.add_info_func = add_info_func
        self.additional = additional
        self.perks = StringVar()
        self.spells = StringVar()
        self.item = StringVar()

        self.frame_perks = Frame(self.grid)
        self.frame_perks.pack(fill='both', padx=self.ui_spacing, pady=self.ui_spacing)
        self.title_perks = Label(self.frame_perks, text='Atuty')
        self.title_perks.pack(side='left', fill='both', padx=self.ui_spacing, pady=self.ui_spacing)
        self.button_perks = Button(self.frame_perks, text='Dodaj atuty', command=self.call_add_perk)
        self.button_perks.pack(side='right', fill='both', padx=self.ui_spacing, pady=self.ui_spacing)
        self.label_perks = Label(self.grid, textvariable=self.perks)
        self.label_perks.pack(fill='both', padx=self.ui_spacing, pady=self.ui_spacing)

        self.sep = ttk.Separator(self.grid, orient='horizontal')
        self.sep.pack(fill='x', padx=self.ui_spacing, pady=self.ui_spacing)

        self.frame_spells = Frame(self.grid)
        self.frame_spells.pack(fill='both', padx=self.ui_spacing, pady=self.ui_spacing)
        self.title_spells = Label(self.frame_spells, text='Zaklęcia')
        self.title_spells.pack(side='left', fill='both', padx=self.ui_spacing, pady=self.ui_spacing)
        self.button_spells = Button(self.frame_spells, text='Dodaj zaklęcia', command=self.call_add_skill)
        self.button_spells.pack(side='right', fill='both', padx=self.ui_spacing, pady=self.ui_spacing)
        self.label_spells = Label(self.grid, textvariable=self.spells)
        self.label_spells.pack(fill='both', padx=self.ui_spacing, pady=self.ui_spacing)

        self.sep = ttk.Separator(self.grid, orient='horizontal')
        self.sep.pack(fill='x', padx=self.ui_spacing, pady=self.ui_spacing)

        self.frame_item = Frame(self.grid)
        self.frame_item.pack(fill='both', padx=self.ui_spacing, pady=self.ui_spacing)
        self.title_item = Label(self.frame_item, text='Przedmioty')
        self.title_item.pack(side='left', fill='both', padx=self.ui_spacing, pady=self.ui_spacing)
        self.button_item = Button(self.frame_item, text='Dodaj przedmioty', command=self.call_add_item)
        self.button_item.pack(side='right', fill='both', padx=self.ui_spacing, pady=self.ui_spacing)
        self.label_item = Label(self.grid, textvariable=self.item)
        self.label_item.pack(fill='both', padx=self.ui_spacing, pady=self.ui_spacing)

        self.display_additional()

    def display_additional(self):
        perk_str = '\n'
        spell_str = '\n'
        item_str = '\n'
        for index, row in self.additional.iterrows():
            # print(row)
            if row.loc['Typ'] == 'Atut':
                perk_str += (str(row['Nazwa']) + ' -> ' + str(row['Info'])
                             + '\n\tAtt mod/Dmg mod -> ' + str(row['Att_mod']) + '/' + str(row['Dmg_mod']) + '\n')
            elif row.loc['Typ'] == 'Zaklęcie':
                spell_str += row + 'W.I.P.'
            else:
                item_str += (str(row['Nazwa']) + ' -> ' + str(row['Info'])
                             + '\n\tAtt mod/Dmg mod -> ' + str(row['Att_mod']) + '/' + str(row['Dmg_mod']) + '\n')

            self.perks.set(perk_str)
            self.spells.set(spell_str)
            self.item.set(item_str)

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

