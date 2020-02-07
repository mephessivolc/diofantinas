import sys

from restricted import Restricted


def vectors(vec):
    _vec_a = []
    _vec_b = []
    for i in range(1, len(vec)):
        num = float(vec[i]) / vec[0]
        _vec_a.append(num)
        _vec_b.append(int(num))

    return (_vec_a, _vec_b)

class Diofante:

    def __init__(self, args):
        args = Restricted(args)
        self.numbers = args.take_numbers()
        self.resp = ''

    def trans_a(self):
        """
            Retorna a matriz transformacao de a (matriz de Perron em 2.3.3)
        """

        _vec_b = vector_b(self.numbers)

        print("vec_a = {}; vec_b = {}".format(_vec_a, _vec_b))
        return _trans

    def show(self):
        print(self.trans_a())


if __name__ == '__main__':
    t = Diofante(sys.argv)
    t.show()
