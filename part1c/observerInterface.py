from abc import ABC, abstractmethod

#interface for the observer with an abstract class.
class Observer(ABC):

    @abstractmethod
    def update(self, info):
        pass
