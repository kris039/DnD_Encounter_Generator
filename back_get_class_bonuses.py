from pandas import read_csv


def get_class_bonuses(classs, level=1):
    lv_bonuses_df = read_csv('resources/lv_bonuses.csv', sep=';')
    bonus_row = lv_bonuses_df[lv_bonuses_df['Poziom'] == int(level)].iloc[0]
    if classs in ['Barbarzyńca', 'Kapłan', 'Łotrzyk', 'Paladyn', 'Wojownik']:
        return bonus_row['Profile_1']
    if classs in ['Druid', 'Bard', 'Mnich', 'Tropiciel']:
        return bonus_row['Profile_2']
    if classs in ['Czarodziej', 'Zaklinacz']:
        return bonus_row['Profile_3']
