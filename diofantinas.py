import sys
import numpy as np
import auxiliar

from restricted import Restricted

class Diofante:

    def __init__(self, argv):
        args = Restricted(argv[1:])
        self.numbers = args.isrestricted()

    def take_vec(self):
        vec = np.array(auxiliar.vec(self.numbers))
        return vec

    def show(self):
        print(self.take_vec())

if __name__ == '__main__':
    t = Diofante(sys.argv)
    t.show()
