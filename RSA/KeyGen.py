def is_prime(n: int):
    """
    Проверяет число на простоту
    :param n Проверяемое число
    :return True, если число простое, иначе False
    """
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


def keygen_RSA(p: int, q: int):
    """
    Генерирует публичный и приватный ключи
    :param p Первое простое число
    :param q Второе простое число
    :return Возвращает словарь с ключами 'publicKey' и
    'privateKey', которые отвечают за публичный и приватный
    ключи соответсвенно
    """

    # Модуль
    n = p * q

    # Функция Эйлера
    fi = (p - 1) * (q - 1)

    # Открытая экспонента
    e = 0
    for i in range(1, fi):
        if fi % i != 0 and is_prime(i):
            e = i
            break

    # Секретный ключ
    d = 0
    while True:
        if (d * e) % fi == 1:
            break
        d += 1

    return {'publicKey': [e, n],
            'privateKey': [d, n]}
