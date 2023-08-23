from tkinter import ttk, Tk, Frame, Label, Entry, Spinbox, StringVar, Button
from window_character_info import CharacterInfo
from back_get_class_bonuses import get_class_bonuses
from pandas import read_csv, DataFrame


class Character(Frame):
    def __init__(self, master, char_id, char_dict, additional=DataFrame()):
        super().__init__(master)
        self.character_id = char_id
        self.ui = 2

        self.grid = Frame(self, borderwidth=2, relief="groove")
        self.grid.pack()

        self.status = StringVar()
        self.name = StringVar()
        self.classs = StringVar()
        self.level = StringVar()
        self.hp = StringVar()
        self.kp = StringVar()
        self.att1 = StringVar()
        self.att1_mod = StringVar()
        self.att1_dmg_mod = StringVar()
        self.att2 = StringVar()
        self.att2_mod = StringVar()
        self.att2_dmg_mod = StringVar()
        self.class_mod = StringVar()
        self.wytr = StringVar()
        self.ref = StringVar()
        self.wola = StringVar()
        self.weapons_df = []

        if self.character_id != '':
            self.name.set(char_dict['Name'] + ' ID:' + str(self.character_id))
        else:
            self.name.set(char_dict['Name'])
        self.classs.set(char_dict['Class'])
        self.level.set(char_dict['Level'])
        self.status.set('character')
        self.hp.set(char_dict['HP'])
        self.kp.set(char_dict['KP'])
        self.att1.set(char_dict['Att1'])
        self.att1_mod.set(char_dict['Att1_mod'])
        self.att1_dmg_mod.set(char_dict['Att1_dmg_mod'])
        self.att2.set(char_dict['Att2'])
        self.att2_mod.set(char_dict['Att2_mod'])
        self.att2_dmg_mod.set(char_dict['Att2_dmg_mod'])
        self.class_mod.set(char_dict['Class_mod'])
        self.wytr.set(char_dict['Wytr'])
        self.ref.set(char_dict['Ref'])
        self.wola.set(char_dict['Wola'])
        self.additional = additional

        self.label_name = Entry(self.grid, textvariable=self.name)
        self.label_name.grid(row=0, column=0, columnspan=2, sticky='we', padx=self.ui, pady=self.ui)
        self.info_frame = Frame(self.grid)
        self.info_frame.grid(row=0, column=2, sticky='we', padx=self.ui, pady=self.ui)
        self.button_info = Button(self.info_frame, text='Info', command=self.call_info)
        self.button_info.pack(side='right', padx=self.ui, pady=self.ui)
        self.label_id = Label(self.info_frame, text=str('ID: ' + str(self.character_id)))
        self.label_id.pack(side='right', padx=self.ui, pady=self.ui)

        self.label_class = Label(self.grid, text='Klasa')
        self.label_class.grid(row=1, column=0, padx=self.ui, pady=self.ui)
        self.label_hp_kp = Label(self.grid, text="HP/KP")
        self.label_hp_kp.grid(row=2, column=0, padx=self.ui, pady=self.ui)
        self.label_att1 = Label(self.grid, text="Atak 1")
        self.label_att1.grid(row=3, column=0, padx=self.ui, pady=self.ui)
        self.label_att1_mod = Label(self.grid, text="Mod/dmg mod")
        self.label_att1_mod.grid(row=4, column=0, padx=self.ui, pady=self.ui)
        self.label_att2 = Label(self.grid, text="Atak 2")
        self.label_att2.grid(row=5, column=0, padx=self.ui, pady=self.ui)
        self.label_att2_mod = Label(self.grid, text="Mod/dmg mod")
        self.label_att2_mod.grid(row=6, column=0, padx=self.ui, pady=self.ui)
        self.label_class_mod = Label(self.grid, text="Modyfikator klasy")
        self.label_class_mod.grid(row=7, column=0, padx=self.ui, pady=self.ui)
        self.label_safe = Label(self.grid, text="Wytr/Ref/Wola")
        self.label_safe.grid(row=8, column=0, columnspan=3, padx=self.ui, pady=self.ui)

        self.field_att1 = Label(self.grid, textvariable=self.classs)
        self.field_att1.grid(row=1, column=1, columnspan=2, padx=self.ui, pady=self.ui)
        self.field_hp = Spinbox(self.grid, from_=-10, to=100, textvariable=self.hp, width=10)
        self.field_hp.grid(row=2, column=1, padx=self.ui, pady=self.ui)
        self.field_kp = Spinbox(self.grid, from_=-10, to=100, textvariable=self.kp, width=10)
        self.field_kp.grid(row=2, column=2, padx=self.ui, pady=self.ui)
        self.field_att1 = Label(self.grid, textvariable=self.att1)
        self.field_att1.grid(row=3, column=1, columnspan=2, padx=self.ui, pady=self.ui)
        self.field_att1_mod = Spinbox(self.grid, from_=-10, to=100, textvariable=self.att1_mod, width=10)
        self.field_att1_mod.grid(row=4, column=1, padx=self.ui, pady=self.ui)
        self.field_att1_dmg_mod = Spinbox(self.grid, from_=-10, to=100, textvariable=self.att1_dmg_mod, width=10)
        self.field_att1_dmg_mod.grid(row=4, column=2, padx=self.ui, pady=self.ui)
        self.field_att2 = Label(self.grid, textvariable=self.att2)
        self.field_att2.grid(row=5, column=1, columnspan=2, padx=self.ui, pady=self.ui)
        self.field_att2_mod = Spinbox(self.grid, from_=-10, to=100, textvariable=self.att2_mod, width=10)
        self.field_att2_mod.grid(row=6, column=1, padx=self.ui, pady=self.ui)
        self.field_att2_dmg_mod = Spinbox(self.grid, from_=-10, to=100, textvariable=self.att2_dmg_mod, width=10)
        self.field_att2_dmg_mod.grid(row=6, column=2, padx=self.ui, pady=self.ui)
        self.field_class_mod = Label(self.grid, textvariable=self.class_mod, width=10)
        self.field_class_mod.grid(row=7, column=1, columnspan=2, padx=self.ui, pady=self.ui)
        self.field_wytr = Spinbox(self.grid, from_=-10, to=100, textvariable=self.wytr, width=10)
        self.field_wytr.grid(row=9, column=0, padx=self.ui, pady=self.ui)
        self.field_ref = Spinbox(self.grid, from_=-10, to=100, textvariable=self.ref, width=10)
        self.field_ref.grid(row=9, column=1, padx=self.ui, pady=self.ui)
        self.field_wola = Spinbox(self.grid, from_=-10, to=100, textvariable=self.wola, width=10)
        self.field_wola.grid(row=9, column=2, padx=self.ui, pady=self.ui)

    def call_info(self):
        self.info = CharacterInfo(self.grid, self.change_class, self.change_level, self.change_weapon, self.add_info,
                                  self.classs.get(), self.level.get(), self.att1.get(), self.att2.get(),
                                  additional=self.additional)
        # self.load_data()

    def add_info(self, row=DataFrame()):
        self.additional = self.additional.append(row)

    def change_weapon(self, att1, att2):
        self.att1.set(att1)
        self.att2.set(att2)

    def change_class(self, classs):
        self.classs.set(classs)
        self.class_mod.set(get_class_bonuses(self.classs.get(), self.level.get()))

    def change_level(self, level):
        self.level.set(level)
        self.class_mod.set(get_class_bonuses(self.classs.get(), self.level.get()))
