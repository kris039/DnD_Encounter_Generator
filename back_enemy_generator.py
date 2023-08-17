import random
from pandas import read_csv, isna, DataFrame
# import pandas


def generate_enemy(r, enemy_r, class_r):
    perks_df = read_csv('tables/perks.csv', sep=';')
    items_df = read_csv('tables/consumables.csv', sep=';')
    name = (r[0] + ' ' + r[1] + ' lv ' + r[2])
    hp = int(enemy_r['KW_mod'].iloc[0] * random.randint(1, enemy_r['KW_k'].iloc[0]))
    if hp == 0:
        hp = 1
    if int(r[2]) > 1:
        for i in range(int(r[2])-1):
            hp += int(class_r['KW_mod'].iloc[0]*random.randint(1, class_r['KW_d'].iloc[0]))
    kp = enemy_r['KP'].iloc[0]
    att1 = enemy_r['Atak_1'].iloc[0]
    att1_mod = enemy_r['Atak_1_mod'].iloc[0]
    att1_dmg_mod = enemy_r['Atak_1_dmg_mod'].iloc[0]
    att2 = enemy_r['Atak_2'].iloc[0]
    att2_mod = enemy_r['Atak_2_mod'].iloc[0]
    att2_dmg_mod = enemy_r['Atak_2_dmg_mod'].iloc[0]
    wytr = enemy_r['Wytrw'].iloc[0]
    ref = enemy_r['Ref'].iloc[0]
    wola = enemy_r['Wola'].iloc[0]

    additional_dict = {"Typ": [], "Nazwa": [], "Info": [], "Att_mod": [], "Dmg_mod": []}
    for i in range(int(r[2])):
        perk = perks_df.iloc[random.randint(0, len(perks_df)-1)]
        additional_dict["Typ"].append(perk['Typ'])
        additional_dict["Nazwa"].append(perk['Nazwa'])
        additional_dict["Info"].append(perk['Info'])
        additional_dict["Att_mod"].append(perk['Att_mod'])
        additional_dict["Dmg_mod"].append(perk['Dmg_mod'])

    items = enemy_r['Item'].iloc[0]
    if not isna(items):
        for i in items.split(','):
            if float(i.split('/')[1]) >= random.randint(0, 100) / 100:
                item = items_df.loc[items_df['Nazwa'] == i.split('/')[0]]
                additional_dict["Typ"].append(item['Typ'].iloc[0])
                additional_dict["Nazwa"].append(item['Nazwa'].iloc[0])
                additional_dict["Info"].append(item['Info'].iloc[0])
                additional_dict["Att_mod"].append(item['Att_mod'].iloc[0])
                additional_dict["Dmg_mod"].append(item['Dmg_mod'].iloc[0])

    # print(additional_dict)
    additional = DataFrame(additional_dict)
    # pandas.set_option('display.max_columns', None)
    # print(additional)
    return [name, hp, kp, att1, att1_mod, att1_dmg_mod, att2, att2_mod, att2_dmg_mod, wytr, ref, wola, additional]
