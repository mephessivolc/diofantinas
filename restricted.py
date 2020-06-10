import prime
import sys

initial_numbers=[0, 37, 89, 131, 401]

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

    def __init__(self, argv):
        if len(argv) == 1:
            argv = initial_numbers

        self.args = argv[1:] # valores recebidos tipo string

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
                    lst.append(_num) # lista de numeros inteiros

        except BaseException as error:
            raise(error)

        return lst

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
        return max(self.change_int_numbers())

    def take_numbers(self):
        """
            Retorna os numeros inseridos e verificados nas condicoes
        """
        if self.is_prime():
            return self.ordered()

        return []

    def is_prime(self):
        """
            Retorna verdadeiro se sao numeros primos ou primos entre si
        """

        resp = True
        for i in range(len(self.ordered())):
            for j in self.ordered()[i+1:]:
                if not prime.verify_prime_between_numbers(self.ordered()[i],j):
                    resp = False

        if not resp:
            return False

        return True

if __name__ == "__main__":
    arg = Restricted(sys.argv)
    print(arg.take_numbers())
