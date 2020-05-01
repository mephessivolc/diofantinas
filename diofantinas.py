import sys
import numpy as np
import aux
import pylatex

from restricted import Restricted

initial_numbers=[0, 37, 89, 131, 401]

class Diofante:

    def __init__(self, argv):
        self.in_latex = False
        if "-l" in argv:
            self.in_latex = True
            argv.remove('-l')
            self.in_pdf = False
            if "pdf" in argv:
                self.in_pdf = True
                argv.remove('pdf')

        if len(argv) == 1:
            argv = initial_numbers

        args = Restricted(argv[1:])
        self.numbers = args.take_numbers()
        self.order = len(self.numbers)

    def take_vec(self):
        """
            Cria a matriz b de valores inteiros
        """
        vec = np.array(aux.vec(self.numbers))
        return vec

    def take_matrix(self):
        """
            Cria a matriz A de valores
        """

        matrix = aux.matrix(self.take_vec(), self.order)

        return matrix

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


        if self.in_pdf:
            pdf.generate_pdf()

        pdf.generate_tex()

    def show(self):
        if self.in_latex:
            self.print_latex()

        else:
            print("n = {}\n\nb =\n{}\n\na =\n{}".format(self.order, self.take_vec(), self.take_matrix()))

if __name__ == '__main__':
    t = Diofante(sys.argv)
    t.show()
