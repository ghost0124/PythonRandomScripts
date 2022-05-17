class ShoppingBasket:
    def __init__(self):
        self.items = []

    def addItem(self, item, count):
        for i in range(0, count):
            self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)

    def updateItem(self, item, newItem):
        if item in self.items:
            for i in range(0, len(self.items)):
                if item == self.items[i]:
                    self.items[i] = newItem

    def view(self):
        for i in range(0, len(self.items)):
            print(self.items[i].name + ' - ' + self.items[i].description)
            print(str(self.items[i].price) + '€')   

    def getTotalCost(self):
        cost = 0
        for i in range(0, len(self.items)):
            cost += self.items[i].price

        return str(cost) + '€'

    def reset(self):
        self.items.clear()

    def isEmpty(self):
        if self.items.count() == 0:
            return True
        else:
            return False


class Item:
  def __init__(self,name,description,price):
    self.name = name
    self.description = description
    self.price = price


tomatoSoup = Item("Tomato Soup","200mL can", 0.70)
spaghetti = Item("Spaghetti","500g pack", 1.10)
blackOlives = Item("Black Olives Jar","200g Jar", 2.10)
mozarella = Item("Mozarella","100g", 1.50)
gratedCheese = Item("Grated Cheese","100g",2.20)


myBasket = ShoppingBasket()

myBasket.addItem(tomatoSoup, 4)
myBasket.addItem(spaghetti, 1)
myBasket.addItem(blackOlives, 1)
myBasket.addItem(mozarella, 2)
myBasket.addItem(gratedCheese, 6)

myBasket.view()
print(myBasket.getTotalCost())

