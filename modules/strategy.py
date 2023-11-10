from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def decide(self, game_state):
        pass