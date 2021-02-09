class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def get_area(self):
    return self.width * self.height
  
  def get_perimeter(self):
    return self.width *2 + self.height *2
  
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5
  
  def set_height(self, height):
    if type(self) == Square:
      self.height = height
      self.width = height
      self.side = height
    self.height = height

  def set_width(self, width):
    if type(self) == Square:
      self.height = width
      self.width = width
      self.side = width
    self.width = width

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    picture = ""
    for i in range(self.height):
      picture+="*"*self.width + "\n"
    return picture
  
  def get_amount_inside(self, shape):
    if shape.width > self.width or shape.height > self.height:
      return 0
    times_height = self.height // shape.height
    times_width = self.width // shape.width
    return times_height * times_width

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'
    

class Square(Rectangle):

  def __init__(self, side):
    super().__init__( side, side)
    self.side = side

  def set_side(self, side):
    super().set_height(side)
    super().set_width(side)
    self.side = side

  def __str__(self):
    return f'Square(side={self.side})'

