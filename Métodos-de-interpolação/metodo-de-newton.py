# Importações
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Função que executa o método de Newton
def interpNewton(x,y,xi):
  n = len(x) # Quantidade de dados
  fdd = [[None for x in range(n)] for x in range(n)] # Criando matriz vazia

  # Preenchendo a primeira coluna da matriz com o Y
  for i in range(n):
    fdd[i][0] = y[i] 

  # Calculando a diferenca dividida e guardando o resultado na matriz
  for j in range(1,n):
    for i in range(n-j):
      fdd[i][j] = (fdd[i+1][j-1] - fdd[i][j-1])/(x[i+j]-x[i])

  xtermo = 1
  yint  = fdd[0][0]
  for ordem in range(1,n): # percorrendo com o for e realizando multiplicação e a soma
    xtermo = xtermo*(xi - x[ordem-1]) # multiplica o termo
    yint  = yint + fdd[0][ordem]*xtermo # soma a diferenca dividida
  
  return yint # retornando o resultado final

# Dados para analise
x = [2.0, 4.0, 8.0] #X
y = [0.3010, 0.6020, 0.9030] #f(x)

n  = 2 #grau

# Ponto à encontrar
xp1 = 6.0
yp1 = interpNewton(x,y,xp1)

# Dados para analise
x = [10.0, 12.0, 16.0] #X
y = [1.0000, 1.0792, 1.2041] #f(x)

# Ponto à encontrar
xp2 = 14.0
yp2 = interpNewton(x,y,xp2)

# Dados para analise
x = [16.0, 18.0, 20.0] #X
y = [1.2041, 1.2552, 1.3010] #f(x)

# Ponto à encontrar
xp3 = 22.0
yp3 = interpNewton(x,y,xp3)

# Vetor com os dados iniciais
x = [2.0, 4.0, 8.0, 10.0, 12.0, 16.0, 18.0, 20.0] #X
y = [0.3010, 0.6020, 0.9030, 1.0000, 1.0792, 1.2041, 1.2552, 1.3010] #f(x)

# Adiciona os pontos encontrados ao vetor
x.append(xp1)
x.append(xp2)
x.append(xp3)
y.append(round(yp1, 4))
y.append(round(yp2, 4))
y.append(round(yp3, 4))

# Ordena vetor em ordem crescente
x = sorted(x)
y = sorted(y)

# Cria a tabela
table = PrettyTable()

# adiciona resultado à tabela
table.add_column("x", x)
table.add_column("f(x)", y)

# Exibe a tabela completa
print(table)