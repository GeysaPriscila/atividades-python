# LER DOIS NÚMEROS E IMPRIMIR OS VALORES INTEIROS ENTRE OS DOIS NÚMEROS LIDOS.

A = int(input())
B = int(input())

if B < A:
    A, B = B, A # A recebe o valor de B e B recebe o valor de A

for i in range(A, B+1):
    print('{} '.format(i), end='')
