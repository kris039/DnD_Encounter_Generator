from tkinter import ttk, Tk, Frame, Label, Entry, Spinbox, StringVar
from encounter_character import Character


class Player(Character):
    def __init__(self, master, char_id, name, hp, kp, att1, att1_mod, att1_dmg_mod, att2, att2_mod, att2_dmg_mod, wytr, ref, wola):
        super().__init__(master, char_id, name, hp, kp, att1, att1_mod, att1_dmg_mod, att2, att2_mod, att2_dmg_mod, wytr, ref, wola)
        self.status.set('Gracz')
