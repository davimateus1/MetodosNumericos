#importacoes
import cmath

#funcao de X da atividade
def f(x):
  num = x + 1
  f = cmath.sqrt(num)
  return f

#integral metodo de simpson
def intfx(f, a, b, n, h=1e-4):
  h = (b - a) / n #passo
  soma_impar = 0
  soma_par = 0

  for k in range(1, n, 2): #soma os impares
    soma_impar += f(a + k * h)
  for k in range(2, n, 2): #soma os pares
    soma_par += f(a + k * h)

  return (h / 3) * (f(a) + 4 * soma_impar + 2 * soma_par + f(b))

#---MAIN---
print("Resultado Integral:", intfx(f, 0, 1, 20))