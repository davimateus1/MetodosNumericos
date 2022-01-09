# importação da Saída de dados
from prettytable import PrettyTable

# importação da biblioteca math
import math

# Defina aqui seus parâmetros
a = 0
b = 2.5

# Cria a tabela
table = PrettyTable(["Iteração", "a", "b", "f(a)", "f(b)", "x", "f(x)"])

# Parâmetros que serão iterados
fx = 0
fa = 0
fb = 0
x = 0
i = 0
tol = 1e-6

# x * e^0,5*x + 1,2 * x - 5 (função da questão)
def f(x):
  f = (x * math.e ** (0.5 * x)) + (1.2 * x) - 5
  return f

while (abs(f(x)) > tol and i < 10): # Para loop com f(x) < 0,000001 ou 10 iterações

  # Motor gerador
  x = ((a * f(b)) - (b * f(a))) / (f(b) - f(a))

  # chamando a função
  fx = f(x)
  fa = f(a)
  fb = f(b)

  # adiciona resultado à tabela
  table.add_row([(i + 1), a, b, fa, fb, x, fx])

  if (fa * fx < 0): # Se f(a) * f(x) < 0
    b = x
  else: # Se f(b) * f(x) < 0
    a = x
  # adiciona mais 1 ao contador da iteração
  i += 1

# Exibe a tabela
print(table)