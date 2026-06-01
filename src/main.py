from perceptron import Perceptron

entradas = [ [0,0], [1,0], [0,1], [1,1] ] # Array de entradas
saidas = [ [0], [0], [0], [1] ] # Array de possíveis saídas

percep = Perceptron() # Cria nova instãncia (objeto) da classe Perceptron
pesos = percep.treinar(entradas, saidas, 0.01, 100) # Usa a função treinar() e usa os arrays entradas, saídas (para entrada e saída)
                                                    #  e os valores 0.01 e 100 (para LR e épocas) como parâmetros para a variável pesos receber

print(percep.prever(pesos, 1, 1)) # Exibe no console o retorno da função prever(), com a variável pesos (para definir os pesos)
                                  # e as entradas x,x (para definir entrada1 e entrada2) como parâmetros