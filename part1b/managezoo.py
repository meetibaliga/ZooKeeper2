from zooanimals import *
from zookeeper import *
from animal import *


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

olivia = Owl("Olivia")
oscar = Owl("Oscar")

steve = Sparrow("Steve")
sam = Sparrow("Sam")

paul = Penguin("Paul")
polly = Penguin("Polly")

tracy = Trout("Tracy")
trump = Trout("Trump")

kelly = Koi("Kelly")
kate = Koi("Kate")

bob = Bass("Bob")
bailey = Bass("Bailey")

alist = [colt, cam, tim, tan, lucy, lidia, ed, ema, henry, holt, rim, rob, will, war, dale, dan, tracy, trump, kelly, kate, bob, bailey, olivia, oscar, steve, sam, paul, polly]
z = Zookeeper()
z.wakeAnimals(alist)
z.rollCallAnimals(alist)
z.feedAnimals(alist)
z.exerciseAnimals(alist)
z.shutDownZoo(alist)
