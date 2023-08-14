from tkinter import ttk, Tk, Frame, Label, Entry, Spinbox, StringVar
from character import Character


class Player(Character):
    def __init__(self, master, char_id, name, hp, kp, att1, att1_mod, att1_dmg_mod, att2, att2_mod, att2_dmg_mod, wytr, ref, wola, drop=()):
        super().__init__(master, char_id, name, hp, kp, att1, att1_mod, att1_dmg_mod, att2, att2_mod, att2_dmg_mod, wytr, ref, wola, drop)
        self.status.set('Gracz')
