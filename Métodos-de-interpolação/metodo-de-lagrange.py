# Importações
import numpy as np
from prettytable import PrettyTable

# Função de interpolação de Lagrange
def interpLagrange(xp,x,y,grau):
  yp = 0 #valor inicial
  for k in range(0,n+1):
    p = 1 #produto
    for j in range(0,n+1):
      if k != j:
        p = p*(xp - x[j])/(x[k] - x[j])

    yp = yp + p * y[k]

  return yp # Retornando o resultado obtido na função

n  = 2 #grau

# Dados para analise
x = [2.0, 4.0, 8.0] #X
y = [0.3010, 0.6020, 0.9030] #f(x)

# Ponto à encontrar
xp1 = 6.0
yp1 = interpLagrange(xp1,x,y,n)

# Dados para analise
x = [10.0, 12.0, 16.0] #X
y = [1.0000, 1.0792, 1.2041] #f(x)

# Ponto à encontrar
xp2 = 14.0
yp2 = interpLagrange(xp2,x,y,n)

# Dados para analise
x = [16.0, 18.0, 20.0] #X
y = [1.2041, 1.2552, 1.3010] #f(x)

# Ponto à encontrar
xp3 = 22.0
yp3 = interpLagrange(xp3,x,y,n)

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