from pandas import read_csv


def get_class_bonuses(classs, level):
    lv_bonuses_df = read_csv('tables/lv_skills.csv', sep=';')
    classs_row = lv_bonuses_df.loc[lv_bonuses_df['Poziom'] == level]
#     if ['Barbarzyńca',
# 'Bard'
# 'Czarodziej'
# 'Druid'
# 'Kapłan'
# 'Łotrzyk'
# 'Mnich'
# 'Paladyn'
# 'Tropiciel'
# 'Wojownik'
# 'Zaklinacz'
