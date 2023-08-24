from back_adds_funtions import *
from tkinter import filedialog
from pandas import read_csv, DataFrame, concat as df_concat


def save_characters(characters, who=''):
    path = filedialog.asksaveasfilename(defaultextension='.csv')
    if path != '':
        characters_df = DataFrame()
        for char in characters:
            if char.status.get() == who or who == '':
                char_dict = {}
                char_dict.update({'Name': [char.name.get().split(' ID:')[0]]})
                char_dict.update({'Class': [char.classs.get()]})
                char_dict.update({'Level': [char.level.get()]})
                char_dict.update({'Status': [char.status.get()]})
                char_dict.update({'HP': [char.hp.get()]})
                char_dict.update({'KP': [char.kp.get()]})
                char_dict.update({'Att1': [char.att1.get()]})
                char_dict.update({'Att1_mod': [char.att1_mod.get()]})
                char_dict.update({'Att1_dmg_mod': [char.att1_dmg_mod.get()]})
                char_dict.update({'Att2': [char.att2.get()]})
                char_dict.update({'Att2_mod': [char.att2_mod.get()]})
                char_dict.update({'Att2_dmg_mod': [char.att2_dmg_mod.get()]})
                char_dict.update({'Class_mod': [char.class_mod.get()]})
                char_dict.update({'Wytr': [char.wytr.get()]})
                char_dict.update({'Ref': [char.ref.get()]})
                char_dict.update({'Wola': [char.wola.get()]})
                try:
                    perks = ','.join(char.perks)
                except TypeError:
                    perks = ''
                try:
                    spells = ','.join(char.spells)
                except TypeError:
                    spells = ''
                try:
                    items = ','.join(char.items)
                except TypeError:
                    items = ''
                char_dict.update({'Perks': [perks]})
                char_dict.update({'Spells': [spells]})
                char_dict.update({'Items': [items]})
                characters_df = df_concat([characters_df, DataFrame(char_dict)], ignore_index=True)
        print(characters_df)
        if len(characters_df) != 0:
            characters_df.to_csv(path, ';', index=False)


def load_characters(func_add_player, func_add_enemy, who='', path=''):
    if path == '':
        path = filedialog.askopenfilename(defaultextension='.csv')
    if path != '':
        loaded = read_csv(path, sep=';')
        for i, j in loaded.iterrows():
            if j['Status'] == who or who == '':
                if j['Status'] == 'Gracz':
                    func_add_player(j.fillna('').to_dict())
                if j['Status'] == 'Przeciwnik':
                    func_add_enemy(j.fillna('').to_dict())


def create_dummy_char_dict(status):
    char_dict = {}
    char_dict.update({'Name': 'Nowa postać'})
    char_dict.update({'Class': ''})
    char_dict.update({'Level': 1})
    char_dict.update({'Status': status})
    char_dict.update({'HP': 1})
    char_dict.update({'KP': 10})
    char_dict.update({'Att1': ''})
    char_dict.update({'Att1_mod': 0})
    char_dict.update({'Att1_dmg_mod': 0})
    char_dict.update({'Att2': ''})
    char_dict.update({'Att2_mod': 0})
    char_dict.update({'Att2_dmg_mod': 0})
    char_dict.update({'Class_mod': ''})
    char_dict.update({'Wytr': 0})
    char_dict.update({'Ref': 0})
    char_dict.update({'Wola': 0})
    char_dict.update({'Perks': []})
    char_dict.update({'Spells': []})
    char_dict.update({'Items': []})
    return char_dict
