import numpy as np

class Perceptron:
    def __init__(self):
        pass

    def train(self, inputs, outputs, learning_rate, epochs):
        self.inputs = inputs
        self.outputs = outputs
        self.learning_rate = learning_rate
        self.epochs = epochs

        w1, w2 = np.random.uniform(-1, 1),np.random.uniform(-1, 1)

        for i in range(epochs):
            for j in range(len(inputs)):
                # baseado em https://prnt.sc/mCFqX_8X-A_o
                # https://prnt.sc/Plo3jNnYluwT

                z = (inputs[j][0] * w1) + (inputs[j][1] * w2)

                # step function
                prev = 1 if z > 0.5 else 0

                erro = outputs[j][0] - prev

                w1 = w1 + (learning_rate * erro * inputs[j][0])
                w2 = w2 + (learning_rate * erro * inputs[j][1])
        return w1, w2
    
    def predict(self, weights, x1, x2):
        return 1 if ((x1 * weights[0]) + (x2 * weights[1])) > 0.5 else 0