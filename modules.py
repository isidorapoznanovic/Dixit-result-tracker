def isitint(n):
    try: 
        int(n)
        return True
    except ValueError:
        return False

class Player:
    
    def __init__(self, name, score, wins, vote, card):
        self.name = name
        self.score = score
        self.wins = wins
        self.vote = vote
        self.card = card


   
    