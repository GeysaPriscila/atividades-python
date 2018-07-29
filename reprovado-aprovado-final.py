'''
Bino obteve média N1 na primeira etapa do semestre e média N2 na segunda etapa do semestre.
Bino não sabe sua situação e quer sua ajuda para saber se ele está aprovado, reprovado ou de prova final.

A nota final de Bino é calculada utilizando uma média ponderada onde o peso da N1 é 2 e o peso da N2 é 3.
Caso a média final seja maior ou igual a 7, Bino está aprovado. Caso a média seja menor que 3, Bino está reprovado.
Caso Bino não esteja reprovado ou aprovado, Bino terá que fazer a prova final.

Faça um programa para ler as duas notas de Bino e imprima qual sua situação.
'''

N1 = int(input())
N2 = int(input())

mediaPonderada = (((N1*2) + (N2*3))/5)

if (mediaPonderada >= 7):
    print("Aprovado")
elif (mediaPonderada < 3):
    print("Reprovado")
else:
    print("Final")