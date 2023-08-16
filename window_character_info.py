from tkinter import ttk, Tk, Frame, Label, Entry, StringVar, Button, Toplevel


class CharacterInfo(Toplevel):
    def __init__(self, master, perks=(), spells=(), drop=()):
        super().__init__(master)
        self.ui_spacing = 2

        self.title("Character info")
        self.minsize(200, 200)

        self.grid = Frame(self)
        self.grid.pack(fill='both', padx=10, pady=10)

        self.perks = StringVar()
        self.spells = StringVar()
        self.drop = StringVar()

        perk_str = '\n'
        for i in perks:
            perk_str += (str(i['Nazwa']) + ' -> ' + str(i['Info'])
                         + '\n\tAtt mod/Dmg mod -> ' + str(i['Att_mod']) + '/' + str(i['Dmg_mod']) + '\n')
        self.perks.set(perk_str)
        self.spells.set(spells)
        drop_str = '\n'
        for i in drop:
            drop_str += i + '\n'
        self.drop.set(drop_str)

        self.title_perks = Label(self.grid, text='Atuty')
        self.title_perks.pack(fill='both', padx=self.ui_spacing, pady=self.ui_spacing)
        self.label_perks = Label(self.grid, textvariable=self.perks)
        self.label_perks.pack(fill='both', padx=self.ui_spacing, pady=self.ui_spacing)
        self.sep = ttk.Separator(self.grid, orient='horizontal')
        self.sep.pack(fill='x', padx=self.ui_spacing, pady=self.ui_spacing)
        self.title_spells = Label(self.grid, text='Zaklęcia')
        self.title_spells.pack(fill='both', padx=self.ui_spacing, pady=self.ui_spacing)
        self.label_spells = Label(self.grid, textvariable=self.spells)
        self.label_spells.pack(fill='both', padx=self.ui_spacing, pady=self.ui_spacing)
        self.sep = ttk.Separator(self.grid, orient='horizontal')
        self.sep.pack(fill='x', padx=self.ui_spacing, pady=self.ui_spacing)
        self.title_drop = Label(self.grid, text='Przedmioty')
        self.title_drop.pack(fill='both', padx=self.ui_spacing, pady=self.ui_spacing)
        self.label_drop = Label(self.grid, textvariable=self.drop)
        self.label_drop.pack(fill='both', padx=self.ui_spacing, pady=self.ui_spacing)


