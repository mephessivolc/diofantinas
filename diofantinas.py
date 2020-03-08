import sys
import numpy as np
import auxiliar

from restricted import Restricted

class Diofante:

    def __init__(self, argv):
        args = Restricted(argv[1:])
        self.numbers = args.isrestricted()
        self.order = len(self.numbers)

    def take_vec(self):
        """
            Cria a matriz b de valores inteiros
        """
        vec = np.array(auxiliar.vec(self.numbers))
        return vec

    def take_matrix(self):
        """
            Cria a matriz A de valores
        """
        matrix = auxiliar.matrix(self.take_vec(), self.order)

        return matrix

    def show(self):
        print(self.take_matrix())

if __name__ == '__main__':
    t = Diofante(sys.argv)
    t.show()
