"""
    Cria uma lista de numeros primos e verifica se um numero é primo.
"""

def verify_prime(num):
    """
        Verifica se o numero recebido em num é primo
    """
    for count in range(2,num):
        if num % count == 0:
            return False

    return True

def verify_prime_between_numbers(num_a, num_b):
    """
        Verifica se os numeros recebidos em num_a e num_b sao primos entre si
    """

    _lst_num = sorted([int(num_a), int(num_b)]) # lista crescente de numeros recebidos

    if _lst_num[1] % _lst_num[0]:
        return False

    return True

def create_prime_number_list(num):
    """
        Retorna a lista de numeros primos menores que o numero recebido em num
    """
    _lst_prime = [] # lista de primos
    n = 2
    while n < num+1:
        if verify_prime(n):
            _lst_prime.append(n)

        n = n + 1

    return _lst_prime
