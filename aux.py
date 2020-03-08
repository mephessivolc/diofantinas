"""
    Funcoes auxiliares para o calculo das equacoes diofantinas
"""
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
            tmp.append(int(calc))

        tmp_a.append(1*div)
        tmp.append(int(1*div))
        vec_a.append(tmp_a)
        vec.append(tmp)

    # return (vec, vec_a,1/(vec_a[0][0]-vec[0][0])*(vec_a[0][1]-vec[0][1]))
    return vec

def matrix(matrix_b, order=4):

    """
        Calculo da Matriz A
        A_i^(v+n) = A_i^(v) + Sum_(j=1)^(n-1) (b_j^(v)A_i^(v+j))
    """
    m = numpy.identity(order, dtype= int)
    for v in range(order):
        for i in range(order):
            calc = 0
            for j in range(1, order - 1):
                calc = calc + matrix_b[v][j]*m[j][i]

            m[v][i] = m[v][i]+calc

    return m
