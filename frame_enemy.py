from tkinter import ttk, Tk, Frame, Label, Entry, Spinbox, StringVar
from pandas import DataFrame
from frame_character import Character


class Enemy(Character):
    def __init__(self, master, char_id, char_dict, additional=DataFrame()):
        super().__init__(master, char_id, char_dict, additional)
        self.status.set('Przeciwnik')


if __name__ == "__main__":
    window = Tk()
    char = Enemy(window, 0, 'Ziomek', *range(11))
    char.pack()
    print(char.status)
    window.mainloop()
