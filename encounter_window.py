import random
from tkinter import ttk, Tk, Frame, Label, Button, StringVar, Scrollbar, Text, END, Menu, Toplevel, filedialog, messagebox
from pandas import read_csv, DataFrame
from encounter_player import Player
from encounter_enemy import Enemy


class Encounter(Toplevel):
    def __init__(self, master, party_save_path='', enemies=()):
        super().__init__(master)
        self.characters = []

        self.grid_main = Frame(self)
        self.grid_main.pack(expand=True)

        # self.root.iconbitmap(r'')
        self.minsize(400, 200)
        self.resizable(False, True)
        # self.resizable(False, False)
        self.title("EnGen")

        self.menubar = Menu(self)

        self.partymenu = Menu(self.menubar, tearoff=0)
        self.partymenu.add_command(label="Zapisz spotkanie", command=self.call_save)
        self.partymenu.add_separator()
        self.partymenu.add_command(label="Otworz party", command=self.call_open)
        self.partymenu.add_command(label="Zapisz party", command=self.call_save_party)
        self.partymenu.add_separator()
        self.partymenu.add_command(label="Dodaj gracza", command=self.call_add_player)
        # self.partymenu.add_command(label="Usuń ostatniego gracza", command=self.call_remove_player)
        self.menubar.add_cascade(label="Gracze", menu=self.partymenu)

        self.enemymenu = Menu(self.menubar, tearoff=0)
        self.enemymenu.add_command(label="Otworz przeciwników", command=self.call_open)
        self.enemymenu.add_command(label="Zapisz przeciwników", command=self.call_save_enemies)
        self.enemymenu.add_separator()
        self.enemymenu.add_command(label="Dodaj wroga", command=self.call_add_enemy)
        # self.enemymenu.add_command(label="Usuń ostatniego wroga", command=self.call_remove_enemy)
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

        if party_save_path != '':
            self.call_open(party_save_path)
        if enemies != ():
            self.generate_enemies(enemies)
        self.call_refresh()
        self.mainloop()

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
            enemy = Enemy(self.grid_bottom, len(self.characters), name, hp, kp, att1, att1_mod, att1_dmg_mod, att2,
                          att2_mod, att2_dmg_mod, wytr, ref, wola)
            self.characters.append(enemy)
            enemy.pack(side='left', padx=2, pady=2)

    def call_random(self):
        if self.check():
            target = random.randint(1, len(self.characters))
            print(target)

    def call_attack(self):
        if self.check():
            attacker = self.attack_from.get()
            attacked = self.attack_to.get()

            if attacker != '' and attacked != '':
                self.battle_log_text += '\n' + attacker + ' zaatakował ' + attacked
                hit_throw = random.randint(1, 20)
                if hit_throw >= 20:
                    self.battle_log_text += ('\n' + attacker + ': Rzut k20 na trafienie: ' + str(hit_throw)
                                             + ' - TRAFIENIE KRYTYCZNE')
                    dmg = 0
                    for i in range(3):
                        dmg_throw = random.randint(1, 8)
                        dmg += dmg_throw
                        self.battle_log_text += ('\n' + attacker + ': Rzut k8(t) na obrażenia: ' + str(dmg_throw))
                    self.battle_log_text += '\n' + attacker + ' zadał ' + str(dmg) + ' punktów obrażeń'
                if hit_throw >= 12:
                    self.battle_log_text += '\n' + attacker + ': Rzut k20 na trafienie: ' + str(hit_throw)
                    dmg = 0
                    dmg_throw = random.randint(1, 8)
                    dmg += dmg_throw
                    self.battle_log_text += ('\n' + attacker + ': Rzut k8(t) na obrażenia: ' + str(dmg_throw))
                    self.battle_log_text += '\n' + attacker + ' zadał punktów obrażeń' + str(dmg)

                else:
                    self.battle_log_text += '\n' + attacker + ': Rzut k20 na trafienie: ' + str(hit_throw)
                    self.battle_log_text += '\n' + attacker + ' chybił'
            self.call_refresh()

    def call_refresh(self):
        self.battle_log_display.delete(1.0, END)
        self.battle_log_display.insert('insert', self.battle_log_text)
        self.battle_log_display.yview_moveto(1)
        self.fill_character_list()
        self.attack_from['values'] = self.character_list
        self.attack_to['values'] = self.character_list
        self.check()

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

    def call_open(self, path='', who=''):
        if path == '':
            path = filedialog.askopenfilename(defaultextension='.csv')
        if path != '':
            loaded = read_csv(path, sep=';')
            for i, j in loaded.iterrows():
                if j[0] == 'Gracz':
                    char = Player(self.grid_top, len(self.characters), *j[1:])
                    self.characters.append(char)
                    char.pack(side='left', padx=2, pady=2)
                if j[0] == 'Przeciwnik':
                    char = Enemy(self.grid_bottom, len(self.characters), *j[1:])
                    self.characters.append(char)
                    char.pack(side='left', padx=2, pady=2)

    def call_save_party(self):
        self.call_save('Gracz')

    def call_save_enemies(self):
        self.call_save('Przeciwnik')

    def call_save(self, who=''):
        def save(c, wh):
            if c.status.get() != wh:
                character_dict["Status"].append(c.status.get())
                character_dict["Imię"].append(c.name.get())
                character_dict["HP"].append(c.hp.get())
                character_dict["KP"].append(c.kp.get())
                character_dict["Atak 1"].append(c.att1.get())
                character_dict["Mod 1"].append(c.att1_mod.get())
                character_dict["Dmg mod 1"].append(c.att1_dmg_mod.get())
                character_dict["Atak 2"].append(c.att2.get())
                character_dict["Mod 2"].append(c.att2_mod.get())
                character_dict["Dmg mod 2"].append(c.att2_dmg_mod.get())
                character_dict["Wytr"].append(c.wytr.get())
                character_dict["Ref"].append(c.ref.get())
                character_dict["Wola"].append(c.wola.get())

        path = filedialog.asksaveasfilename(defaultextension='.csv')
        if path != '':
            character_dict = {"Status": [], "Imię": [], "HP": [], "KP": [],
                              "Atak 1": [], "Mod 1": [], "Dmg mod 1": [],
                              "Atak 2": [], "Mod 2": [], "Dmg mod 2": [],
                              "Wytr": [], "Ref": [], "Wola": []}

            for p in self.characters:
                if who == 'Gracz':
                    save(p, 'Przeciwnik')
                elif who == 'Przeciwnik':
                    save(p, 'Gracz')
                else:
                    save(p, '')
            DataFrame(character_dict).to_csv(path, ';', index=False)

    def call_add_player(self):
        player = Player(self.grid_top, len(self.characters), "Gracz " + str(len(self.characters)), *range(1, 12))
        self.characters.append(player)
        player.pack(side='left', padx=2, pady=2)
        self.call_refresh()

    def call_add_enemy(self):
        enemy = Enemy(self.grid_bottom, len(self.characters), "Przeciwnik " + str(len(self.characters)), *range(1, 12))
        self.characters.append(enemy)
        enemy.pack(side='left', padx=2, pady=2)
        self.call_refresh()


if __name__ == "__main__":
    r = random.randint(1, 8)
    hp = int(0.5 * r)
    print(r)
    print(hp)

