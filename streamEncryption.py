import random


def keyGen(key: str):
    """
    Генератор бесконечного ключа по ключу
    :param key Базовый ключ
    :return Бесконечная последовательность ключа
    """

    seed = 0
    for char in key:
        seed += ord(char)

    random.seed(seed)

    while True:
        yield random.randint(0, 2000)


def stream_encryption(message: str, key: str):
    """
    Шифрует сообщение методом поточного шифрования
    :param message Сообщение
    :param key Ключ шифрования
    :return Зашифрованное сообщение
    """

    result = []
    gen = keyGen(key)

    for char in message:
        encrypted = ord(char) ^ next(gen)
        result.append(chr(encrypted))
    return ''.join(result)
