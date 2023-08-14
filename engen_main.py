from tkinter import Tk, Button, filedialog
from creator_window import Generator
from encounter_window import Encounter


class EnGen:
    def __init__(self):
        self.root = Tk()

        # self.root.iconbitmap(r'')
        self.root.resizable(False, False)
        self.root.title("EnGen")

        self.button_generator = Button(self.root, command=self.call_new, text='Nowe spotkanie', width=30)
        self.button_generator.pack(padx=5, pady=5, fill='both')
        self.button_generator = Button(self.root, command=self.call_generate, text='Generuj spotkanie', width=30)
        self.button_generator.pack(padx=5, pady=5, fill='both')
        self.button_generator = Button(self.root, command=self.call_open, text='Wczytaj spotkanie', width=30)
        self.button_generator.pack(padx=5, pady=5, fill='both')
        self.button_generator = Button(self.root, command=self.call_test, text='Wczytaj test', width=30)
        self.button_generator.pack(padx=5, pady=5, fill='both')

        self.root.mainloop()

    def call_new(self):
        self.encounter = Encounter(self.root)

    def call_generate(self):
        self.generator = Generator(self.root)

    def call_open(self):
        path = filedialog.askopenfilename()
        if path != '':
            print(path)
            self.encounter = Encounter(self.root, path)

    def call_test(self):
        self.encounter = Encounter(self.root, 'C:/Users/a764741/Downloads/test3_csv.csv')
