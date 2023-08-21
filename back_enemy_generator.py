import random
from pandas import read_csv, isna, DataFrame
from back_get_class_bonuses import get_class_bonuses


def generate_enemy(r, enemy_r, class_r):
    perks_df = read_csv('tables/perks.csv', sep=';')
    items_df = read_csv('tables/consumables.csv', sep=';')
    lv_perks_df = read_csv('tables/lv_skills.csv', sep=';')
    lv_drop_df = read_csv('tables/lv_items.csv', sep=';')
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

    additional_dict = {"Typ": [], "Nazwa": [], "Info": [], "Att_mod": [], "Dmg_mod": []}

    bonus_row = lv_perks_df.loc[lv_perks_df['Poziom'] == int(r[2])]

    for i in range(bonus_row['Atuty'].iloc[0]):
        perk = perks_df.iloc[random.randint(0, len(perks_df)-1)]
        additional_dict["Typ"].append(perk['Typ'])
        additional_dict["Nazwa"].append(perk['Nazwa'])
        additional_dict["Info"].append(perk['Info'])
        additional_dict["Att_mod"].append(perk['Att_mod'])
        additional_dict["Dmg_mod"].append(perk['Dmg_mod'])

    items_row = lv_drop_df.loc[lv_drop_df['Poziom'] == int(r[2])]
    items = enemy_r['Item'].iloc[0]
    items2 = items_row['Item'].iloc[0]
    if not isna(items):
        for i in items.split(',') + items2.split(','):
            if float(i.split('/')[1]) >= random.randint(0, 100) / 100:
                item = items_df.loc[items_df['Nazwa'] == i.split('/')[0]]
                additional_dict["Typ"].append(item['Typ'].iloc[0])
                additional_dict["Nazwa"].append(item['Nazwa'].iloc[0])
                additional_dict["Info"].append(item['Info'].iloc[0])
                additional_dict["Att_mod"].append(item['Att_mod'].iloc[0])
                additional_dict["Dmg_mod"].append(item['Dmg_mod'].iloc[0])

    additional = DataFrame(additional_dict)
    return [char_dict, additional]
