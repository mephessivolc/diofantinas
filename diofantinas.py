import sys

from restricted import Restricted


def vectors(vec, div=None):
    _vec_a = []
    _vec_b = []
    if not div is None:
        for i in range(1, len(vec)):
            num = float(vec[i]) / vec[0]
            _vec_a.append(num)
            _vec_b.append(int(num))

    else:
        for i in range(1, len(vec)):
            num = float(vec[i]) / vec[0]
            _vec_a.append(num)
            _vec_b.append(int(num))

    return (_vec_a, _vec_b)

class Diofante:

    def __init__(self, argv):
        args = Restricted(argv)
        self.numbers = args.take_numbers()
        self.resp = ''

    def trans_a(self):
        """
            Retorna a matriz transformacao de a (matriz de Perron em 2.3.3)
        """

        _vec_a = vectors(self.numbers)[0]
        _vec_b = vectors(self.numbers)[1]

        print("vec_a = {}; vec_b = {}".format(_vec_a, _vec_b))
        for i in range(1,len(self.numbers)):
            div = 1/(_vec_a[i-1][0]-_vec_b[i-1][0])
            aux = []
            for j in range(_vec_b[i]):
                aux.append(j/div)

            _vec_a.append(vectors(aux)[0])
            _vec_b.append(vectors(aux)[1])

        print(_vec_b)
        return _vec_b

    def show(self):
        # print(self.trans_a())
        print(self.numbers)


if __name__ == '__main__':
    t = Diofante(sys.argv)
    t.show()
