import random


def attack(attacker, attacked, weapons_df, nr):
    text = ''
    weapon = weapons_df.loc[weapons_df['Nazwa'] == attacker.att1.get()]
    dmg = 0
    att_mod = 0
    dmg_mod = 0
    if nr == 1:
        att_mod = int(attacker.att1_mod.get())
        dmg_mod = int(attacker.att1_dmg_mod.get())
        info = ' pierwszą bronią'
    elif nr == 2:
        att_mod = int(attacker.att2_mod.get())
        dmg_mod = int(attacker.att2_dmg_mod.get())
        info = ' drugą bronią'
    else:
        return 'Błędny parametr ataku'

    text += '\n' + attacker.name.get() + ' zaatakował ' + attacked.name.get() + info
    hit_throw = random.randint(1, 20)

    if hit_throw >= weapon['Kryt_próg'].iloc[0]:
        text += ('\n\t' + attacker.name.get() + ': Rzut k20 na trafienie: ' + str(hit_throw)
                 + ' - TRAFIENIE KRYTYCZNE')
        for i in range(weapon['Kryt_mnożnik'].iloc[0]):
            dmg_throw = random.randint(1, weapon['Obrażenia'].iloc[0])
            dmg += dmg_throw + dmg_mod
            text += ('\n\t' + attacker.name.get() + ': Rzut k' + str(weapon['Obrażenia'].iloc[0]) + ' na obrażenia: '
                     + str(dmg_throw) + ' + modyfikator obrażeń: ' + str(dmg_mod))
        text += '\n\t' + attacker.name.get() + ' zadał ' + str(dmg) + ' punktów obrażeń'
    elif hit_throw + att_mod >= int(attacked.kp.get()):
        text += '\n\t' + attacker.name.get() + ': Rzut k20 na trafienie: ' + str(hit_throw)
        text += '\n\t' + 'KP: ' + attacked.kp.get() + ' vs Rzut: ' + str(hit_throw) + ' + modyfikator ataku: ' + str(att_mod)
        dmg_throw = random.randint(1, weapon['Obrażenia'].iloc[0])
        dmg += dmg_throw + dmg_mod
        text += ('\n\t' + attacker.name.get() + ': Rzut k' + str(weapon['Obrażenia'].iloc[0]) + ' na obrażenia: '
                 + str(dmg_throw) + ' + modyfikator obrażeń: ' + str(dmg_mod))
        text += '\n\t' + attacker.name.get() + ' zadał punktów obrażeń ' + str(dmg)

    else:
        text += '\n\t' + attacker.name.get() + ': Rzut k20 na trafienie: ' + str(hit_throw)
        text += '\n\t' + 'KP: ' + attacked.kp.get() + ' vs Rzut+mod: ' + str(hit_throw) + str(att_mod)
        text += '\n\t' + attacker.name.get() + ' chybił'
    return text

