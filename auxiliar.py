
def vec(numbers): # vetor formado por numeros tipo int
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
