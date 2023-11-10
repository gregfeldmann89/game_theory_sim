class Game:
    def __init__(self, players, payoff_matrix):
        self.players = players
        self.payoff_matrix = payoff_matrix
        self.history = []
        self.current_state = None

    def play_round(self):
        # Logic for playing a single round
        pass

    def get_payoff(self):
        # Calculate and return the payoff for the current state
        pass

    def update_state(self):
        # Update the game state after each round
        pass