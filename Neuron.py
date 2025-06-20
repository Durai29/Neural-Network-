import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()
''' reason for using nnfs.init() method:
        1. Sets the Random Seed: It initializes NumPy's random number generator with a seed value of 0. 
        This ensures that any random numbers generated (such as weights and biases) are the same each 
        time the code is run, aiding in reproducibility.

        2. Configures Default Data Type: The function sets the default data type for NumPy arrays to float32.
           This is particularly useful in neural network computations, as it standardizes the data type across
           various operations, potentially improving performance and compatibility.

        3. Overrides NumPy's Dot Product: It replaces NumPy's default np.dot function with a version that
        ensures consistent behavior, especially concerning data types and precision. This modification helps 
        prevent subtle bugs that can arise from data type mismatches during matrix operations.'''

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.01 * np.random.randn(n_inputs,n_neurons) # 0.01 is multiplied (small num -> easy calculation)
        self.biases = np.zeros((1,n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs,self.weights) + self.biases

class Activation_RELU():
    def forward(self,inputs):
        self.output = np.maximum(0,inputs)

class Activation_Softmax():
    def forward(self,inputs):
        exp_values = np.exp(inputs - np.max(inputs,axis = 1,keepdims=True))
        self.output = exp_values / np.sum(exp_values,axis=1,keepdims=True)

X, y = spiral_data(samples=100,classes=3)
dense1 = Layer_Dense(2,3)
activation1 = Activation_RELU()
dense2 = Layer_Dense(3,3)
activation2 = Activation_Softmax()

dense1.forward(X)
activation1.forward(dense1.output)
dense2.forward(activation1.output)
activation2.forward(dense2.output)

print(activation2.output[:5])