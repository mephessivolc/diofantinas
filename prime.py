"""
    Cria lista de numeros primos e verifica se um numero é primo.
"""

def verify_prime(num):
    """
        Verifica se o numero recebido em num é primo.
    """

    for count in range(2,num):
        if num % count == 0:
            return False

        return True

def create_prime_number_list(num):
    """
        Retorna a lista de numeros primos menores que o numero recebido em num
    """
    _lst_prime = [2] # lista de primos
    n = 2

    while n < num+1:
        if verify_prime(n):
            _lst_prime.append(n)

        n = n + 1

    return _lst_prime

def verify_prime_between_numbers(num):
    """
        Verifica se os numeros recebidos em num_a e num_b sao primos entre si
    """

    if isinstance(num, list):
        _lst_prime = create_prime_number_list(max(num))
        for arg in num:
            print(num)
            if arg in _lst_prime:
                print('{} Não é numero primo'.format(arg))
                return False
    elif isinstance(num, int):
        if not verify_prime(num):
            print('Não é numero primo')
            return False

    print('É numero primo')
    return True

if __name__ == "__main__":
    n = int(input("insira um numero "))

    print(create_prime_number_list(n))
