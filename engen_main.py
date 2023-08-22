import random
from tkinter import (ttk, Tk, Frame, Label, Button, StringVar, Scrollbar, Text, END, Menu, Toplevel, filedialog,
                     messagebox, OptionMenu, Checkbutton)
from pandas import read_csv, DataFrame
from frame_player import Player
from frame_enemy import Enemy
from frame_dice_pack import DicePack
from back_enemy_generator import generate_enemy
from window_enemy_group import EnemyGroupWindow
from window_enemy_creator import Creator
from window_delete_character import DeleteCharacterWindow
from back_attack import attack
from back_save_file_functions import *


class EnGen:
    def __init__(self):
        self.root = Tk()
        # self.root.iconbitmap(r'')
        self.root.minsize(600, 200)
        # self.root.resizable(False, True)
        self.root.resizable(False, False)
        self.root.title("EnGen")

        self.characters = []
        self.character_list = []
        self.id_count = 0
        self.attack_count = 1
        self.previous_attacker = -1
        self.weapons_df = read_csv('tables/weapons.csv', sep=';')

        self.attack_from_name = StringVar()
        self.attack_to_name = StringVar()

        self.grid_main = Frame(self.root)
        self.grid_main.pack(expand=True)

        self.menubar = Menu(self.root)

        self.generalmenu = Menu(self.menubar, tearoff=0)
        self.generalmenu.add_command(label="Otworz spotkanie", command=self.call_open)
        self.generalmenu.add_command(label="Zapisz spotkanie", command=self.call_save)
        self.generalmenu.add_command(label="Usuń postać", command=self.call_delete_window)
        self.menubar.add_cascade(label="Ogólne", menu=self.generalmenu)

        self.partymenu = Menu(self.menubar, tearoff=0)
        self.partymenu.add_command(label="Otworz party", command=self.call_open)
        self.partymenu.add_command(label="Zapisz party", command=self.call_save_party)
        self.partymenu.add_separator()
        self.partymenu.add_command(label="Dodaj gracza", command=self.add_player)
        self.menubar.add_cascade(label="Gracze", menu=self.partymenu)

        self.enemymenu = Menu(self.menubar, tearoff=0)
        self.enemymenu.add_command(label="Otworz przeciwników", command=self.call_open)
        self.enemymenu.add_command(label="Zapisz przeciwników", command=self.call_save_enemies)
        self.enemymenu.add_separator()
        self.enemymenu.add_command(label="Wybierz przeciwników", command=self.call_choose_enemy)
        self.enemymenu.add_command(label="Generuj losowych przeciwników", command=self.call_enemy_group)
        self.enemymenu.add_separator()
        self.enemymenu.add_command(label="Dodaj wroga", command=self.add_enemy)
        self.menubar.add_cascade(label="Wrogowie", menu=self.enemymenu)
        self.root.config(menu=self.menubar)

        self.grid_top = Frame(self.grid_main)
        self.grid_top.pack(side='top')
        self.grid_middle = Frame(master=self.grid_main)
        self.grid_middle.pack(fill='both', expand=True)
        self.grid_bottom = Frame(master=self.grid_main)
        self.grid_bottom.pack(side='bottom')

        self.battle_log_text = 'BattleLog started'
        self.battle_log_display = Text(master=self.grid_middle, background='white', height=15, width=100)
        self.battle_log_display.configure(font=('Segoe UI', 12, 'normal'))
        self.battle_log_display.pack(side='left', fill='both', expand=True, padx=2, pady=2)
        self.right_panel = Frame(master=self.grid_middle)
        self.right_panel.pack(side='right', fill='both', padx=2, pady=2)
        self.attack_panel = Frame(master=self.right_panel)
        self.attack_panel.pack(padx=2, pady=2)
        self.attack_from = ttk.OptionMenu(self.attack_panel, self.attack_from_name, '', *self.character_list)
        self.attack_from.grid(row=0, column=0, columnspan=2, padx=2, pady=2, sticky='we')
        self.attack_to = ttk.OptionMenu(self.attack_panel, self.attack_to_name, '', *self.character_list)
        self.attack_to.grid(row=1, column=0, columnspan=2, padx=2, pady=2, sticky='we')
        self.random_att = Button(master=self.attack_panel, command=self.call_random, text='Losowy cel', width=25)
        self.random_att.grid(row=2, column=0, columnspan=2, sticky='we', padx=2, pady=2)
        self.attack1 = Button(master=self.attack_panel, command=self.call_attack1, text='Atak 1')
        self.attack1.grid(row=3, column=0, columnspan=1, sticky='we', padx=2, pady=2)
        self.attack2 = Button(master=self.attack_panel, command=self.call_attack2, text='Atak 2')
        self.attack2.grid(row=3, column=1, columnspan=1, sticky='we', padx=2, pady=2)
        self.refresh = Button(master=self.attack_panel, command=self.call_refresh, text='Odśwież')
        self.refresh.grid(row=4, column=0, columnspan=2, sticky='we', padx=2, pady=2)
        self.test = Button(master=self.attack_panel, command=self.call_test, text='TEST LOAD')
        self.test.grid(row=5, column=0, columnspan=2, sticky='we', padx=2, pady=2)
        self.test = Button(master=self.attack_panel, command=self.call_test2, text='TEST GEN')
        self.test.grid(row=6, column=0, columnspan=2, sticky='we', padx=2, pady=2)
        self.dices = DicePack(self.right_panel, self.add_to_log)
        self.dices.pack(side='bottom')

        self.call_refresh()
        self.root.mainloop()

    def call_choose_enemy(self):
        enemy_inp = []
        win = Creator(self.root, self.generate_enemies, enemy_inp)

    def call_enemy_group(self):
        enemy_inp = []
        win = EnemyGroupWindow(self.root, self.generate_enemies, enemy_inp)

    def generate_enemies(self, enemies_inp):
        enemies_df = read_csv('tables/enemies.csv', sep=';')
        classes_df = read_csv('tables/classes.csv', sep=';')
        for e in enemies_inp:
            r = e.split(', ')
            enemy_r = enemies_df.loc[enemies_df['Przeciwnik'] == r[0]]
            class_r = classes_df.loc[classes_df['Klasa'] == r[1]]
            enemy = Enemy(self.grid_bottom, self.id_count, *generate_enemy(r, enemy_r, class_r))
            self.id_count += 1
            self.characters.append(enemy)
            enemy.pack(side='left', padx=2, pady=2)

    def remove_character(self, name):
        for index, char in enumerate(self.characters):
            if char.name.get() == name:
                self.characters.pop(index)
                char.pack_forget()
        self.call_refresh()

    def call_delete_window(self):
        win = DeleteCharacterWindow(self.root, self.characters, self.remove_character)

    def call_random(self):
        if self.check() and len(self.characters) > 0:
            self.attack_to_name.set(self.character_list[random.randint(0, len(self.characters)-1)])

    def call_attack1(self):
        self.call_attack(1)

    def call_attack2(self):
        self.call_attack(2)

    def call_attack(self, att):
        if self.check():
            attacker = self.find_char_by_name(self.attack_from_name.get())
            attacked = self.find_char_by_name(self.attack_to_name.get())

            if attacker != '' and attacked != '':
                if self.previous_attacker != attacker.character_id:
                    self.attack_count = 1
                    self.previous_attacker = attacker.character_id
                else:
                    self.previous_attacker = attacker.character_id

                class_mods = attacker.class_mod.get().split('/')
                cl_mod = int(class_mods[self.attack_count-1])
                print(self.attack_count, self.previous_attacker)

                if self.attack_count < len(class_mods):
                    self.attack_count += 1
                self.battle_log_text += attack(attacker, attacked, self.weapons_df, att, cl_mod)
            self.call_refresh()

    def call_refresh(self):
        self.battle_log_display.delete(1.0, END)
        self.battle_log_display.insert('insert', self.battle_log_text)
        self.battle_log_display.yview_moveto(1)
        self.fill_character_list()
        self.attack_from.set_menu(None, *self.character_list)
        self.attack_to.set_menu(None, *self.character_list)
        self.check()

    def call_open(self, path='', who=''):
        load_characters(self.add_player, self.add_enemy, who=who, path=path)

    def call_save_party(self):
        self.call_save('Gracz')

    def call_save_enemies(self):
        self.call_save('Przeciwnik')

    def call_save(self, who=''):
        save_characters(self.characters)

    def add_player(self, char_dict=()):
        if char_dict == ():
            char_dict = create_dummy_char_dict('Gracz')
        player = Player(self.grid_top, self.id_count, char_dict)
        self.id_count += 1
        self.characters.append(player)
        player.pack(side='left', padx=2, pady=2)
        self.call_refresh()

    def add_enemy(self, char_dict=()):
        if char_dict == ():
            char_dict = create_dummy_char_dict('Przeciwnik')
        enemy = Enemy(self.grid_bottom, self.id_count, char_dict)
        self.id_count += 1
        self.characters.append(enemy)
        enemy.pack(side='left', padx=2, pady=2)
        self.call_refresh()

    def add_to_log(self, text):
        self.battle_log_text += text
        self.call_refresh()

    def find_char_by_name(self, name):
        for c in self.characters:
            if name == c.name.get():
                return c

    def check(self):
        if len(self.character_list) == len(set(self.character_list)):
            return True
        else:
            messagebox.showwarning('Ogarnij imiona',
                                   'Zanim będziesz kontynuować, zmień imiona by były unikalne')
            return False

    def fill_character_list(self):
        self.character_list = []
        for i in self.characters:
            if i.name.get() != '' and int(i.hp.get()) > 0:
                self.character_list.append(i.name.get())
        self.character_list.sort()

    def call_test(self):
        self.call_open(path='test_csv.csv')

    def call_test2(self):
        self.generate_enemies(['Kobold, Barbarzyńca, 15'])
        self.call_refresh()


if __name__ == "__main__":
    r = random.randint(1, 8)
    hp = int(0.5 * r)
    print(r)
    print(hp)

