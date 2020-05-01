"""
    Funcoes auxiliares para o calculo das equacoes diofantinas
"""
from math import floor, ceil
import numpy

def vec(numbers): # vetor formado por numeros tipo int
    """
        Construção do vetor transformacao (matriz b)
    """
    vec = [] # vetor b do trabalho do Juscimar
    vec_a = [] # vetor a do trabalho do Juscimar

    tmp = [] # entradas para o vetor vec
    tmp_a = [] # entradas para o vetor vec_a
    for i in numbers[1:]:
        num = i/numbers[0]
        tmp_a.append(num)
        tmp.append(int(num))

    vec_a.append(tmp_a)
    vec.append(tmp)

    for i in range(len(numbers)-1):
        tmp = []
        tmp_a = []

        div = 1/(vec_a[i][0]-vec[i][0])

        for j in range(1,len(vec[i])):
            calc = div * (vec_a[i][j]-vec[i][j])
            tmp_a.append(calc)
            # tmp.append(int(calc)) # somente o numero inteiro
            # tmp.append(round(calc)) # arredondamento para o inteiro mais proximo
            tmp.append(int(round(calc)))
            # tmp.append(floor(calc)) # arredondamento sempre para baixo
            # tmp.append(ceil(calc)) # arredondamento para cima

        tmp_a.append(div)
        # tmp.append(int(div))
        # tmp.append(round(div))
        # tmp.append(floor(div))
        # tmp.append(ceil(div))
        tmp.append(int(round(div)))

        vec_a.append(tmp_a)
        vec.append(tmp)

    return vec

def matrix(matrix_b, order=4):

    """
        Calculo da Matriz A
        A_i^(v+n) = A_i^(v) + Sum_(j=1)^(n-1) (b_j^(v)A_i^(v+j))
        order = n (do trabalho escrito)
    """
    a = numpy.identity(order, dtype= int)

    # print("n = {}\nb = \n{}\nA = \n{}".format(order, matrix_b, a))
    for i in range(order):
        for v in range(order):
            div = (v+order) % order
            # resp = "A[{}][{}] = A[{}][{}] + ".format(i, div, i, v)
            # resp1 = "A[{}][{}] = {} + ".format(i,div, a[i][div])
            calc = 0
            for j in range(order-1):
                div1 = (v+j+1) % order
                # resp = resp + "b[{}][{}]*A[{}][{}] + ".format(v, j, i, div1)
                # resp1 = resp1 + "{} * {} + ".format(matrix_b[v][j], a[i][div1])
                calc = calc + matrix_b[v][j] * a[i][div1]
            a[i][div] = a[i][v] + calc
            # print("{}".format(resp))
            # print("{}".format(resp1))

    return a
