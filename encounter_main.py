import random
from tkinter import Tk, Button
from encounter_generator import Generator


class Encounter:
    def __init__(self):
        self.root = Tk()

        # self.root.iconbitmap(r'')
        self.root.resizable(False, False)
        self.root.title("EnGen")

        self.button_generator = Button(self.root, command=self.call_generate, text='Generuj spotkanie', width=30)
        self.button_generator.pack(padx=10, pady=10, fill='both')

        self.root.mainloop()

    def call_generate(self):
        self.generator = Generator(self.root)
