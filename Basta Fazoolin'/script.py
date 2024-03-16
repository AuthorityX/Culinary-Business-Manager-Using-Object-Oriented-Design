class Business: 
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return self.address

  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if menu.start_time <= time and time <= menu.end_time:
        available_menus.append(menu)
    if available_menus == []:
      return "We are not open!"
    else:
      return available_menus

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    if self.start_time < 12:
      start_p = "am"
    elif self.start_time == 12:
      start_p = "pm"
    elif self.start_time == 24:
      start_p = "am"
    else: 
      start_p = "pm"
    
    if self.end_time < 12:
      end_p = "am"
    elif self.end_time == 12:
      end_p = "pm"
    elif self.end_time == 24:
      end_p = "am"
    else:
      end_p = "pm"

    if self.start_time > 12:
      start_t = self.start_time - 12
    elif self.start_time == 24:
      start_t = 12
    else: 
      start_t = self.start_time

    if self.end_time > 12:
      end_t = self.end_time - 12
    elif self.end_time == 24:
        end_t = 12
    else: 
      end_t = self.end_time 

    return "{} menu available from {}{} to {}{}".format(self.name, start_t, start_p, end_t, end_p)

  def calculate_bill(self, purchased_items):
    total_items = 0
    for item in purchased_items:
      if item in self.items:
        total_items += self.items[item]
    return total_items

brunch = Menu("brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 11, 16)

early_bird = Menu("early_bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}, 15, 18)

dinner = Menu("dinner", {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}, 17, 23)

kids = Menu("kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 11, 21)

arepas_menu = Menu("arepas menu", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, 10, 20)

menus = [brunch, early_bird, dinner, kids]
arepas_menus = [arepas_menu]

flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menus)

business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepa = Business("Take a' Arepa", [arepas_place])

print(arepas_place.available_menus(17))
print(arepa.franchises[0].menus[0])
print(arepas_menu.items)
