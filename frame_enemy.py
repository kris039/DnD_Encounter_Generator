from frame_character import Character


class Enemy(Character):
    def __init__(self, master, char_id, char_dict):
        super().__init__(master, char_id, char_dict)
        self.status.set('Przeciwnik')
