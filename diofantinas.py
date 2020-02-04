#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import timeit
import numpy as np

from restricoes import Restrited

class Diofante:

    def __init__(self, numbers):
        self.numbers_not_treated = numbers
        self.numbers = Restrited(numbers[1:])
        self.time_init = timeit.default_timer()
        self.resp = ''

        self.calc()

    def __del__(self):
        time_end = timeit.default_timer()
        if "-t" in self.numbers_not_treated:
            print("Time: {}".format(time_end-self.time_init))

    def calc(self):
        """
            Calcula as matrizes para a solucao diofantina
        """

        numbers = self.numbers.int_treatment()
        self.resp += "Numeros: {}\n".format(numbers).replace('[', '').replace(']','') # Para impressão nos meios tela/arquivo
        self.resp += '\n{}\n'.format('Calculando') # Para impressão nos meios tela/arquivo
        A = np.identity(len(numbers))

        if not self.numbers.verify():
            self.resp += self.numbers.take_message() + "\n"

        b = [] # matriz utilizado
        vec_float = [] # vetor suporte

        vec_int = []
        for i in numbers[1:]:
            calc = float(i)/numbers[0]
            vec_int.append(int(calc))
            vec_float.append(calc)

        b.append(vec_int)

        qtd = len(numbers)
        for i in range(qtd):
            cont = (vec_float[0]-b[i][0])
            vec_int = []
            vec_sup = []

            for j in range(1,len(b[i])):
                valor = (vec_float[j]-b[i][j])/cont
                vec_int.append(int(valor))
                vec_sup.append(valor)

            vec_int.append(int(1/cont))
            vec_float = vec_sup
            vec_float.append(1/cont)
            b.append(vec_int)

        b = np.array(b)

        for i in range(qtd):
            for j in range(len(b[i])):
                soma = A[i][j]
                for k in range(qtd-1):
                    soma = soma + b[k][j] * A[i][(k+j) % qtd]
                    print("b[{}][{}] = {}; A[{}][{}] = {}; soma = {}".format(k,j,b[k][j],i,(k+j)%qtd,A[i][(k+j) % qtd], soma))
                A[i][j] = soma

        self.resp += 'b = \n{}\n\nmatriz A =\n{}'.format(b, A)
        

    def show(self):

        info = self.numbers_not_treated

        if "-f" in info:
            name = info[info.index('-f') + 1]

        else:
            print(self.resp)

if __name__ == "__main__":

    diofante = Diofante(sys.argv)
    diofante.show()
