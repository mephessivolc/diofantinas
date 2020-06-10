"""
    Funcoes auxiliares para o calculo das equacoes diofantinas
"""
from math import floor, ceil
import numpy

decimal_places = 20

def vec(numbers): # vetor formado por numeros tipo int


    vec = [] # vetor b do trabalho do Juscimar
    vec_a = [] # vetor a do trabalho do Juscimar

    tmp = [] # entradas para o vetor vec
    tmp_a = [] # entradas para o vetor vec_a

    for i in numbers[1:]:
        num = divmod(i,numbers[0])
        tmp.append(num[0])
        tmp_a.append(num[1])

    vec.append(tmp)
    vec_a.append(tmp_a)

    i=0
    while vec_a[i][0] != 0:
        tmp = [] # entradas para o vetor vec
        tmp_a = [] # entradas para o vetor vec_a
        for j in range(1,len(numbers)-1):
            calc = divmod(vec_a[i][j],vec_a[i][0])
            tmp.append(calc[0])
            tmp_a.append(calc[1])

        if i == 0:
            calc = divmod(numbers[0],vec_a[i][0])
        else:
            calc = divmod(vec_a[i-1][0],vec_a[i][0])

        tmp.append(calc[0])
        tmp_a.append(calc[1])
        vec.append(tmp)
        vec_a.append(tmp_a)
        i=i+1

    return vec
    
def matrix(matrix_b, order=4):

    """
        Calculo da Matriz A
        A_i^(v+n) = A_i^(v) + Sum_(j=1)^(n-1) (b_j^(v)A_i^(v+j))
        order = n (do trabalho escrito)
    """
    a = numpy.identity(order, dtype= int)

    for i in range(order):
        for v in range(order):
            div = (v+order) % order
            calc = 0
            for j in range(order-1):
                div1 = (v+j+1) % order
                calc = calc + matrix_b[v][j] * a[i][div1]
            a[i][div] = a[i][v] + calc

    return a

def cofactor(A,lc =(0,0)):

    newMatrix = numpy.delete(A, lc[0], axis=0)
    newMatrix = numpy.delete(newMatrix, lc[1], axis=1)

    return newMatrix


if __name__ == "__main__":
    initial_numbers=[37, 89, 131, 401]
    print(numpy.array(vec(initial_numbers)[0]))
