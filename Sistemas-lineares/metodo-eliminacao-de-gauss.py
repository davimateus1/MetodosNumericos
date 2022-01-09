# =========================================================
# Importações

import numpy as np

# =========================================================
# Definindo o sistema

# A matriz "a" representa todos os elementos que vem antes da igualdade (=)
a = np.array([[10.0,2.0,1.0,1.0,-1.0],
              [1.0,5.0,-1.0,2.0,3.0],
              [2.0,1.0,7.0,1.0,1.0],
              [1.0,2.0,3.0,10.0,1.0],
              [1.0,1.0,1.0,-1.0,2.0]])

# A matriz "b" representa todos os elementos que vem após a igualdade (=)
b = np.array([1.0,5.0,8.0,-4.0,5.0])

# =========================================================
# Exibição da matriz e vetor

# Função responsável por exibir a matriz A
def imprime_matriz(matriz):

    linhas = len(matriz)
    colunas = len(matriz[0])

    for i in range(linhas):
        for j in range(colunas):
            if(j == colunas - 1):
                print("%.2f" %matriz[i][j])
            else:
                print("%.2f" %matriz[i][j], end = "  ")
    print()
    
# Função responsável por exibir o vetor B
def imprime_vetor(vetor):

    for v in vetor:
      print("%.2f" %v, end = "  ")

    print()

# =========================================================
# Triangulação do sistema

def triangular_solver(a,b):
  n = np.size(b) #tamanho do vetor B
  x = np.zeros(n) #Pegando os zeros obtidos em n
  x[-1] = b[-1]/a[-1,-1]

  for i in reversed(range(n-1)): # Etapas
    s = 0
    for j in range(i+1,n):
      s += a[i,j]*x[j]
      x[i] = (b[i]-s)/a[i,i]

  return x
  

def triangular_superior(a,b):
  print("===========================================")
  n = np.size(b) #tamanho do vetor B
  for e in range(n-1): #Etapas

  # "i" representa a iteração atual
  # ":" representa o número total de colunas
  # "m" é o multiplicador
  # "e" é um "Pivô" para indentificarmos as posições das linhas e colunas da nossa matriz, ex: [0,0], [1,1]...

    for i in range(e+1,n):
      m = a[i,e]/a[e,e]             # Pega a linha "i" e a coluna "e" para efetuar o calculo de remoção
      a[i,:] = a[i,:] - m*a[e,:]    # A cada etapa rodada no for, essa linha de código elimina uma linha
      b[i] = b[i] - m*b[e]          # Basicamente tudo que acontece com  a, acontece com b, então é a mesma ideia da linha acima

      print("A:")
      imprime_matriz(a)             # Imprimindo o resultado da matriz a
      print("-------------------------------------------")
      print("B:")
      imprime_vetor(b)              # Imprimindo o resultado da matriz b
      print("-------------------------------------------")
      print("M:")
      print(m)                      # Imprimindo o resultado da matriz m
      print("===========================================")

# Função de Gauss
def gauss_eliminacao(a,b):
  triangular_superior(a,b)
  x = triangular_solver(a,b)

  return x

# =========================================================
# Main - Parte inicial do programa

# Chama a função de Gauss
result = gauss_eliminacao(a,b)

# Exibe solução do sistema
print("Solução do sistema:")
cont = 1
for x in result:
  print("X", cont, ": %.2f" %x)
  cont += 1