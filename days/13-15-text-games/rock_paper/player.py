class Player:
    
    def __init__(self, p_name):
        self.name = p_name
        self.score = 0

    def score_total(self, increment):
        self.score += increment
        return self.score


         