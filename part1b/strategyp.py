from abc import ABC, abstractmethod

#contains the strategy pattern for roam.


# abstract class to make an interface for the abstract strategy roam
class RoamStrategyAbstract(ABC):

    @abstractmethod
    def roam(self):
        pass

#1 roam strategy interface
class RoamBySwimStrategy(RoamStrategyAbstract):

    def roam(self):
        return " is swimming by Strategy."

#2 roam strategy interface
class RoamByFlyStrategy(RoamStrategyAbstract):

    def roam(self):
        return " is flying by Strategy."

#3 roam strategy interface
class RoamNormalStrategy(RoamStrategyAbstract):

    def roam(self):
        return " is roaming by NormalStrategy."
