import random
from tkinter import ttk, Tk, Frame, Label, Entry, StringVar, Button, Toplevel, Checkbutton, Spinbox, IntVar
from pandas import read_csv


class EnemyGroupWindow(Toplevel):
    def __init__(self, master, generator):
        super().__init__(master)
        self.ui_spacing = 2

        self.title("Enemy group creator")
        self.minsize(300, 100)
        self.resizable(False, False)

        self.generator = generator
        self.enemy_inp = []

        self.enemy_list = []
        self.class_list = []

        self.grid = Frame(self)
        self.grid.pack(fill='both')

        self.grid_left = Frame(self.grid)
        self.grid_left.pack(side='left', fill='both', padx=10, pady=10)
        self.uncheck_all_enemies = Button(master=self.grid_left, command=self.call_uncheck_enemies, text='Uncheck all')
        self.uncheck_all_enemies.pack(side='bottom', fill='x')
        self.check_all_enemies = Button(master=self.grid_left, command=self.call_check_enemies, text='Check all')
        self.check_all_enemies.pack(side='bottom', fill='x')

        self.sep = ttk.Separator(self.grid, orient='vertical')
        self.sep.pack(side='left', fill='y', padx=self.ui_spacing, pady=self.ui_spacing)

        self.grid_mid = Frame(self.grid)
        self.grid_mid.pack(side='left', fill='both', padx=10, pady=10)
        self.uncheck_all_classes = Button(master=self.grid_mid, command=self.call_uncheck_classes, text='Uncheck all')
        self.uncheck_all_classes.pack(side='bottom', fill='x')
        self.check_all_classes = Button(master=self.grid_mid, command=self.call_check_classes, text='Check all')
        self.check_all_classes.pack(side='bottom', fill='x')

        self.sep2 = ttk.Separator(self.grid, orient='vertical')
        self.sep2.pack(side='left', fill='y', padx=self.ui_spacing, pady=self.ui_spacing)

        self.grid_right = Frame(self.grid)
        self.grid_right.pack(side='left', fill='both', padx=10, pady=10)
        self.label_level = Label(self.grid_right, text='Poziom wrogów')
        self.label_level.pack(fill='x', padx=self.ui_spacing, pady=self.ui_spacing)
        self.min_level = Spinbox(self.grid_right, from_=1, to=100)
        self.min_level.pack(fill='x', padx=self.ui_spacing, pady=self.ui_spacing)
        self.max_level = Spinbox(self.grid_right, from_=1, to=100)
        self.max_level.pack(fill='x', padx=self.ui_spacing, pady=self.ui_spacing)
        self.label_amount = Label(self.grid_right, text='Ilość wrogów')
        self.label_amount.pack(fill='x', padx=self.ui_spacing, pady=self.ui_spacing)
        self.enemy_amount = Spinbox(self.grid_right, from_=1, to=100)
        self.enemy_amount.pack(fill='x', padx=self.ui_spacing, pady=self.ui_spacing)
        self.ok = Button(master=self.grid_right, command=self.call_ok, text='OK')
        self.ok.pack(side='right', fill='x', padx=self.ui_spacing, pady=self.ui_spacing)

        self.load_data()

        self.fill_enemy_list()
        self.fill_class_list()

    def call_ok(self):
        enemies = []
        classes = []
        for check, enemy, name in self.enemy_list:
            if check.get() == 1:
                enemies.append(name)
        for check, en_class, name in self.class_list:
            if check.get() == 1:
                classes.append(name)
        for i in range(int(self.enemy_amount.get())):
            self.enemy_inp.append(str(enemies[random.randint(0, len(enemies)-1)] + ', ' +
                                  classes[random.randint(0, len(classes)-1)] + ', ' +
                                  str(random.randint(1, int(self.max_level.get())))))
        self.generator(self.enemy_inp)
        self.destroy()

    def load_data(self):
        self.enemybook = read_csv('resources/enemies.csv', sep=';')
        self.classbook = read_csv('resources/classes.csv', sep=';')

    def fill_enemy_list(self):
        for e in list(self.enemybook['Przeciwnik']):
            enemy_int = IntVar()
            enemy = Checkbutton(self.grid_left, text=e, variable=enemy_int)
            enemy.pack(fill='x')
            self.enemy_list.append([enemy_int, enemy, e])

    def fill_class_list(self):
        for c in list(self.classbook['Klasa']):
            class_int = IntVar()
            en_class = Checkbutton(self.grid_mid, text=c, variable=class_int)
            en_class.pack(fill='x')
            self.class_list.append([class_int, en_class, c])

    def call_check_enemies(self):
        for check, enemy, name in self.enemy_list:
            enemy.select()

    def call_uncheck_enemies(self):
        for check, enemy, name in self.enemy_list:
            enemy.deselect()

    def call_check_classes(self):
        for check, en_class, name in self.class_list:
            en_class.select()

    def call_uncheck_classes(self):
        for check, en_class, name in self.class_list:
            en_class.deselect()
