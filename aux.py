"""
    Funcoes auxiliares para o calculo das equacoes diofantinas
"""
import numpy as np

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

    return np.array(vec)

def matrix(b, n=4):
    """
        Retorna o calculo da matriz A
        A_i^(v+n) = A_i^(v) + Sum_(j=1)^(n-1) [b_j^(v)*A_i^(v+j)]
        order = n (do trabalho escrito)

        valores de entrada:
        b = matriz b de valores
        n = ordem
    """
    lin_b = b.shape[0] # obtendo a quantidade de linhas da matriz b

    # Contruindo a matrix A[order, order + lin_b]
    m = np.eye(n, dtype=int) # bloco de matriz identidade de ordem B[order, order]
    m = np.c_[m, np.zeros((n, lin_b), dtype=int)] # adicionando um segundo bloco de matriz nula de ordem B[order, lin_b]

    for i in range(n): # linhas
        for v in range(lin_b): # colunas
            calc = m[i][v]
            for j in range(n-1): # j do trabalho
                calc = calc + b[v][j] * m[i][v+j+1]

            m[i][v+n] = calc

    print(m)
    m = np.delete(m, np.s_[0:-n], axis=1) # retirando as primeiras colunas, mantendo as n ultimas

    return m

def cofactor(A, lc =(0,0)):

    newMatrix = np.delete(A, lc[0], axis=0)
    newMatrix = np.delete(newMatrix, lc[1], axis=1)

    return newMatrix


if __name__ == "__main__":
    # initial_numbers=[37, 89, 131, 401] # para teste da funcao vec

    # para teste da funcao matrix
    # initial_numbers = np.array([[2,3,5],[4,3,4],[0,1,1],[1,2,3],[1,0,2]])
    initial_numbers = np.array([[2, 3, 10], [1, 2, 2], [0, 1, 3], [2, 0, 5]])
    print(matrix(initial_numbers, 4))
