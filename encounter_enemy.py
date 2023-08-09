from tkinter import ttk, Tk, Frame, Label, Entry, Spinbox, StringVar


class Enemy(Frame):
    def __init__(self, master, enemy_id, name, hp, kp, att_mod, weapon, weapon_mod, damage_mod, wytr, ref, wola):
        super().__init__(master)
        self.player_id = enemy_id
        self.ui_spacing = 2
        self.grid = Frame(self)
        self.grid.pack()
        self.name = StringVar()
        self.name.set(name + ' ' + str(enemy_id))
        self.name_entry = Entry(self.grid, textvariable=self.name)
        self.name_entry.grid(column=0, columnspan=2, padx=self.ui_spacing, pady=self.ui_spacing)

        self.kp = StringVar()
        self.hp = StringVar()
        self.att_mod = StringVar()
        self.weapon = StringVar()
        self.weapon_mod = StringVar()
        self.damage_mod = StringVar()
        self.wytr = StringVar()
        self.ref = StringVar()
        self.wola = StringVar()

        self.hp.set(hp)
        self.kp.set(kp)
        self.att_mod.set(att_mod)
        self.weapon.set(weapon)
        self.weapon_mod.set(weapon_mod)
        self.damage_mod.set(damage_mod)
        self.wytr.set(wytr)
        self.ref.set(ref)
        self.wola.set(wola)

        self.field_hp = Spinbox(self.grid, from_=-10, to=100, textvariable=self.hp)
        self.field_hp.grid(row=1, column=1, padx=self.ui_spacing, pady=self.ui_spacing)
        self.field_kp = Spinbox(self.grid, from_=-10, to=100, textvariable=self.kp)
        self.field_kp.grid(row=2, column=1, padx=self.ui_spacing, pady=self.ui_spacing)
        self.field_att_mod = Spinbox(self.grid, from_=-10, to=100, textvariable=self.att_mod)
        self.field_att_mod.grid(row=3, column=1, padx=self.ui_spacing, pady=self.ui_spacing)
        self.field_weapon = Spinbox(self.grid, from_=-10, to=100, textvariable=self.weapon)
        self.field_weapon.grid(row=4, column=1, padx=self.ui_spacing, pady=self.ui_spacing)
        self.field_weapon_mod = Spinbox(self.grid, from_=-10, to=100, textvariable=self.weapon_mod)
        self.field_weapon_mod.grid(row=5, column=1, padx=self.ui_spacing, pady=self.ui_spacing)
        self.field_damage_mod = Spinbox(self.grid, from_=-10, to=100, textvariable=self.damage_mod)
        self.field_damage_mod.grid(row=6, column=1, padx=self.ui_spacing, pady=self.ui_spacing)
        self.field_wytr = Spinbox(self.grid, from_=-10, to=100, textvariable=self.wytr)
        self.field_wytr.grid(row=7, column=1, padx=self.ui_spacing, pady=self.ui_spacing)
        self.field_ref = Spinbox(self.grid, from_=-10, to=100, textvariable=self.ref)
        self.field_ref.grid(row=8, column=1, padx=self.ui_spacing, pady=self.ui_spacing)
        self.field_wola = Spinbox(self.grid, from_=-10, to=100, textvariable=self.wola)
        self.field_wola.grid(row=9, column=1, padx=self.ui_spacing, pady=self.ui_spacing)

        self.label_hp = Label(self.grid, text="HP")
        self.label_hp.grid(row=1, column=0, padx=self.ui_spacing, pady=self.ui_spacing)
        self.label_kp = Label(self.grid, text="Klasa pancerza")
        self.label_kp.grid(row=2, column=0, padx=self.ui_spacing, pady=self.ui_spacing)
        self.label_att_mod = Label(self.grid, text="Modyfikator ataku")
        self.label_att_mod.grid(row=3, column=0, padx=self.ui_spacing, pady=self.ui_spacing)
        self.label_weapon = Label(self.grid, text="Broń")
        self.label_weapon.grid(row=4, column=0, padx=self.ui_spacing, pady=self.ui_spacing)
        self.label_weapon_mod = Label(self.grid, text="Modyfikator broni")
        self.label_weapon_mod.grid(row=5, column=0, padx=self.ui_spacing, pady=self.ui_spacing)
        self.label_damage_mod = Label(self.grid, text="Premia do obrażeń")
        self.label_damage_mod.grid(row=6, column=0, padx=self.ui_spacing, pady=self.ui_spacing)
        self.label_wytr = Label(self.grid, text="Wytrwałość")
        self.label_wytr.grid(row=7, column=0, padx=self.ui_spacing, pady=self.ui_spacing)
        self.label_ref = Label(self.grid, text="Refleks")
        self.label_ref.grid(row=8, column=0, padx=self.ui_spacing, pady=self.ui_spacing)
        self.label_wola = Label(self.grid, text="Siła woli")
        self.label_wola.grid(row=9, column=0, padx=self.ui_spacing, pady=self.ui_spacing)

