import numpy as np

class Layer:
    def __init__(self):
        self.input = None
        self.output = None
    
    def forward(self, input):
        pass
    
    def backward(self, output_gradient, learning_rate):
        pass
    
class Dense(Layer):
    def __init__(self, input_size, output_size):
        self.weights = np.random.randn(output_size, input_size)
        self.bias = np.random.randn(output_size, 1)
        
    def forward(self, input):
        self.input = input
        return np.dot(self.weights, self.input) + self.bias
    
    def backward(self, output_gradient, learning_rate):
        weights_gradient =  np.dot(output_gradient, self.input.T)
        self.weights -= learning_rate * output_gradient
        self.bias -= np.dot(self.weights.T, output_gradient)
        return np.dot(self.weights.T, output_gradient)
    
    

        
        
    