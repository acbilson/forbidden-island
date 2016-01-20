class WaterMarker(object):

  def __init__(self, startingPosition):
    self.position = startingPosition
    self.maxPosition = 6

  def raise_water_level(self):
    """ Raise the position of the marker after Waters Rise event """
    pass 

  def get_current_level(self):
    """ Gets the current position of the water marker """
    pass 
  
  def OnIslandSinks(self):
    """ Event when the marker reaches the final stage and the island sinks """
    pass
