from pandas import read_csv


def get_perk_by_name(perk_name):
    perks_df = read_csv('tables/perks.csv', sep=';')
    perk = perks_df.loc[perks_df['Nazwa'] == perk_name]
    return create_dict_from_additional(perk)


def get_perk_by_id(perk_id):
    perks_df = read_csv('tables/perks.csv', sep=';')
    perk = perks_df.loc[perks_df['ID'] == perk_id]
    return create_dict_from_additional(perk)


def get_item_by_name(item_name):
    items_df = read_csv('tables/consumables.csv', sep=';')
    item = items_df.loc[items_df['Nazwa'] == item_name]
    return create_dict_from_additional(item)


def get_item_by_id(item_id):
    items_df = read_csv('tables/consumables.csv', sep=';')
    item = items_df.loc[items_df['ID'] == item_id]
    return create_dict_from_additional(item)


def create_dict_from_additional(row):
    row_dict = {}
    row_dict.update({"ID": row['ID'].iloc[0]})
    row_dict.update({"Typ": row['Typ'].iloc[0]})
    row_dict.update({"Nazwa": row['Nazwa'].iloc[0]})
    row_dict.update({"Info": row['Info'].iloc[0]})
    row_dict.update({"Att_mod": row['Att_mod'].iloc[0]})
    row_dict.update({"Dmg_mod": row['Dmg_mod'].iloc[0]})
    return row_dict
