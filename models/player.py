class Player():
    def __init__(self, input_name, input_weapon):
        self.name = input_name
        self.weapon = input_weapon
    
    def get_name(self):
        return self.name
    
    def get_weapon(self):
        return self.weapon