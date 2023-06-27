'''

Leia 3 valores de ponto flutuante
e efetue o cálculo das raízes da equação de Bhaskara.
Se não for possível calcular as raízes,
mostre a mensagem correspondente “Impossivel calcular”,
caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes,
apresente a mensagem "Impossivel calcular". Caso contrário,
imprima o resultado das raízes com 5 dígitos após o ponto,
com uma mensagem correspondente conforme exemplo abaixo.
Imprima sempre o final de linha após cada mensagem.

'''

A, B, C = map(float, input().split())

# Formaula de bascara
# x = (-b ± √(b² – 4ac)) / (2a)

# A = 0, não é uma equação de segundo grau
# B² - 4AC < 0, não existe raiz quadrada de número negativo

if A == 0 or (B ** 2 - 4 * A * C) < 0:
    print('Impossivel calcular')
else:
    R1 = (-B + (B ** 2 - 4 * A * C) ** (1 / 2)) / (2 * A)
    R2 = (-B - (B ** 2 - 4 * A * C) ** (1 / 2)) / (2 * A)
    print('R1 = {:.5f}'.format(R1))
    print('R2 = {:.5f}'.format(R2))

