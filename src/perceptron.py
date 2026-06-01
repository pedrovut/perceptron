import numpy as np

class Perceptron:
    def treinar(self, entradas, saidas, taxa_aprendizagem, epocas): # Cria a função treinar com os parâmetros entradas, saídas, taxa de aprendizagem e a quantidade de épocas
        self.entradas = entradas
        self.saidas = saidas
        self.taxa_aprendizagem = taxa_aprendizagem
        self.epocas = epocas

        peso1, peso2, bias = np.random.uniform(-1, 1),np.random.uniform(-1, 1), np.random.uniform(-1, 1) # Define peso1, peso2 e bias como um número aleatório entre -1 e 1 (uniformemente)

        for _ in range(epocas): # Percorre cada época
            for j in range(len(entradas)): # Para cada coluna (j) em total(entrdas)

                z = (entradas[j][0] * peso1) + (entradas[j][1] * peso2) + bias # Soma das multiplicações + bias

                prev = 1 if z >= 0 else 0 # Função de ativação (Step Function)

                erro = saidas[j][0] - prev # Cálculo do erro: erro = saída_esperada - previsão

                peso1 = peso1 + (taxa_aprendizagem * erro * entradas[j][0]) # Novo peso 1
                peso2 = peso2 + (taxa_aprendizagem * erro * entradas[j][1]) # Novo peso 2
                bias = bias + (taxa_aprendizagem * erro) # Novo peso bias

                print(z) # Exibe uma nova "soma das multiplicações" (z) no console

        return peso1, peso2, bias # Função treinar() retorna novos pesos
    
    def prever(self, pesos, entrada1, entrada2):
        z =  (entrada1 * pesos[0]) + (entrada2 * pesos[1]) + pesos[2] # Soma das multiplicações + bias (com os pesos definidos na função treinar)
        prev = 1 if z >= 0 else 0 # Função de ativação definitiva

        return prev # Função prever() retorna o resultado da Step Function