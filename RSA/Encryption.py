import re


def RSA_encryption(message: str, key: str):
    """
    Шифрует сообщение с помощью RSA
    При публичном ключе - шифрование
    При секретном - дешифрование
    :param message Сообщение
    :param key Ключ
    :return Зашифрованное сообщение
    :raise ValueError, если ключ задан в неправильном формате
    """

    try:
        key = re.sub(r"[$@&() ]", "", key)
        key = tuple(map(int, key.split(',')))
    except (TypeError, ValueError):
        raise ValueError

    if len(key) < 2:
        raise ValueError

    result = []
    for char in message:
        enc = pow(ord(char), key[0], key[1])
        result.append(chr(enc))

    return ''.join(result)
