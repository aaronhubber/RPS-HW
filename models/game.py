class Game:
    def __init__(self, player1, player2):
        self.player1name = player1.get_name()
        self.player1weapon = player1.get_weapon()
        self.player2name = player2.get_name()
        self.player2weapon = player2.get_weapon()
        self.winner = ""
        self.winner_weapon = ""
        self.loser = ""
        

    def play_game(self):
    
        if self.player1weapon == self.player2weapon:
            return None
    
        if self.player1weapon == "rock":
            if self.player2weapon == "scissors":
                self.winner = self.player1name
                self.winner_weapon = self.player1weapon
                self.loser = self.player2name
            else:
                self.winner = self.player2name
                self.winner_weapon = self.player2weapon
                self.loser = self.player1name

        if self.player1weapon == "scissors":
            if self.player2weapon == "paper":
                self.winner = self.player1name
                self.winner_weapon = self.player1weapon
                self.loser = self.player2name
            else:
                self.winner = self.player2name
                self.winner_weapon = self.player2weapon
                self.loser = self.player1name

        if self.player1weapon == "paper":
            if self.player2weapon == "rock":
                self.winner = self.player1name
                self.winner_weapon = self.player1weapon
                self.loser = self.player2name
            else:
                self.winner = self.player2name
                self.winner_weapon = self.player2weapon
                self.loser = self.player1name
        
        return f"{self.winner} has triumphed by using their mighty {self.winner_weapon} to slay {self.loser}." 


