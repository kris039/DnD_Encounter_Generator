from tkinter import filedialog
from pandas import read_csv, DataFrame


def save_characters(characters, who=''):
    path = filedialog.asksaveasfilename(defaultextension='.csv')
    if path != '':
        characters_df = DataFrame()
        for char in characters:
            if char.status.get() == who or who == '':
                char_dict = {}
                char_dict['Name'] = char.name.get().split(' ID:')[0]
                char_dict['Class'] = char.classs.get()
                char_dict['Level'] = char.level.get()
                char_dict['Status'] = char.status.get()
                char_dict['HP'] = char.hp.get()
                char_dict['KP'] = char.kp.get()
                char_dict['Att1'] = char.att1.get()
                char_dict['Att1_mod'] = char.att1_mod.get()
                char_dict['Att1_dmg_mod'] = char.att1_dmg_mod.get()
                char_dict['Att2'] = char.att2.get()
                char_dict['Att2_mod'] = char.att2_mod.get()
                char_dict['Att2_dmg_mod'] = char.att2_dmg_mod.get()
                char_dict['Class_mod'] = char.class_mod.get()
                char_dict['Wytr'] = char.wytr.get()
                char_dict['Ref'] = char.ref.get()
                char_dict['Wola'] = char.wola.get()
                characters_df = characters_df.append(char_dict, ignore_index=True)
        characters_df.to_csv(path, ';', index=False)


def load_characters(func_add_player, func_add_enemy, who='', path=''):
    if path == '':
        path = filedialog.askopenfilename(defaultextension='.csv')
    if path != '':
        loaded = read_csv(path, sep=';')
        for i, j in loaded.iterrows():
            if j[0] == who or who == '':
                if j['Status'] == 'Gracz':
                    func_add_player(j.to_dict())
                if j['Status'] == 'Przeciwnik':
                    func_add_enemy(j.to_dict())


def create_dummy_char_dict(status):
    char_dict = {}
    char_dict['Name'] = 'Nowa postać'
    char_dict['Class'] = ''
    char_dict['Level'] = 1
    char_dict['Status'] = status
    char_dict['HP'] = 1
    char_dict['KP'] = 10
    char_dict['Att1'] = ''
    char_dict['Att1_mod'] = 0
    char_dict['Att1_dmg_mod'] = 0
    char_dict['Att2'] = ''
    char_dict['Att2_mod'] = 0
    char_dict['Att2_dmg_mod'] = 0
    char_dict['Class_mod'] = ''
    char_dict['Wytr'] = 0
    char_dict['Ref'] = 0
    char_dict['Wola'] = 0
    return char_dict
