class CoffeeCup():
# The __init__ method is a special method Python executes
# When a new cup of coffee is created.
  def __init__(self, capacity):
    # Self keyword is similar to "this"
    # Self isn't automatically assigned like this is
    self.capacity = capacity
    self.amount = 0

  # This is a method
  def fill(self):
    self.amount = self.capacity

  def empty(self):
    self.amount = 0

  def drink(self, amount):
    self.amount -= amount
    if(self.amount <= 0):
      self.amount = 0

lys_cup = CoffeeCup(12) # Tall dirty chai
brandis_cup = CoffeeCup(2) # A quick espresso
jacksons_cup = CoffeeCup(16) # Jackson needs his fix

lys_cup.fill()
jacksons_cup.fill()
brandis_cup.fill()


lys_cup.drink(1)
jacksons_cup.drink(12)
brandis_cup.drink(2)
# Printing like this shows where it's stored in memory.
# print(lys_cup,brandis_cup,jacksons_cup)

print(lys_cup.amount,brandis_cup.amount,jacksons_cup.amount)