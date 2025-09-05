#Real Life Example : MCDonald's uses those Chaos Machines to take orders or add items to orders. 
#Lets create a function to make a hamburger

def makeHamburger(): 
  print("Cook Meat")
  print("Add Meat to Bun")
  print("Server the customer")
makeHamburger()
#def makeHamburger(): in the () we can add parameters
def makeHamburger(cheese,Onion): 
  print("Cook Meat")
  print("Add Meat to Bun")
  print("Add Cheese: {0}".format(cheese))
  print("Add Onion: {0}".format(Onion))
  print("Server the customer")
makeHamburger(1, 1)
makeHamburger(10, 1)
makeHamburger(0, 1)
makeHamburger(0, 0)
