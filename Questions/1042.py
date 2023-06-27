'''

Leia 3 valores inteiros e ordene-os em ordem crescente.
No final, mostre os valores em ordem crescente,
uma linha em branco e em seguida,
os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.

'''

a, b, c = map(int, input().split())

OrdemCrescente = sorted([a, b, c])

print(OrdemCrescente[0])
print(OrdemCrescente[1])
print(OrdemCrescente[2])
print('\n')
print(a)
print(b)
print(c)
