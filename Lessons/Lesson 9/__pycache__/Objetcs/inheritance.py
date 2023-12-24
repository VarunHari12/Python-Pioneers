# sub classes can inherit attrubutes and methods from the parent class
# it is just like an animal, the next generation inherits the traits from the previous gen and adds some more

# ex. parent class is animal, subclass is eagle or pig
# check animal file for more info

from animal import *

hawk = Hawk()
print(hawk.alive)

hawk.sleep()

# this hawk class inherits the attributes and methods of the parent class (alive and sleep)

hawk.fly()

# At the same time, the hawk class cna use its own methods that no other class can use such as the fly method

# hawk.hop()

# this wont work since the hawk does not inherit methods from other child classes



# --------------------------------------------------------------------------------



# we also have multi-level-inheritance which is when a child class is derived from another child class

baby = BabyHawk()

print(baby.alive)

baby.sleep()

baby.fly()

baby.cry()

# The multi-level-inherited class can still use the attributes and methods of all of the previous parent classes before it and make its own new methods
