class History:
    def __init__(self):
        self.rounds = []

    def add_round(self, round_info):
        self.rounds.append(round_info)

    def get_history(self):
        return self.rounds