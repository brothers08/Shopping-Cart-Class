class Cart:
  def __init__(self, total = 0, items = {}):
    self.total = total
    self.items = items
    self.balance = 0
  
  #Add item to cart
  def add_item(self, item, price, quantity):
    if item not in self.items:
      self.items[item] = [price, quantity]
    else:
      self.items[item][1] += quantity

    self.total += price * quantity
  
  #Remove item from cart
  def rem_item(self, item, quantity):
    self.total -= self.items[item][0] * quantity

    if quantity == self.items[item][1]:
      self.items.pop(item)
    else:
      self.items[item][1] -= quantity
      
  #Print items dictionary
  def get_items(self):
    print(self.items)
  
  #Print total price of cart
  def get_total(self):
    print(self.total)
  
  #Checkout items
  def checkout(self, payment):
    if payment > self.total:
      return "Thank you! Here's your change: $" + str(round(payment - self.total, 2))
    if payment < self.total:
      self.total = self.total - payment
      return "Payment not enough. You still owe: $" + str(round(self.total, 2))
    
    return "Thank you for shopping with us!"
  
#### Tests ####
myCart = Cart()

myCart.add_item("soda", 0.99, 2)
myCart.add_item("cereal", 2.49, 1)
myCart.add_item("bread", 1.75, 1)
myCart.add_item("apples", 0.49, 3)
print(myCart.items)
print(round(myCart.total, 2))

myCart.add_item("soda", 0.99, 2)
print(myCart.items)
print(round(myCart.total, 2))

myCart.rem_item("soda", 1)
myCart.rem_item("cereal", 1)
print(myCart.items)
print(round(myCart.total, 2))

print(myCart.checkout(5.00))
print(myCart.checkout(2.00))
