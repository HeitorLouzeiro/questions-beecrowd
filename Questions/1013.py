'''

Faça um programa que leia três valores e apresente o maior dos três valores
lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b).
Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço
e a mensagem "eh o maior".

'''

A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
# abs retorna sempre o valor absoluto de A - B(sempre positivo)

MAIORAB = (A + B + abs(A - B)) / 2
MAIOR = (MAIORAB + C + abs(MAIORAB - C)) / 2

print('{} eh o maior'.format(int(MAIOR)))