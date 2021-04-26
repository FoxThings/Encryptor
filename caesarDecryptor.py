from collections import Counter
import caesarEncryption as Caesar


def caesar_decryption(message: str, alphabet: str, exceptions: str):
    """
    Автоматическое дешифрование шифра Цезаря
    :param message Сообщение
    :param alphabet Алфавит шиврования
    :param exceptions Символы-исключения при шифровании
    :return Список возможных исходных текстов
    :raise ValueError, если найден чужеродный символ
    """

    lower_message = message.lower()
    counter = Counter(lower_message)
    most_common = counter.most_common()[0][0]
    variants = []

    for symbols in alphabet:
        shift = abs(ord(most_common) - ord(symbols))
        result = Caesar.caesar_encryption(message, shift,
                                          alphabet, exceptions)

        variants.append(result)

    return variants
