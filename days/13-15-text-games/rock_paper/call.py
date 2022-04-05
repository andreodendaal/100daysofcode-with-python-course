class Call:

    def __init__(self, type) -> type:
        self.roll_type = type

    def can_defeat(self, opposition_type):
        if self.roll_type == 'rock' and opposition_type == 'scissors':
            return 'win'
        elif self.roll_type == 'rock' and opposition_type == 'paper':
            return 'lose'

        elif self.roll_type == 'scissors' and opposition_type == 'paper':
            return 'win'
        elif self.roll_type == 'scissors' and opposition_type == 'rock':
            return 'lose'

        elif self.roll_type == 'paper' and opposition_type == 'rock':
            return 'win'
        elif self.roll_type == 'paper' and opposition_type == 'scissors':
            return 'lose'
        else:
            return 'draw'

