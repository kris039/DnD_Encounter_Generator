from back_adds_funtions import *
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
                adds = ''
                for add in char.additional['ID'].to_list():
                    adds += add+','
                char_dict['Additional_IDs'] = adds
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
                    adds = j['Additional_IDs'].split(',')
                    adds.remove('')
                    add_df = DataFrame()
                    if len(adds) != 0:
                        for add in adds:
                            if add[0] == 'p':
                                add_df = add_df.append(get_perk_by_id(add), ignore_index=True)
                            if add[0] == 's':
                                add_df = add_df.append(get_perk_by_id(add), ignore_index=True)
                            if add[0] == 'i':
                                add_df = add_df.append(get_item_by_id(add), ignore_index=True)
                    func_add_enemy(j.to_dict(), add_df)


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
