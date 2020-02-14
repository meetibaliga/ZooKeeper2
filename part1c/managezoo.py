from zooanimals import *
from zookeeper import *
from zooannouncer import *


colt = Cat("Colt")
cam = Cat("Cam")

tim = Tiger("Tim")
tan = Tiger("Tan")

lucy = Lion("Lucy")
lidia = Lion("Lidia")

ed = Elephant("Ed")
ema = Elephant("Ema")

henry = Hippo("Henry")
holt = Hippo("Holt")

rim = Rhino("Rim")
rob = Rhino("Rob")

will = Wolf("Will")
war = Wolf("War")

dale = Dog("Dale")
dan = Dog("Dan")

tracy = Trout("Tracy")
trump = Trout("Trump")

kelly = Koi("Kelly")
kate = Koi("Kate")

bob = Bass("Bob")
bailey = Bass("Bailey")

olivia = Owl("Olivia")
oscar = Owl("Oscar")

steve = Sparrow("Steve")
sam = Sparrow("Sam")

paul = Penguin("Paul")
polly = Penguin("Polly")


alist = [colt, cam, tim, tan, lucy, lidia, ed, ema, henry, holt, rim, rob, will, war, dale, dan, tracy, trump, kelly, kate, bob, bailey, olivia, oscar, steve, sam, paul, polly]


zanc1 = ZooAnnouncer("Number#1")
zanc2 = ZooAnnouncer("Number#2")

z = Zookeeper()

z.listObservers()

z.registerObserver(zanc1)
z.registerObserver(zanc2)

z.listObservers()

z.wakeAnimals(alist)
z.rollCallAnimals(alist)
z.feedAnimals(alist)
z.exerciseAnimals(alist)
z.shutDownZoo(alist)

z.removeObserver(zanc1)
z.removeObserver(zanc2)

z.listObservers()

del zanc1
del zanc2
