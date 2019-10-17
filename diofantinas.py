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
        self.header = ''
        self.footer = ''

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
        self.resp += "Numeros: {}\n".format(numbers).replace('[', '').replace(']','')
        self.resp += '\n{}\n'.format('Calculando')

        if not self.numbers.verify():
            self.resp += self.numbers.take_message() + "\n"
        else:
            self.resp += "\n{}\n".format('Sem nada para Calcular ainda' )


        matrix = []
        comp=True
        vec = numbers
        for j in numbers:
            vec = vector(vec, comp=comp)
            matrix.append(vec)
            comp = False

        print(matrix)

        # numpy: np.transpose() - transpor uma matriz

    def create_file(self):

        info = self.numbers_not_treated

        if "-f" in info:
            name = info[info.index('-f') + 1]
            if '.tex' in name:
                self.header = create_header_tex()


                self.footer = "\end{document}"

            file_name = name

            with open(name, 'w') as file_open:
                file_open.write(self.header)
                file_open.write(self.resp)
                file_open.write(self.footer)

        else:
            print(self.resp)

def create_header_tex():
    msg = r"\documentclass[a4,12pt]{article}"+"\n"
    msg += r"\usepackage[brazil]{babel}"+"\n"
    msg += r"\usepackage{amssymb}"+"\n"
    msg += r"\usepackage[utf8]{inputenc}"+"\n"
    msg += r"\begin{document}"+"\n"

    return msg

def vector(a, comp=False):
    print(a)
    vector = []
    length = len(a[1:])
    for i in range(length):
        if not comp and i != length:
            vector.append(int(i/a[0]))
        else:
            vector.append(1)

    return vector


if __name__ == "__main__":


    diofante = Diofante(sys.argv)
    diofante.create_file()
