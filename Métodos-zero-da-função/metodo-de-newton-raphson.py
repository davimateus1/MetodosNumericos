# importação da Saída de dados
from prettytable import PrettyTable
from prettytable import from_csv
from prettytable import from_html

# importação da biblioteca math
import math

# Cria a tabela
table = PrettyTable(["Iteração", "x", "f(x)"])

# x * e^0,5*x + 1,2 * x - 5 (função da questão)
def f(x):
  f = (x * math.e ** (0.5 * x)) + (1.2 * x) - 5
  return f

# Função que calcula a derivada
def dnf(x):
  h = 1e-8
  dnf = (f(x + h) - f(x)) / h
  return dnf

# Parâmetros que serão iterados
x = 1.25
fx = 0
i = 0
tol = 1e-6

while (abs(f(x)) > tol and i < 10): # Para loop com f(x) < 0,000001 ou 10 iterações

  # Motor gerador
  x = x - (f(x) / dnf(x))

  # chamando a função
  fx = f(x)

  # adiciona resultado à tabela
  table.add_row([(i + 1), x, fx])

  # adiciona mais 1 ao contador da iteração
  i += 1

# Exibe a tabela
print(table)