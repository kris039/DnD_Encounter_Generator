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
        self.partymenu.add_command(label="Usuń ostatniego gracza", command=self.call_remove_player)
        self.menubar.add_cascade(label="Gracze", menu=self.partymenu)

        self.enemymenu = Menu(self.menubar, tearoff=0)
        self.enemymenu.add_command(label="Dodaj wroga", command=self.call_add_enemy)
        self.enemymenu.add_command(label="Usuń ostatniego wroga", command=self.call_remove_enemy)
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
        self.target_panel = Frame(master=self.grid_middle)
        self.target_panel.pack(side='right', fill='both', padx=2, pady=2)
        self.attack_from = ttk.Combobox(master=self.target_panel)
        self.attack_from.grid(row=0, column=0, columnspan=2, padx=2, pady=2)
        self.attack_to = ttk.Combobox(master=self.target_panel)
        self.attack_to.grid(row=1, column=0, columnspan=2, padx=2, pady=2)
        self.random_att = Button(master=self.target_panel, command=self.call_random, text='Losowy cel')
        self.random_att.grid(row=2, column=0, columnspan=2, sticky='we', padx=2, pady=2)
        self.attack1 = Button(master=self.target_panel, command=self.call_attack, text='Atak 1')
        self.attack1.grid(row=3, column=0, columnspan=1, sticky='we', padx=2, pady=2)
        self.attack2 = Button(master=self.target_panel, command=self.call_attack, text='Atak 2')
        self.attack2.grid(row=3, column=1, columnspan=1, sticky='we', padx=2, pady=2)
        self.refresh = Button(master=self.target_panel, command=self.call_refresh, text='Odśwież')
        self.refresh.grid(row=4, column=0, columnspan=2, sticky='we', padx=2, pady=2)

        self.initialized_fight(party_save_path, enemies)
        self.call_refresh()
        self.mainloop()

    def initialized_fight(self, path, enemies):
        if path != '':
            print('Party załadowane')
        if len(enemies) > 0:
            self.generate_enemies(enemies)
            print('Wrogowie załadowani')

    def generate_enemies(self, enemies_inp):
        enemies_df = read_csv('tables/enemies.csv', sep=';')
        for e in enemies_inp:
            r = e.split(', ')
            enemy_r = enemies_df.loc[enemies_df['Przeciwnik'] == r[0]]
            name = (r[0] + ' ' + r[1])
            hp = int(enemy_r['KW_mod'].iloc[0]*random.randint(1, enemy_r['KW_k'].iloc[0]))
            if hp == 0:
                hp = 1
            kp = enemy_r['KP'].iloc[0]
            att1 = enemy_r['Atak_1'].iloc[0]
            att1_mod = enemy_r['Atak_1_mod'].iloc[0]
            att1_dmg_mod = enemy_r['Atak_1_dmg_mod'].iloc[0]
            att2 = enemy_r['Atak_2'].iloc[0]
            att2_mod = enemy_r['Atak_2_mod'].iloc[0]
            att2_dmg_mod = enemy_r['Atak_2_dmg_mod'].iloc[0]
            wytr = enemy_r['Wytrw'].iloc[0]
            ref = enemy_r['Ref'].iloc[0]
            wola = enemy_r['Wola'].iloc[0]
            enemy = Enemy(self.grid_bottom, len(self.enemies), name, hp, kp, att1, att1_mod, att1_dmg_mod, att2,
                          att2_mod, att2_dmg_mod, wytr, ref, wola)
            self.enemies.append(enemy)
            enemy.pack(side='left', padx=2, pady=2)

    def call_random(self):
        target = random.randint(1, len(self.fighters))
        print(target)
        # self.battle_log_display.yview_moveto(1)

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
        player = Player(self.grid_top, len(self.enemies), "Gracz", *range(11))
        self.players.append(player)
        player.pack(side='left', padx=2, pady=2)
        self.call_refresh()

    def call_add_enemy(self):
        enemy = Enemy(self.grid_bottom, len(self.enemies), "Przeciwnik", *range(11))
        self.enemies.append(enemy)
        enemy.pack(side='left', padx=2, pady=2)
        self.call_refresh()

    def call_remove_player(self):
        if len(self.players) > 1:
            self.players[-1].pack_forget()
            self.players.pop(-1)

    def call_remove_enemy(self):
        if len(self.enemies) > 1:
            self.enemies[-1].pack_forget()
            self.enemies.pop(-1)


if __name__ == "__main__":
    r = random.randint(1, 8)
    hp = int(0.5 * r)
    print(r)
    print(hp)

