
class Paper:
    roll_type = 'paper'

    def can_defeat(self, opposition_type):
        self.opposition_type = opposition_type
        if self.opposition_type == 'rock':
            return True
        else:
            return False

class Rock:
    roll_type = 'rock'

    def can_defeat(self, opposition_type):
        self.opposition_type = opposition_type
        if self.opposition_type == 'scissors':
            return True
        else:
            return False

class Scissors:
    roll_type = 'scissors'

    def can_defeat(self, opposition_type):
        self.opposition_type = opposition_type
        if self.opposition_type == 'paper':
            return True
        else:
            return False
        