from tkinter import ttk, Tk, Frame, Label, Entry, Spinbox, StringVar
from pandas import DataFrame
from frame_character import Character


class Player(Character):
    def __init__(self, master, char_id, char_dict, additional=DataFrame()):
        super().__init__(master, char_id, char_dict, additional)
        self.status.set('Gracz')
