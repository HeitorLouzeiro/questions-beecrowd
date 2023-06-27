'''

Neste problema, deve-se ler o código de uma peça 1, o número de peças 1,
o valor unitário de cada peça 1, o código de uma peça 2,
o número de peças 2 e o valor unitário de cada peça 2.
Após, calcule e mostre o valor a ser pago.

Entrada
O arquivo de entrada contém duas linhas de dados.
Em cada linha haverá 3 valores, respectivamente dois inteiros
e um valor com 2 casas decimais.

Saída
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo,
lembrando de deixar um espaço após os dois pontos e um espaço após o "R$".
O valor deverá ser apresentado com 2 casas após o ponto.

'''

CODE1, UNITS1, PRICE1 = input().split()
CODE1 = int(CODE1)
UNITS1 = int(UNITS1)
PRICE1 = float(PRICE1)

CODE2, UNITS2, PRICE2 = input().split()
CODE2 = int(CODE2)
UNITS2 = int(UNITS2)
PRICE2 = float(PRICE2)

TOTAL = (UNITS1 * PRICE1) + (UNITS2 * PRICE2)

print('VALOR A PAGAR: R$ {:.2f}'.format(TOTAL))
