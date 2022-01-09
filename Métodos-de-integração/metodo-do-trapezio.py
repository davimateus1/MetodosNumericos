#importacoes
import cmath

#funcao de X da atividade
def f(x):
  num = x + 1
  f = cmath.sqrt(num)
  return f

#integral metodo do trapezio
def intfx(f, a, b, n):
  x = a
  h = (b - a) / n #passo
  soma = 0 #soma do intervalo -> faremos as areas e somaremos aqui
  cont = 0 #contador de janelas

  while cont < n: #irá fazer iterações de acordo com o numero de janelas
    area = (f(x) + f(x + h)) * h / 2
    soma += area
    x += h
    cont += 1
  
  return soma

#---MAIN---
print("Resultado Integral:", intfx(f, 0, 1, 20))