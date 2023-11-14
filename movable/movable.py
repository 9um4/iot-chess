from abc import ABC, abstractmethod

class Movable(ABC):
    @abstractmethod
    def move(self, move: int = 1):
        pass