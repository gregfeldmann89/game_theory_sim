class Player:
    def __init__(self, strategy):
        self.strategy = strategy
        self.score = 0

    def make_move(self, game_state):
        # Use strategy to determine the move
        return self.strategy.decide(game_state)

    def update_score(self, payoff):
        self.score += payoff