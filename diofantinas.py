import sys
import math
import numpy as np
import aux
import pylatex

from restricted import Restricted

initial_first_numbers=[0, 37, 89, 131, 401]
initial_second_numbers=[0, 53, 117, 209, 300]


"""
    sequencia para os novos calculos

    aux = lista.pop(0) -> exclui o primeiro elemento
    lista.append(aux) -> inserir o elemento

"""
class Diofante:

    def __init__(self, argv):
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

        self.with_tmp = False
        if '-t' in argv:
            self.with_tmp = True
            argv.remove("-t")

        if len(argv) == 1:
            argv = initial_numbers

        args = Restricted(argv)
        self.numbers = args.take_numbers()
        self.order = len(self.numbers)

    def take_vec(self):
        """
            Cria a matriz b de valores inteiros
        """
        vec = np.array(aux.vec(self.numbers))#, self.with_tmp))

        return vec

    def take_matrix(self):
        """
            Cria a matriz A de valores
        """
        matrix = aux.matrix(self.take_vec(), self.order)

        return matrix

    def det_matrix(self):
        return np.linalg.det(self.take_matrix())

    def cofactor_matrix(self):
        resp = []
        for i in range(self.order):
            _matrix = aux.cofactor(self.take_matrix(), (i,self.order-1))
            _resp = math.pow(-1,12) * np.linalg.det(_matrix) * math.pow(-1, i*(self.order-1))

            resp.append(int(round(_resp)))

        return resp

    def print_latex(self):
        pdf = pylatex.Document("default")

        with pdf.create(pylatex.Section("Equações Diofantinas")) as section:
            section.append("Equação:")
            ultimo = self.numbers[-1]
            eq = []
            cont = 1
            for i in self.numbers:
                simbolo = "+"
                if i == ultimo:
                    simbolo = "= 1"
                eq.append(pylatex.NoEscape(" {}x_{} {}".format(i,cont, simbolo)))
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
                # section.append(pylatex.LineBreak())
                section.append(resp)

        if self.create_pdf:
            pdf.generate_pdf()

        pdf.generate_tex()

    def show(self):

        if self.in_latex:
            self.print_latex()

        else:
            resp = "numeros = {}\n".format(self.numbers)
            resp = resp + "n = {}\n".format(self.order)

            resp = resp + "\nb =\n{}\n\nA =\n{}\n".format(self.take_vec(), self.take_matrix())
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

if __name__ == '__main__':
    t = Diofante(sys.argv)
    t.show()
