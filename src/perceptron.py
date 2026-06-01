import numpy as np

class Perceptron:
    def treinar(self, entradas, saidas, taxa_aprendizagem, epocas):
        self.entradas = entradas
        self.saidas = saidas
        self.taxa_aprendizagem = taxa_aprendizagem
        self.epocas = epocas

        peso1, peso2 = np.random.uniform(-1, 1),np.random.uniform(-1, 1) # Define peso1 e peso2 como um número aleatório entre -1 e 1 (uniformemente)

        for _ in range(epocas): # Percorre cada época
            for j in range(len(entradas)): # Para cada coluna (j) em total(entrdas)

                z = (entradas[j][0] * peso1) + (entradas[j][1] * peso2) # Soma das multiplicações

                prev = 1 if z > 0.5 else 0 # Função de ativação (Step Function)

                erro = saidas[j][0] - prev # Cálculo do erro: erro = saída_esperada - previsão

                peso1 = peso1 + (taxa_aprendizagem * erro * entradas[j][0]) # Novo peso 1
                peso2 = peso2 + (taxa_aprendizagem * erro * entradas[j][1]) # Novo peso 2

                print(z) # Exibe uma nova "soma das multiplicações" (z) no console

        return peso1, peso2 # Função treinar() retorna novos pesos
    
    def prever(self, pesos, entrada1, entrada2):
        z =  (entrada1 * pesos[0]) + (entrada2 * pesos[1]) # 
        prev = 1 if z > 0.5 else 0

        return prev