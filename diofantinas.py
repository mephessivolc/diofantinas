import sys
import numpy as np
import aux

from restricted import Restricted

initial_numbers=[0, 37, 89, 131, 401]

class Diofante:

    def __init__(self, argv):
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

    def show(self):
        print("n = {}\n\nb =\n{}\n\na =\n{}".format(self.order, self.take_vec(), self.take_matrix()))

if __name__ == '__main__':
    t = Diofante(sys.argv)
    t.show()
