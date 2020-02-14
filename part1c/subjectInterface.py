from abc import ABC, abstractmethod

#defines the interface for the Observable with an abstract class.

class Subject(ABC):

    @abstractmethod
    def notifyObservers(self, **kwargs):
        pass

    @abstractmethod
    def stateChange(self, **kwargs):
        pass

    @abstractmethod
    def registerObserver(self, observer):
        pass

    @abstractmethod
    def removeObserver(self, observer):
        pass



