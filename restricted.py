import prime

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
            for num in self.args[1:]:
                _num = int(num)
                if _num > 0:
                    lst.append(int(num)) # lista de numeros inteiros

            return lst

        except BaseException as error:
            raise(error)

    def order(self):
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

    def verify_prime_between_numbers(self):
        """
            Verifica se todos os numeros da lista sao primos entre si, referente
            a restricao item c)
        """
        _lst_num = self.order() # lista de numeros inseridos
        _qty_lst_num = len(self.order()) # quantidade de numeros inseridos

        for i in range(_qty_lst_num-1):
            for j in range(i+1, _qty_lst_num):
                if prime.verify_prime_between_numbers(_lst_num[i], _lst_num[j]):
                    return False

        return True

    def is_conditioned(self):
        """
            Verifica se a lista inserida esta nas condicoes exigidas
        """
        if not self.verify_prime_between_numbers():
            print("Nao esta condicionado")
            return False

        return True

    def take_numbers(self):
        """
            Retorna os numeros inseridos e verificados nas condicoes
        """
        if not self.is_conditioned():
            return

        return self.order()
