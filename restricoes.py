
class Restrited():

    """
        Verifica as necessidades:
        1 - se sao numeros naturais maiores que zero, caso contrario retira os valores negativos ou nulos ou retorna um erro
        2 - se sao primos entre si
    """

    def __init__(self, numbers):
        self.msgs = []
        self.numbers_not_treated = numbers
        self.numbers = self.int_treatment()
        self.max = max(self.numbers) # toma o maior numero

    def int_treatment(self):

        # maiores que zero
        _temp = []

        for x in self.numbers_not_treated:
            if str(x).isdigit():
                _resp = int(x)
                if _resp > 0:
                    _temp.append(_resp) # lista de todos os numeros inseridos em tipo inteiro

        return sorted(_temp, key=int) # retorna os numeros ordenados do menor para o maior

    def verify(self):
        resp = True
        obs = ''
        if (not self.is_prime_numbers() or not self.is_not_divided()):
            resp = False

        return resp

    def take_message(self):
        msg = "\n"
        for i in self.msgs:
            msg += "{}\n".format(i)
        return msg

    def create_prime_numbers_list(self):
        """
            Constroi uma lista de numeros primos menores que o maior numero inserido.
        """
        dvs = []
        lst = []
        for i in range(2, self.max+1):
            for j in range(1,i+1):
                if i>=j:
                    if i % j == 0:
                        dvs.append(j)
            if len(dvs) == 2:
                lst.append(i)

            dvs = []

        return lst

    def is_prime_numbers(self):
        """
            Verifica se na lista inserida, todos sao primos entre si.
        """

        _lst = []


        for j in self.numbers:
            _inner_lst = []
            for i in self.create_prime_numbers_list():
                if i <= j:
                    if j % i == 0:
                        _inner_lst.append(i)
                else:
                    break

            _lst.append(_inner_lst)

        resp = True
        for number in self.create_prime_numbers_list():
            cont=0
            for reg in _lst:
                cont += reg.count(number)

            if cont >= len(_lst):
                resp = False
                self.msgs.append('Os numeros na lista sao primos entre si')


        return resp

    def is_not_divided(self):

        resp = True
        i = 0
        while i < len(self.numbers):
            for j in self.numbers[i+1:]:
                if j % self.numbers[i] == 0:
                    self.msgs.append("Os Numeros {} e {} sao divisiveis entre si".format(self.numbers[i],j))
                    resp = False
            i += 1

        return resp
