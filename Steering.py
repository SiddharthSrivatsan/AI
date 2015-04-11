from perceptron import Perceptron
from random import randint
import numpy as np
import matplotlib.pyplot as plt
import time
import math

plt.ion()
class PVector(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.limit = 10
  def returnX(self):
    return self.x
  def returnY(self):
    return self.y
  def add(self, vector):
    self.x += vector.returnX()
    self.y += vector.returnY()
  def setLimit(self, n):
    self.limit = n
    if(self.x > self.limit):
        self.x -= (self.x - self.limit)
    if(self.y > self.limit):
        self.y -= (self.y - self.limit)
  def normalize(self):
    if(self.x == 0 and self.y == 0):
        return 0;
    length = abs(math.sqrt(self.x**2 + self.y**2))
    self.x /= length
    self.y /= length
  def mult(self, n):
    self.x *=  n
    self.y *= n
  def sub(self, target, location):
    myX = target.returnX() - location.returnX()
    myY = target.returnY() - location.returnY()
    return PVector(myX, myY)
  def dist(self, target, location):
    xdistance = target.returnX() - location.returnX()
    ydistance = target.returnY() - location.returnY()
    return math.sqrt((xdistance)**2 + (ydistance)**2) 

class vehiclePerceptron(Perceptron):
  def feedforward(self, forcearray):
    sum = PVector(0, 0)
    #i = 0
    #while i < len(forcearray):
    forcearray[0].x += self.weights[0]
    forcearray[0].y += self.weights[1]
    sum.add(forcearray[0])
    print forcearray[0].x, forcearray[0].y
#	i+=1
    return sum
  def train(self, forcearray, vectorerror):
    learningConstant = 0.75
    #i = 0
    #while i < len(self.weights):
    self.weights[0] = learningConstant*vectorerror.returnX()
    self.weights[1] = learningConstant*vectorerror.returnY()
        #i+=1

class Vehicle(object):
  def __init__(self, n, x, y):
    self.brain = vehiclePerceptron(n)
    self.acceleration = PVector(0, 0)
    self.velocity = PVector(0, 0)
    self.location = PVector(x, y)
    self.maxspeed = 4
    self.maxforce = 0.5
  def update(self):
    self.velocity.add(self.acceleration)
    self.velocity.setLimit(self.maxspeed)
    self.location.add(self.velocity)
    self.acceleration.mult(0)
  def applyForce(self, force):
    if force.returnX() > self.maxforce:
	force = PVector(force.returnX() - (force.returnX() - self.maxforce), force.returnY())
    if force.returnY() > self.maxforce:
	force = PVector(force.returnX(), force.returnY() - (force.returnY() - self.maxforce))
    self.acceleration.add(force)
  def seek(self, target):
    vector = PVector(0, 0)
    desired = vector.sub(target, self.location)
    desired.normalize()
    desired.mult(self.maxspeed)
    steer = vector.sub(desired, self.velocity)
    steer.setLimit(self.maxspeed)
    return steer
  def steer(self, vectorarray):
    forces = []
    i = 0
    while i < len(vectorarray):
	forces.append(self.seek(vectorarray[i]))
    	i+=1
    output = self.brain.feedforward(forces)
    self.applyForce(output)
    self.update()
    for vector in vectorarray:
	desired = vector
	error = vector.sub(desired, self.location)
	self.brain.train(forces, error)
"""
vehicle = Vehicle(2, 0, 0)
plt.scatter(vehicle.location.returnX(), vehicle.location.returnY(),
	    c = 'blue', s=150)
myVectors = []
for i in range(1):
  myVectors.append(PVector(randint(-10, 10), randint(-10, 10)))

#for i in myVectors:
xpoint = myVectors[0].returnX()
ypoint = myVectors[0].returnY()
plt.scatter(xpoint, ypoint, c='red', s=100,
              label='black', edgecolors='none')

while abs(xpoint - vehicle.location.returnX()) > 0.75 or abs(ypoint - vehicle.location.returnY()) > 0.75:
  plt.draw()
  time.sleep(1)
  vehicle.steer(myVectors)
  plt.scatter(vehicle.location.returnX(), vehicle.location.returnY(),
            c = 'blue', s=150)
  print vehicle.location.returnX(), vehicle.location.returnY()
  print xpoint, ypoint

plt.scatter(vehicle.location.returnX(), vehicle.location.returnY(), c = 'green', s=150)
now = time.time()
future = now + 5
while time.time() < future:
  plt.draw()"""
