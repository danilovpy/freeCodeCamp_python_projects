class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []
  

  def deposit(self, amount, description=""):
    obj = {'amount': float(amount), 'description': description,}
    self.ledger.append(obj)

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      amount = -amount
      obj = {'amount': amount, 'description': description,}
      self.ledger.append(obj)
      return True
    else:
      return False

  
  def get_balance(self):
    money = 0
    for obj in self.ledger:
      money+= obj['amount']
    return money


  def get_money_spent(self):
    money = 0
    for obj in self.ledger:
      if obj['amount']<0:
        money += obj['amount']
    return money


  def transfer(self, amount, category_obj):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {category_obj.name}")
      category_obj.deposit(amount, f"Transfer from {self.name}")
      return True
    else:
      return False

  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else: 
      return True

  def __str__(self):
    wide = 30
    name_len = len(self.name)
    stars = (wide-name_len)//2
    return_str = "*"*stars+ self.name +"*"*stars + "\n"
    info_str = ""
    for item in self.ledger:
      float_str = str("{:.2f}".format(item['amount']))[0:7]
      whitespaces = wide - (len(item['description'][0:23])+len(float_str))
      info_str += item['description'][0:23] + " "*whitespaces + str(float_str) + "\n"
    return_str = return_str + info_str + f"Total: {self.get_balance()}"
    return return_str
      

def total_money_spent(categories):
  money_spent = 0
  for category in categories:
    money_spent += category.get_money_spent()
  return money_spent

def longest_name_len(categories):
  categories = sorted(categories, key=lambda category: len(category.name), reverse=True)
  name_len = len(categories[0].name)
  return name_len

def create_spend_chart(categories):
  money_spent = total_money_spent(categories)
  result = ""
  for i in range(100,-20,-10):
    if i != -10:
      result += " "*(3-len(str(i)))+ str(i) +"|"+ " "
    else:
        result+= " "*4+"-"*len(categories)*3+"-"+"\n"
        break
    for category in categories:
      if i<= int(round(100*category.get_money_spent()/money_spent,1)) or i == 0:
        result+= "o"+"  "
      else:
        result+= "   "
    result+="\n"
  for n in range(longest_name_len(categories)):
    result+=" "*5
    for category in categories:
      try:
        result += category.name[n]+"  "
      except IndexError:
        result+="   "
    result+="\n"
  result = "Percentage spent by category\n"+result.rstrip("\n")
  return result