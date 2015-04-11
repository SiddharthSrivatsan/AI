from random import randint
import numpy as np
import matplotlib.pyplot as plt
class Perceptron(object):
	def __init__(self, n):
		self.n = n
		i = 0
		self.weights = [0]*n
		while i < len(self.weights):
			self.weights[i] = randint(-1, 1)
			i+=1
	def __repr__(self):
		return str(self.weights)
	def setInputs(self, inputs):
		self.inputs = inputs
	def feedforward(self):
		sum = 0.0
		i = 0
		while i < self.n:
			sum = sum + self.inputs[i]*self.weights[i]
			i+=1
		return np.sign(sum)
	def train(self, guess, desired):
        	error = desired - guess
		i = 0
		while i < len(self.weights):
			self.weights[i] += error * self.inputs[i]
			i+=1

#Uncomment following section when steering file is not used
"""
def f(x):
	return 2*x + 1

xpoint = randint(-100, 100)
ypoint = randint(-100, 100)

print  xpoint, ypoint

def trainPerceptron(perceptron, inputs):
	perceptron.setInputs(inputs)
	print perceptron
	a = 1
	if inputs[1] < f(inputs[0]):
		a = -1
	b = perceptron.feedforward() 
	print b
	perceptron.train(b, a)
	return perceptron.feedforward()	

p = Perceptron(3)
point = [xpoint, ypoint, 1]
scale = 75
print trainPerceptron(p, point)
for i in range(25):
	xpoint = randint(-10, 10)
	ypoint = randint(-10, 10)
	newPerceptron = Perceptron(3)
	point = [xpoint, ypoint, 1]
	x = trainPerceptron(newPerceptron, point)
	if(x == 1):
		plt.scatter(xpoint, ypoint, c='red', s=scale,
				label='red', edgecolors='none')
	else:
 		plt.scatter(xpoint, ypoint, c='green', s=scale,
                                label='green', edgecolors='none')

plt.grid(True)
pointx = np.linspace(-15, 15, 100)
pointy = f(pointx)
plt.plot(pointx, pointy)
plt.show()
"""
