import numpy as np

class ConvolutionLayer:
    def __init__(self, kernel_num, kernel_size):
        self.kernel_num = kernel_num
        self.kernel_size = kernel_size
        self.kernels = np.random.randn(kernel_num, kernel_size, kernel_size) / (kernel_size ** 2)
        
    def sliding_windows(self, image):
        image_h, image_w = image.shape
        self.image = image
        windows = []
        for h in range(image_h - self.kernel_size+1):
            for w in range(image_w - self.kernel_size + 1):
                window = image[h: (h + self.kernel_size), w : (w + self.kernel_size)]
                windows.append([window, h, w])
        return windows
    
    def forward_prop(self, image):
        image_h, image_w = image.shape
        convolution_output = np.zeros((image_h - self.kernel_size+1, image_w - self.kenel_size + 1, self.kernel_num))
        for window, h, w in self.sliding_windows(image):
            convolution_output[h, w] = np.sum(window * self.kernels, axis=(1, 2))
        return convolution_output
    
    def back_prop(self, dE_dY, alpha):
        # Tomamos la informacion que venia de al frente y la derivamos
        dE_dK = np.zeros(self.kernels.shape)
        for window, h, w in self.sliding_windows(self.image):
            for f in range(self.kernels_num):
                dE_dK[f] += window * dE_dY[h, w, f]
        self.kernels -= alpha * dE_dK
        return dE_dK

if __name__ == "__main__":
    print("HOLA :)")
    convlayer = ConvolutionLayer(3, 4)
    print(convlayer.kernels)