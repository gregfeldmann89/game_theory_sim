class Player:
    def __init__(self, player_id, strategy):
        self.player_id = player_id
        self.strategy = strategy
        self.score = 0  # Score can be utility, money, points, etc.

    def make_move(self, game_state):
        """
        Uses the player's strategy to decide the next move based on the current game state.
        """
        return self.strategy.decide(game_state)

    def update_score(self, payoff):
        """
        Updates the player's score based on the received payoff.
        """
        self.score += payoff

    def reset_score(self):
        """
        Resets the player's score to zero.
        """
        self.score = 0

    def __str__(self):
        """
        Returns a string representation of the player's status.
        """
        return f'Player {self.player_id}: Score = {self.score}'
