import numpy as np
import random
import os

learning_rate = 1
bias = 1
# Need three weights for two neurons and one bias
weights = [random.random() for i in range(3)]

def Perceptron(input1, input2, output):
	outputP = input1*weights[0] + input2*weights[1] +bias*weights[2]   
	if outputP > 0: # activation function
		outputP = 1
	else:
		outputP = 0
	error = output - outputP
	weights[0] += error * input1 * learning_rate
	weights[1] += error * input2 * learning_rate
	weights[2] += error * bias * learning_rate

for i in range(50):
	Perceptron(1,1,1) # true or true
	Perceptron(1,0,1) # true or false
	Perceptron(0,1,1) # false or true
	Perceptron(0,0,1) # false or false 


x = int(input())
y = int(input())
outputP = x*weights[0] + y*weights[1] + bias*weights[2]
if outputP > 0:
	outputP = 1
else:
	outputP = 0
print(x, "or", y, "is :", outputP)


# Alternative activation function, sigmoid function
outputP = 1/np.exp(-outputP))

# Save weights in file for later, so need not repeat learning process with each run

	
