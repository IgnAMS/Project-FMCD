import numpy as np
from layer import Layer

class Activation(Layer):
    def __init__(self, activation, activation_prime):
        self.activation = activation
        self.activation_prime = activation_prime
        
    def forward(self, input):
        self.input = input
        return self.activation(input)
    
    def backward(self, output_gradients, learning_rate):
        return np.multiply(output_gradient, self.activation_prime(self.input))
    
class Tanh(Activation):
    def __init__(self):
        tanh = lambda x: np.tanh(x)
        tanh_prime = lambda x: 1 - np.tanh(x) ** 2
        super.__init__(tanh, tanh_prime)
        
    