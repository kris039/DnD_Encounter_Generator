from tkinter import ttk, Tk, Frame, Label, Button, Toplevel, filedialog, StringVar, Listbox, END
from pandas import read_csv, DataFrame


class Creator(Toplevel):
    def __init__(self, master, generator):
        super().__init__(master)
        self.grid_main = Frame(self)
        self.grid_main.pack(fill='both')

        # self.root.iconbitmap(r'')
        self.minsize(500, 200)
        self.resizable(False, False)
        self.title("EnGen")

        self.enemybook = ''
        self.classbook = ''
        self.party_save_path = StringVar()
        self.party_save_path.set('')
        self.generator = generator

        self.monster_choice = Frame(self.grid_main)
        self.monster_choice.pack(fill='x', padx=5, pady=5)
        self.monster_left = Frame(self.monster_choice)
        self.monster_left.pack(expand=True, side='left', padx=5, pady=5)
        self.monster_type = ttk.Combobox(self.monster_left)
        self.monster_type.pack(fill='x', padx=5, pady=5)
        self.monster_class = ttk.Combobox(self.monster_left)
        self.monster_class.pack(fill='x', padx=5, pady=5)
        self.monster_level = ttk.Spinbox(self.monster_left, from_=1, to=100)
        self.monster_level.pack(fill='x', padx=5, pady=5)
        self.monster_buttons = Frame(self.monster_choice)
        self.monster_buttons.pack(side='left', padx=5, pady=5)
        self.monster_on = Button(self.monster_buttons, text='>>>', command=self.call_add)
        self.monster_on.pack(padx=5, pady=5)
        self.monster_off = Button(self.monster_buttons, text='<<<', command=self.call_remove)
        self.monster_off.pack(padx=5, pady=5)
        self.monster_right = Listbox(self.monster_choice)
        self.monster_right.pack(fill='x', expand=True, side='left', padx=5, pady=5)
        self.button_ok = Button(self.grid_main, text='OK', command=self.call_ok)
        self.button_ok.pack(fill='x', padx=5, pady=5)

        self.load_data()

    def load_data(self):
        self.enemybook = read_csv('tables/enemies.csv', sep=';')
        self.monster_type['values'] = list(self.enemybook['Przeciwnik'])
        self.classbook = read_csv('tables/classes.csv', sep=';')
        self.monster_class['values'] = list(self.classbook['Klasa'])

    def call_add(self):
        if self.monster_type.get() != '' and self.monster_class.get() != '' and self.monster_level.get() != '':
            monster = self.monster_type.get() + ', ' + self.monster_class.get() + ', ' + self.monster_level.get()
            self.monster_right.insert('end', monster)

    def call_remove(self):
        self.monster_right.delete(self.monster_right.curselection()[0])

    def call_ok(self):
        self.generator(self.monster_right.get(0, END))
        self.destroy()
