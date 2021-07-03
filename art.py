class Canvas():

  def __init__(self, height, width):
    self.height = height
    self.width = width
    self.shapes = []
    self.outline = {}

  def create_canvas(self):
    """Create dictionary with the appropriate key:value pair structure to represent canvas"""

    for h in range (1, self.height +1):
        self.outline[h] = {}
      
        for w in range(1, self.width +1):
          self.outline[h][w] = " "

  def print_canvas(self):
    """Print canvas to console"""

    for h in range (1, self.height +1):  
        line_to_print = ' '    
        for w in range(1, self.width +1):
          line_to_print += self.outline[h][w]
          
          if w == self.width:
            print(line_to_print)


  def add_shape(self, shape):
    """Takes a shape object and adds it to the canvas"""
    # Notes: shape will start at a particular x & y axis.
    # Shape should not be printed out of the boundary of the canvas
    self.shapes.append(shape)

  
  def clear_shape(self):
    """Clears canvas of any existing art"""
    self.create_canvas()


class Shape():

  def __init__(self, start_x, start_y, end_x, end_y, fill_char):
    self.start_x = start_x #X coordinate of the upper-left-hand corner of the rectangle
    self.start_y = start_y #Y coordinate of the upper-left-hand corner of the rectangle
    self.end_x = end_x #X coordinate of the lower-right-hand corner of the rectangle
    self.end_y = end_y #Y coordinate of the lower-right-hand corner of the rectangle
    self.fill_char = fill_char #the character that should be used to draw the rectangle

  
  def update_fill_char(self, update_fill_char):
    """Change the fill character to use in order to draw a pre-existing rectangle"""
    self.fill_char = update_fill_char

  def translate(self, axis, num):
    """Moves the recentage on the 'y' or 'x' axis, by a given number."""
    if type(num) is not int:
      print("Value provided must be an integer")
      return
    
    if axis == 'x':
      self.start_x += num
      self.end_x += num
    
    elif axis == 'y':
      self.start_y += num
      self.end_y += num
    
    else:
      print("Axis value must be 'y' or 'x'")


