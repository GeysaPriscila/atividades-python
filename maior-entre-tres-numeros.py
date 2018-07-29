'''
Bino recebeu de Cino três inteiros de presente e gostaria de saber qual dos dois inteiros é o maior.

'''

A = int(input())
B = int(input())
C = int(input())

if A > B and A > C:
    print(A)
elif B > A and B > C:
    print(B)
else:
    print(C)
