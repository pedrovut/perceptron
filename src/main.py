from perceptron import Perceptron

entradas = [ [0,0], [1,0], [0,1], [1,1] ]
saidas = [[0], [0], [0], [1]]

percp = Perceptron()
pesos = percp.treinar(entradas, saidas, 0.01, 100)

print(percp.prever(pesos, 1, 1))