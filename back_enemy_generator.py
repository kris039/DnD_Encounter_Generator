import random
from pandas import read_csv, isna


def generate_enemy(r, enemy_r, class_r):
    perks_df = read_csv('tables/perks.csv', sep=';')
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
    perks = []
    for i in range(int(r[2])):
        perks.append(perks_df.iloc[random.randint(0, len(perks_df)-1)])

    drop = []
    pre_drop = enemy_r['Drop'].iloc[0]
    if not isna(pre_drop):
        for i in pre_drop.split(','):
            if float(i.split('/')[1]) >= random.randint(0, 100) / 100:
                drop.append(i.split('/')[0])
    return [name, hp, kp, att1, att1_mod, att1_dmg_mod, att2, att2_mod, att2_dmg_mod, wytr, ref, wola, perks, drop]
