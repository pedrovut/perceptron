from perceptron import Perceptron

inputs = [ [0,0], [1,0], [0,1], [1,1] ]
outputs = [[0], [0], [0], [1]]

percp = Perceptron()
pesos = percp.train(inputs, outputs, 0.1, 10000)

print(percp.predict(pesos, 1, 0))