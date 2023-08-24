from pandas import read_csv, DataFrame
import random


def get_perk_by_name(perk_name):
    perks_df = read_csv('resources/perks.csv', sep=';')
    perk = perks_df.loc[perks_df['Nazwa'] == perk_name].iloc[0]
    return perk


def get_perk_by_id(perk_id):
    perks_df = read_csv('resources/perks.csv', sep=';')
    perk = perks_df.loc[perks_df['ID'] == perk_id].iloc[0]
    return perk


def get_spell_by_id(spell_id):
    spells_df = read_csv('resources/spells.csv', sep=';')
    spell = spells_df.loc[spells_df['ID'] == spell_id].iloc[0]
    return spell


def get_item_by_name(item_name):
    items_df = read_csv('resources/consumables.csv', sep=';')
    item = items_df.loc[items_df['Nazwa'] == item_name].iloc[0]
    return item


def get_item_by_id(item_id):
    items_df = read_csv('resources/consumables.csv', sep=';')
    item = items_df.loc[items_df['ID'] == item_id].iloc[0]
    return item


def create_dict_from_additional(row):
    row_dict = {}
    row_dict.update({"ID": row['ID']})
    row_dict.update({"Typ": row['Typ']})
    row_dict.update({"Nazwa": row['Nazwa']})
    row_dict.update({"Info": row['Info']})
    row_dict.update({"Att_mod": row['Att_mod']})
    row_dict.update({"Dmg_mod": row['Dmg_mod']})
    return row_dict


def get_random_info_id(add_type, add_class=''):
    if add_type == 'Atut':
        perk_ids_df = read_csv('resources/perks.csv', sep=';')['ID']
        return perk_ids_df.iloc[random.randint(0, len(perk_ids_df) - 1)]
    if add_type == 'Czar':
        spells_df = read_csv('resources/spells.csv', sep=';')
        class_spell_ids = spells_df[spells_df['Klasa'] == add_class]['ID']
        return class_spell_ids.iloc[random.randint(0, len(class_spell_ids) - 1)]
