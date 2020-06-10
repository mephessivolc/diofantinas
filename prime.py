"""
    Cria lista de numeros primos e verifica se um numero é primo.
"""
def verify_prime_between_numbers(a, b):

    try:
        _a = int(a)
        _b = int(b)

    except:
        raise BaseException

    if _a > _b:
        resp = _a % _b

    elif _a < _b:
        resp = _b % _a

    else:
        return False

    if resp == 0:
        return False

    return True

def verify_prime(num):
    """
        Verifica se o numero recebido em num é primo.
    """

    if num > 2:
        for count in range(2,num):
            if num % count == 0:
                return False

    return True

def create_prime_number_list(num):
    """
        Retorna a lista de numeros primos menores que o numero recebido em num
    """

    _lst_prime = [] # lista de primos
    n = 2
    _num = num

    try:
        if isinstance(num, list):
            _num = max(num)
        elif isinstance(num, int) or isinstance(num, float):
            _num = int(num)
        elif isinstance(num, dict):
            _num = int(max(num.values()))
    except BaseException as error:
        raise(error)

    while n < _num+1:
        if verify_prime(n):
            _lst_prime.append(n)

        n = n + 1

    return _lst_prime

if __name__ == "__main__":
    n = []
    i = 1
    resp = input("Verificar se dois numeros sao primos entre si? ")
    if resp == "sim" or resp == "s" or resp == "yes" or resp == "y":
        a = input("Primeiro Numero: ")
        b = input("Segundo Numero: ")

        if verify_prime_between_numbers(a,b):
            print("{} e {} são primos entre si".format(a,b))
        else:
            print("{} e {} não são primos entre si".format(a,b))
    else:
        print("Entao vamos criar uma lista de numeros para saber se sao primos")
        while True:
            try:
                tmp = int(input("insira o {}º numero ".format(i)))
            except:
                break
            n.append(tmp)
            i = i+1

        print('{} são os números inseridos'.format(n))
        for i in n:
            print("{} é numero primo? {}".format(i, verify_prime(i)))

        print("lista de tabela de primos menores que {}: {}".format(max(n), create_prime_number_list(max(n))))
