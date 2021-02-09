import copy
import random

class Hat():

  def __init__(self, **kwargs):
    self.contents = []
    for k,v in kwargs.items():
      for i in range(v):
        self.contents.append(k)

  def draw(self, number):
    if number >= len(self.contents):
      return self.contents

    return_list = []
    for i in range(number):
      return_list.append(self.contents.pop(random.randint(0,len(self.contents)-1)))

    return return_list
   
  def create_list(self, expected_balls):
    return_list = []
    for k,v in expected_balls.items():
      for i in range(v):
        return_list.append(k)
    return return_list

def check(bigger_list, smaller_list):
  try:
    [bigger_list.remove(x) for x in smaller_list]
    return True
  except:
    return False

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  expected_balls = hat.create_list(expected_balls)
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    balls = hat_copy.draw(num_balls_drawn)
    if check(balls, expected_balls):
      count += 1
  return count/num_experiments

