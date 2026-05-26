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

                z = (inputs[j][0] * w1) + (inputs[j][1] * w2)

                ## função sigmoid: https://prnt.sc/mmf9Tp_kJK_e
                sigmoid = 1 / (1 + np.exp(-z))

                erro = outputs[j][0] - sigmoid

                novo_w1 = w1 + (learning_rate * erro * inputs[j][0])
                novo_w2 = w2 + (learning_rate * erro * inputs[j][1])
        return novo_w1, novo_w2
    
    def predict(self, weights, x1, x2):
        return 1 if 1 / (1 + np.exp(-((x1 * weights[0]) + (x2 * weights[1])))) > 0.5 else 0
