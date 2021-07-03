class Canvas():

  def __init__(self, height, width):
    self.height = height
    self.width = width

  def add_shape(shape):
    """Takes a shape object and adds it to the canvas"""
    # Notes: shape will start at a particular x & y axis.
    # Shape should not be printed out of the boundary of the canvas

  
  def clear_shape():
    """Clears canvas of any existing art"""


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
    