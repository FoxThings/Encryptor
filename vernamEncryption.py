def vernam_encryption(message: str, key: str):
    """
    Шифрует сообщение с помощью шифра Вернама
    Шифр симметричный, а значит ключ может
    как шифровать, так и дешифровать.
    В идеале, ключ должен быть длинной в сообщение.
    :param message Сообщение
    :param key Ключ шифрования
    :return Зашифрованное сообщение
    """

    result = []
    key_length = len(key)
    index = 0
    for char in message:
        encrypted = ord(char) ^ ord(key[index % key_length])
        result.append(chr(encrypted))
        index += 1
    return ''.join(result)
