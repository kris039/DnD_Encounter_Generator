from tkinter import ttk, Tk, Frame, Label, Entry, Spinbox, StringVar
from frame_character import Character


class Enemy(Character):
    def __init__(self, master, char_id, name, hp, kp, att1, att1_mod, att1_dmg_mod, att2, att2_mod, att2_dmg_mod, wytr, ref, wola, perks=(), drop=()):
        super().__init__(master, char_id, name, hp, kp, att1, att1_mod, att1_dmg_mod, att2, att2_mod, att2_dmg_mod, wytr, ref, wola, perks, drop)
        self.status.set('Przeciwnik')


if __name__ == "__main__":
    window = Tk()
    char = Enemy(window, 0, 'Ziomek', *range(11))
    char.pack()
    print(char.status)
    window.mainloop()
