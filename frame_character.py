from tkinter import ttk, Tk, Frame, Label, Entry, Spinbox, StringVar, Button
from window_character_info import Character_info


class Character(Frame):
    def __init__(self, master, char_id, name, hp, kp, att1, att1_mod, att1_dmg_mod, att2, att2_mod, att2_dmg_mod,
                 wytr, ref, wola, drop=()):
        super().__init__(master)
        self.character_id = char_id
        self.ui_spacing = 2

        self.grid = Frame(self)
        self.grid.pack()

        self.status = StringVar()
        self.name = StringVar()
        self.hp = StringVar()
        self.kp = StringVar()
        self.att1 = StringVar()
        self.att1_mod = StringVar()
        self.att1_dmg_mod = StringVar()
        self.att2 = StringVar()
        self.att2_mod = StringVar()
        self.att2_dmg_mod = StringVar()
        self.wytr = StringVar()
        self.ref = StringVar()
        self.wola = StringVar()

        self.name.set(name)
        self.status.set('character')
        self.hp.set(hp)
        self.kp.set(kp)
        self.att1.set(att1)
        self.att1_mod.set(att1_mod)
        self.att1_dmg_mod.set(att1_dmg_mod)
        self.att2.set(att2)
        self.att2_mod.set(att2_mod)
        self.att2_dmg_mod.set(att2_dmg_mod)
        self.wytr.set(wytr)
        self.ref.set(ref)
        self.wola.set(wola)
        self.drop = drop

        self.label_name = Entry(self.grid, textvariable=self.name)
        self.label_name.grid(row=0, column=0, columnspan=2, sticky='we', padx=self.ui_spacing, pady=self.ui_spacing)
        self.info_frame = Frame(self.grid)
        self.info_frame.grid(row=0, column=2, sticky='we', padx=self.ui_spacing, pady=self.ui_spacing)
        self.button_info = Button(self.info_frame, text='Info', command=self.call_info)
        self.button_info.pack(side='right', padx=self.ui_spacing, pady=self.ui_spacing)
        self.label_id = Label(self.info_frame, text=str('ID: ' + str(self.character_id)))
        self.label_id.pack(side='right', padx=self.ui_spacing, pady=self.ui_spacing)
        self.label_hp_kp = Label(self.grid, text="HP/KP")
        self.label_hp_kp.grid(row=1, column=0, padx=self.ui_spacing, pady=self.ui_spacing)
        self.label_att1 = Label(self.grid, text="Atak 1")
        self.label_att1.grid(row=2, column=0, padx=self.ui_spacing, pady=self.ui_spacing)
        self.label_att1_mod = Label(self.grid, text="Mod/dmg mod")
        self.label_att1_mod.grid(row=3, column=0, padx=self.ui_spacing, pady=self.ui_spacing)
        self.label_att2 = Label(self.grid, text="Atak 2")
        self.label_att2.grid(row=4, column=0, padx=self.ui_spacing, pady=self.ui_spacing)
        self.label_att2_mod = Label(self.grid, text="Mod/dmg mod")
        self.label_att2_mod.grid(row=5, column=0, padx=self.ui_spacing, pady=self.ui_spacing)
        self.label_safe = Label(self.grid, text="Wytr/Ref/Wola")
        self.label_safe.grid(row=6, column=0, columnspan=3, padx=self.ui_spacing, pady=self.ui_spacing)

        self.field_hp = Spinbox(self.grid, from_=-10, to=100, textvariable=self.hp, width=10)
        self.field_hp.grid(row=1, column=1, padx=self.ui_spacing, pady=self.ui_spacing)
        self.field_kp = Spinbox(self.grid, from_=-10, to=100, textvariable=self.kp, width=10)
        self.field_kp.grid(row=1, column=2, padx=self.ui_spacing, pady=self.ui_spacing)
        self.field_att1 = Entry(self.grid, textvariable=self.att1)
        self.field_att1.grid(row=2, column=1, columnspan=2, padx=self.ui_spacing, pady=self.ui_spacing)
        self.field_att1_mod = Spinbox(self.grid, from_=-10, to=100, textvariable=self.att1_mod, width=10)
        self.field_att1_mod.grid(row=3, column=1, padx=self.ui_spacing, pady=self.ui_spacing)
        self.field_att1_dmg_mod = Spinbox(self.grid, from_=-10, to=100, textvariable=self.att1_dmg_mod, width=10)
        self.field_att1_dmg_mod.grid(row=3, column=2, padx=self.ui_spacing, pady=self.ui_spacing)
        self.field_att2 = Entry(self.grid, textvariable=self.att2)
        self.field_att2.grid(row=4, column=1, columnspan=2, padx=self.ui_spacing, pady=self.ui_spacing)
        self.field_att2_mod = Spinbox(self.grid, from_=-10, to=100, textvariable=self.att2_mod, width=10)
        self.field_att2_mod.grid(row=5, column=1, padx=self.ui_spacing, pady=self.ui_spacing)
        self.field_att2_dmg_mod = Spinbox(self.grid, from_=-10, to=100, textvariable=self.att2_dmg_mod, width=10)
        self.field_att2_dmg_mod.grid(row=5, column=2, padx=self.ui_spacing, pady=self.ui_spacing)
        self.field_wytr = Spinbox(self.grid, from_=-10, to=100, textvariable=self.wytr, width=10)
        self.field_wytr.grid(row=7, column=0, padx=self.ui_spacing, pady=self.ui_spacing)
        self.field_ref = Spinbox(self.grid, from_=-10, to=100, textvariable=self.ref, width=10)
        self.field_ref.grid(row=7, column=1, padx=self.ui_spacing, pady=self.ui_spacing)
        self.field_wola = Spinbox(self.grid, from_=-10, to=100, textvariable=self.wola, width=10)
        self.field_wola.grid(row=7, column=2, padx=self.ui_spacing, pady=self.ui_spacing)

    def call_info(self):
        self.info = Character_info(self.grid, drop=self.drop)
