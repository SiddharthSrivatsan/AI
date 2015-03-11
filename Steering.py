from random import randint
import numpy as np
import matplotlib.pyplot as plt

class PVector(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def returnX(self):
    return self.x
  def returnY(self):
    return self.y

class Vehicle(object):
  def __init__(self, 
