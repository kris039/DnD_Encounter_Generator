import random
from tkinter import ttk, Tk, Frame, Label, Button, StringVar, Scrollbar, Text, END, Menu, Toplevel, filedialog
from pandas import read_csv, DataFrame
from encounter_player import Player
from encounter_enemy import Enemy


class Encounter(Toplevel):
    def __init__(self, master, party_save_path, enemies):
        super().__init__(master)
        # self.party_safe_path = party_save_path
        self.fighters = []
        self.players = []
        self.enemies = []

        self.initialized_fight(party_save_path, enemies)

        self.grid_main = Frame(self)
        self.grid_main.pack(expand=True)

        # self.root.iconbitmap(r'')
        self.minsize(400, 200)
        self.resizable(False, True)
        # self.resizable(False, False)
        self.title("EnGen")

        self.menubar = Menu(self)

        self.partymenu = Menu(self.menubar, tearoff=0)
        self.partymenu.add_command(label="Otworz party", command=self.call_attack)
        self.partymenu.add_command(label="Zapisz party", command=self.safe_party)
        self.partymenu.add_separator()
        self.partymenu.add_command(label="Dodaj gracza", command=self.call_add_player)
        self.partymenu.add_command(label="Usuń gracza", command=self.call_remove_player)
        self.menubar.add_cascade(label="Gracze", menu=self.partymenu)

        self.enemymenu = Menu(self.menubar, tearoff=0)
        self.enemymenu.add_command(label="Dodaj wroga", command=self.call_add_enemy)
        self.enemymenu.add_command(label="Usuń wroga", command=self.call_remove_enemy)
        self.menubar.add_cascade(label="Wrogowie", menu=self.enemymenu)
        self.config(menu=self.menubar)

        self.grid_top = Frame(self.grid_main, background='green')
        self.grid_top.pack(side='top')
        self.grid_middle = Frame(master=self.grid_main, background='red')
        self.grid_middle.pack(fill='both', expand=True)
        self.grid_bottom = Frame(master=self.grid_main, background='green')
        self.grid_bottom.pack(side='bottom')

        self.battle_log_text = 'BattleLog started'
        self.battle_log_display = Text(master=self.grid_middle, background='white', height=15)
        self.battle_log_display.pack(side='left', fill='both', expand=True, padx=2, pady=2)
        self.dices = Frame(master=self.grid_middle, background='yellow')
        self.dices.pack(side='right', fill='both', padx=2, pady=2)
        self.attack_from = ttk.Combobox(master=self.dices)
        self.attack_from.pack(fill='both', padx=2, pady=2)
        self.attack_to = ttk.Combobox(master=self.dices)
        self.attack_to.pack(fill='both', padx=2, pady=2)
        self.attack = Button(master=self.dices, command=self.call_random, text='Losowy cel', width=25)
        self.attack.pack(fill='both', padx=2, pady=2)
        self.attack = Button(master=self.dices, command=self.call_attack, text='Atak', width=25)
        self.attack.pack(fill='both', padx=2, pady=2)
        self.refresh = Button(master=self.dices, command=self.call_refresh, text='Odśwież', width=25)
        self.refresh.pack(fill='both', padx=2, pady=2)

        self.call_refresh()
        self.mainloop()

    def initialized_fight(self, path, enemies):
        if path != '':
            print('party załadowane')
        if len(enemies) > 0:
            self.generate_enemies(enemies)
            print('wrogowie załadowani')

    def generate_enemies(self, enemies_inp):
        enemies_df = read_csv('tables/enemies.csv', sep=';')
        print(enemies_df)
        print(enemies_inp)
        for e in enemies_inp:
            r = e.split(', ')
            enemy_r = enemies_df.loc[enemies_df['Przeciwnik'] == r[0]]
            hp = int(enemy_r['KW_mod'][0]*random.randint(1, enemy_r['KW_k'][0]))
            if hp == 0:
                hp = 1
            kp = enemy_r['KP'][0]
            att_mod = 0
            weapon = enemy_r['Broń'][0]
            weapon_mod = 0
            damage_mod = enemy_r['Obrażenia_mod'][0]
            wytr = enemy_r['Wytrw'][0]
            ref = enemy_r['Ref'][0]
            wola = enemy_r['Wola'][0]

            enemy = Enemy(self.grid_bottom, len(self.enemies), (r[0] + ' ' + r[1]), hp, kp, att_mod, weapon, weapon_mod, damage_mod, wytr,
                          ref, wola)
            self.enemies.append(enemy)
            enemy.pack(side='left', padx=2, pady=2)

        print('Wygenerowano: ')

    def call_random(self):
        target = random.randint(1, len(self.fighters))
        print(target)
        self.battle_log_display.yview_moveto(1)

    def call_attack(self):
        throw = random.randint(1, 20)
        self.battle_log_text += '\n' + 'Rzut k20: ' + str(throw)
        self.battle_log_display.insert('insert', ('\n' + 'Rzut k20: ' + str(throw)))
        self.battle_log_display.yview_moveto(1)

    def call_refresh(self):
        self.battle_log_display.delete(1.0, END)
        self.battle_log_display.insert('insert', self.battle_log_text)
        self.fill_fighters_list()
        self.attack_from['values'] = self.fighters
        self.attack_to['values'] = self.fighters

    def fill_fighters_list(self):
        self.fighters = []
        for i in self.players+self.enemies:
            if i.name.get() != '' and int(i.hp.get()) > 0:
                self.fighters.append(i.name.get())

    def open_party(self):
        return None

    def safe_party(self):
        path = filedialog.asksaveasfilename(defaultextension='.csv')
        player_dict = {"Imię": [], "HP": [], "Klasa pancerza": [], "Modyfikator ataku": [], "Broń": [],
                       "Premia do obrażeń": []}
        for p in self.players:
            print(p.name.get(), p.health.get(), p.armor.get(), p.attack_mod.get(), p.weapon.get(), p.additional.get())
            player_dict["Imię"].append(p.name.get())
            player_dict["HP"].append(p.health.get())
            player_dict["Klasa pancerza"].append(p.armor.get())
            player_dict["Modyfikator ataku"].append(p.attack_mod.get())
            player_dict["Broń"].append(p.weapon.get())
            player_dict["Premia do obrażeń"].append(p.additional.get())
        print(path)
        print(DataFrame(player_dict))

    def call_add_player(self):
        player = Player(self.grid_top, len(self.players), *range(1, 10))
        self.players.append(player)
        player.pack(side='left', padx=2, pady=2)
        self.call_refresh()

    def call_add_enemy(self):
        enemy = Enemy(self.grid_bottom, len(self.enemies), "Przeciwnik", *range(1, 10))
        self.enemies.append(enemy)
        enemy.pack(side='left', padx=2, pady=2)
        self.call_refresh()

    def call_remove_player(self):
        if len(self.players) > 1:
            self.players[-1].pack_forget()
            self.players.pop(0)

    def call_remove_enemy(self):
        if len(self.enemies) > 1:
            self.enemies[-1].pack_forget()
            self.enemies.pop(0)


if __name__ == "__main__":
    r = random.randint(1, 8)
    hp = int(0.5 * r)
    print(r)
    print(hp)

