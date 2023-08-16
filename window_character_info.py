from tkinter import ttk, Tk, Frame, Label, Entry, StringVar, Button, Toplevel


class Character_info(Toplevel):
    def __init__(self, master, perks=(), skills=(), drop=()):
        super().__init__(master)
        self.ui_spacing = 2

        self.title("Character info")
        self.minsize(200, 200)

        self.grid = Frame(self)
        self.grid.pack(fill='both')

        self.perks = StringVar()
        self.skills = StringVar()
        self.drop = StringVar()

        self.perks.set(perks)
        self.skills.set(skills)
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
        self.title_skills = Label(self.grid, text='Umiejętności')
        self.title_skills.pack(fill='both', padx=self.ui_spacing, pady=self.ui_spacing)
        self.label_skills = Label(self.grid, textvariable=self.skills)
        self.label_skills.pack(fill='both', padx=self.ui_spacing, pady=self.ui_spacing)
        self.sep = ttk.Separator(self.grid, orient='horizontal')
        self.sep.pack(fill='x', padx=self.ui_spacing, pady=self.ui_spacing)
        self.title_drop = Label(self.grid, text='Przedmioty')
        self.title_drop.pack(fill='both', padx=self.ui_spacing, pady=self.ui_spacing)
        self.label_drop = Label(self.grid, textvariable=self.drop)
        self.label_drop.pack(fill='both', padx=self.ui_spacing, pady=self.ui_spacing)


