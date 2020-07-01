import sys
import math
import time
import numpy as np
import auxiliar as aux
import pylatex

from restricted import Restricted

initial_first_numbers = [0, 37, 89, 131, 401]
initial_second_numbers = [0, 53, 117, 209, 300]

"""
    sequencia para os novos calculos

    aux = lista.pop(0) -> exclui o primeiro elemento
    lista.append(aux) -> inserir o elemento

"""


class Diofante:

    def __init__(self, argv):
        """
            Inicializacao:
            argv = numeros a serem trabalhados
            como parametro recebe uma quantidade de numeros inteiros, gerando uma lista a ser trabalhada,
            e caso nao receba nenhuma sequencia de numeros interios, a
            inicializacao da classe sera feita automaticamente com a sequencia de numeros 0, 37, 89, 131, 401

            comandos anexados:
            -s = utiliza automaticamente a sequencia de numeros 0, 53, 117, 209, 300
            -l = apresenta os dados finais em um arquivo .tex
            pdf = cria o arquivo .pdf gerado pelo arquivo .tex
        """

        self.in_latex = False
        if "-l" in argv:
            self.in_latex = True
            argv.remove('-l')
            self.create_pdf = False
            if "pdf" in argv:
                self.create_pdf = True
                argv.remove('pdf')

        initial_numbers = initial_first_numbers
        if '-s' in argv:
            initial_numbers = initial_second_numbers
            argv.remove('-s')

        self.with_time = False
        if '-t' in argv:
            self.initial_time = time.time()
            self.with_time = True
            argv.remove("-t")

        if len(argv) == 1:
            argv = initial_numbers

        args = Restricted(argv)
        self.numbers = args.take_numbers()
        self.order = len(self.numbers)

    def take_vec(self):
        """
            Cria e retorna a matriz b de valores inteiros
        """
        vec = aux.vec(self.numbers)

        return vec

    def take_matrix(self):
        """
            Cria e retorna a matriz A de valores
        """
        matrix = aux.matrix(self.take_vec(), self.order)

        return matrix

    def det_matrix(self):
        """
            Retorna o determinante da matriz self.take_matrix()
        """
        return np.linalg.det(self.take_matrix())

    def cofactor_matrix(self):
        """
            Retorna a matriz cofatora
        """
        resp = []
        for i in range(self.order):
            _matrix = aux.cofactor(self.take_matrix(), (i, self.order - 1))
            _resp = math.pow(-1, 12) * np.linalg.det(_matrix) * math.pow(-1, i * (self.order - 1))

            resp.append(int(round(_resp)))

        return resp

    def print_latex(self):
        """
            Gerador de arquivos .tex e .pdf
        """

        pdf = pylatex.Document(
            "default"
        )

        with pdf.create(pylatex.Section(
                "Equações Diofantinas"
        )) as section:

            section.append("Equação:")
            ultimo = self.numbers[-1]
            eq = []
            cont = 1
            for i in self.numbers:
                simbolo = "+"
                if i == ultimo:
                    simbolo = "= 1"
                eq.append(
                    pylatex.NoEscape(
                        " {}x_{} {}".format(i, cont, simbolo)
                    )
                )
                cont = cont + 1

            section.append(pylatex.Math(data=eq))

            text = "n = {}".format(self.order)
            section.append(text)

            m = pylatex.Matrix(self.take_vec(), mtype='b')
            matrix = pylatex.Math(data=['b = ', m])
            section.append(matrix)

            m = pylatex.Matrix(self.take_matrix(), mtype='b')
            matrix = pylatex.Math(data=['A = ', m])
            section.append(matrix)

            section.append("Resposta = {}".format(self.cofactor_matrix()))

            section.append(pylatex.LineBreak())
            section.append("Confirmando:")
            section.append(pylatex.LineBreak())
            s = 0
            for i in range(len(self.numbers)):
                r = self.numbers[i] * self.cofactor_matrix()[i]
                s = s + r
                resp = "\t {}\t{} \t* \t{} \t= \t{} \t({})\n".format(
                    i,
                    self.numbers[i],
                    self.cofactor_matrix()[i],
                    r,
                    s
                )
                section.append(resp)

        if self.create_pdf:
            pdf.generate_pdf()

        pdf.generate_tex()

    def show(self):
        '''
            Apresenta os resultados, exibindo-os na tela ou em arquivo .tex
        '''

        if self.in_latex:
            self.print_latex()

        else:
            resp = "numeros = {}\n".format(self.numbers)
            resp = resp + "n = {}\n".format(self.order)

            resp = resp + "\nb =\n{}\n\nA =\n{}\n".format(
                self.take_vec(),
                self.take_matrix(),
            )
            resp = resp + "Resposta =\n{} \n".format(self.cofactor_matrix())
            resp = resp + "Confirmando: \n"
            s = 0
            for i in range(len(self.numbers)):
                r = self.numbers[i] * self.cofactor_matrix()[i]
                s = s + r
                resp = resp + "{} * {} = {} ({})\n".format(
                    self.numbers[i],
                    self.cofactor_matrix()[i],
                    r,
                    s
                )

            print(resp)

        if self.with_time:
            print("Tempo de execucao: {}".format(time.time() - self.initial_time))

if __name__ == '__main__':
    t = Diofante(sys.argv)
    t.show()
