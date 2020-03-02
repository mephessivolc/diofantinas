import prime
import sys

class Restricted:

    """
        Verifica as restricoes necessarias para a equacao de Diofante
        que sao:
        a) c_i : são numeros naturais, para i = 1, ... , n
        b) 1 < c_1 < c_2 < ... < c_n
        c) c_i, c_j sao primos entre si, para todo 1<= i,j <= n
        d) c_i nao divide c_j para i,j > 1 e i+j < n
        e)
    """

    def __init__(self, args):
        self.args = args # valores recebidos tipo string
        self.numbers = self.take_numbers()

    def change_int_numbers(self):
        """
            Modifica os valores recebidos para tipo inteiro, exceto o primeiro
            valor. Referente a restricao item a)
        """
        try:
            lst = []
            for num in self.args:
                _num = int(num)
                if _num > 0:
                    lst.append(int(num)) # lista de numeros inteiros

            return lst

        except BaseException as error:
            raise(error)

    def ordered(self):
        """
            Retora a lista de numeros em ordem crescente, referente a restricao
            item b)
        """
        return sorted(self.change_int_numbers())


    def max_number(self):
        """
            Retorna o maior valor inserido na lista de numeros
        """
        return max(self.numbers)

    def take_numbers(self):
        """
            Retorna os numeros inseridos e verificados nas condicoes
        """
        return self.ordered()

    def isrestricted(self):

        """
            Retorn os numeros confirmados pela restricao

        """
        _tmp = prime.create_prime_number_list(self.take_numbers())
        for i in self.take_numbers():
            if i not in _tmp:
                return None

        return self.ordered()

if __name__ == "__main__":
    arg = Restricted(sys.argv[1:])
    print(arg.isrestricted())
