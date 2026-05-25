from perceptron import Perceptron

inputs = [ [0,0], [1,0], [0,1], [1,1] ]
outputs = [[0], [1], [1], [1]]

percp = Perceptron()
train = percp.train(inputs, outputs, 0.01, 10000)

predc = percp.predict(train, 1, 0)
print(predc)