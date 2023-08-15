from tkinter import Frame, Button, Toplevel, Checkbutton, IntVar, ttk, StringVar, Label


class DeleteCharacterWindow(Toplevel):
    def __init__(self, master, characters, func):
        super().__init__(master)
        self.grid = Frame(self)
        self.grid.pack(fill='both')

        self.resizable(False, False)
        self.title("EnGen")

        self.characters = characters
        self.character_names = []
        self.char_to_del = StringVar()
        self.func = func

        self.fill_character_names()

        self.label_who = Label(self.grid, text='Kogo chcesz usunąć?')
        self.label_who.pack(fill='x', padx=5, pady=5)
        self.char_menu = ttk.OptionMenu(self.grid, self.char_to_del, '', *self.character_names)
        self.char_menu.pack(fill='x', padx=5, pady=5)

        self.ok = Button(self.grid, text='OK', command=self.call_delete)
        self.ok.pack(fill='x', padx=5, pady=5)

    def fill_character_names(self):
        for c in self.characters:
            self.character_names.append(c.name.get())

    def call_delete(self):
        self.func(self.char_to_del.get())
        self.destroy()
