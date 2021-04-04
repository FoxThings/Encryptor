def vigener_encryption(message: str, key: str, side: int,
                       alphabet: str, exceptions: str):
    """
    Шифрует сообщение с помощью шифра Виженера по алфавиту.
    Если передать отрицательное значение,
    то можно производить дешифрование.
    :param message Сообщение
    :param key Ключ шифрования
    :param side 1 - шифрование, -1 - дешифрование
    :param alphabet Алфавит шиврования
    :param exceptions Символы-исключения при шифровании
    :return Зашифрованное сообщение
    :raise ValueError, если найден чужеродный символ
    """

    result = []
    key_length = len(key)
    key_index = 0
    alpha_len = len(alphabet)
    for char in message:

        # Проверка на исключения
        if exceptions.find(char) != -1:
            result.append(char)
            continue

        # Не найден элемент в алфавите
        found = alphabet.find(char.lower())
        if found == -1:
            raise ValueError

        # Не найден элемент сдвига в алфавите
        shift = alphabet.find(key[key_index % key_length].lower())
        if found == -1:
            raise ValueError

        encrypted = alphabet[(found + (shift * side)) % alpha_len]

        # Случай с большой буквой
        if char.isupper():
            encrypted = encrypted.upper()

        result.append(encrypted)
    return ''.join(result)
