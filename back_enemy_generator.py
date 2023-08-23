import random
from pandas import read_csv, isna, DataFrame
from back_get_class_bonuses import get_class_bonuses
from back_adds_funtions import *


def generate_enemy(r, enemy_r, class_r):
    lv_perks_df = read_csv('tables/lv_skills.csv', sep=';')
    lv_items_df = read_csv('tables/lv_items.csv', sep=';')
    char_dict = {}
    char_dict.update({'Name': str(r[0] + ' ' + r[1] + ' lv ' + r[2])})
    char_dict.update({'Class': str(r[1])})
    char_dict.update({'Level': int(r[2])})

    hp = int(enemy_r['KW_mod'].iloc[0] * random.randint(1, enemy_r['KW_k'].iloc[0]))
    if hp == 0:
        hp = 1
    if int(r[2]) > 1:
        for i in range(int(r[2])-1):
            hp += int(class_r['KW_mod'].iloc[0]*random.randint(1, class_r['KW_d'].iloc[0]))
    char_dict.update({'HP': hp})

    char_dict.update({'KP': enemy_r['KP'].iloc[0]})
    char_dict.update({'Att1': enemy_r['Atak_1'].iloc[0]})
    char_dict.update({'Att1_mod': enemy_r['Atak_1_mod'].iloc[0]})
    char_dict.update({'Att1_dmg_mod': enemy_r['Atak_1_dmg_mod'].iloc[0]})
    char_dict.update({'Att2': enemy_r['Atak_2'].iloc[0]})
    char_dict.update({'Att2_mod': enemy_r['Atak_2_mod'].iloc[0]})
    char_dict.update({'Att2_dmg_mod': enemy_r['Atak_2_dmg_mod'].iloc[0]})
    char_dict.update({'Class_mod': get_class_bonuses(str(r[1]), r[2])})
    char_dict.update({'Wytr': enemy_r['Wytrw'].iloc[0]})
    char_dict.update({'Ref': enemy_r['Ref'].iloc[0]})
    char_dict.update({'Wola': enemy_r['Wola'].iloc[0]})

    additional = DataFrame()

    bonus_row = lv_perks_df.loc[lv_perks_df['Poziom'] == int(r[2])]

    for i in range(bonus_row['Atuty'].iloc[0]):
        additional = additional.append(get_random_additional('Atut'), ignore_index=True)

    for i in range(int(int(r[2])/3)):
        additional = additional.append(get_random_additional('Czar', r[1]), ignore_index=True)

    items_row = lv_items_df.loc[lv_items_df['Poziom'] == int(r[2])]
    items = enemy_r['Item'].iloc[0]
    items2 = items_row['Item'].iloc[0]
    if not isna(items):
        for i in items.split(',') + items2.split(','):
            if float(i.split('/')[1]) >= random.randint(0, 100) / 100:
                additional = additional.append(get_item_by_name(i.split('/')[0]), ignore_index=True)
    additional = additional.fillna(0)
    return [char_dict, additional]
