def caesar_encryption(message: str, offset: int,
                      alphabet: str, exceptions: str):
    """
    Шифрует сообщение с помощью шифра Цезаря по алфавиту.
    Если передать отрицательное значение,
    то можно производить дешифрование.
    :param message Сообщение
    :param offset Смещение в алфавите
    :param alphabet Алфавит шиврования
    :param exceptions Символы-исключения при шифровании
    :return Зашифрованное сообщение
    :raise ValueError, если найден чужеродный символ
    """

    result = []
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

        encrypted = alphabet[(found + offset) % alpha_len]

        # Случай с большой буквой
        if char.isupper():
            encrypted = encrypted.upper()

        result.append(encrypted)
    return ''.join(result)
