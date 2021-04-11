import sys
import caesarEncryption as Caesar
import vernamEncryption as Vernam
import vigenerEncryption as Vigener
import caesarDecryptor as CaesarDec

import RSA.KeyGen as RsaKeyGen
import RSA.Encryption as Rsa

import streamEncryption as Stream

russian_alphabet = 'абвгдеёжзийклмнопрстуфхчшщъыьэюя'
english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
exception_symbols = '.!?:;,_-\n\r\t '

if len(sys.argv) < 4:
    print('Error! Not enough args')
    sys.exit()

cipher_type = sys.argv[1]
input_file = sys.argv[2]
output_file = sys.argv[3]

if len(sys.argv) > 4:
    key = sys.argv[4]
else:
    key = '0'

alphabet = russian_alphabet
if len(sys.argv) > 5:
    lang = sys.argv[5]
    if lang.lower() == 'rus':
        alphabet = russian_alphabet
    elif lang.lower() == 'eng':
        alphabet = english_alphabet
    else:
        print('Error! Lang does not found!')
        sys.exit()

with open(input_file, 'r', encoding="utf-8") as f:
    message = f.read()

with open(output_file, 'w', encoding="utf-8") as f:
    if cipher_type.lower() == 'caesar':
        key = int(key)
        try:
            result = Caesar.caesar_encryption(message, key, alphabet,
                                              exception_symbols)
        except ValueError:
            print("Error! Incorrect args!")
            sys.exit()
        f.write(result)
    elif cipher_type.lower() == 'vernam':
        result = Vernam.vernam_encryption(message, key)
        f.write(result)
    elif cipher_type.lower() == 'vigener_enc':
        try:
            result = Vigener.vigener_encryption(message, key, 1,
                                                alphabet, exception_symbols)
        except ValueError:
            print("Error! Incorrect args!")
            sys.exit()
        f.write(result)
    elif cipher_type.lower() == 'vigener_dec':
        try:
            result = Vigener.vigener_encryption(message, key, -1,
                                                alphabet, exception_symbols)
        except ValueError:
            print("Error! Incorrect args!")
            sys.exit()
        f.write(result)
    elif cipher_type.lower() == 'caesar_dec':
        try:
            result = CaesarDec.caesar_decryption(message, alphabet,
                                                 exception_symbols)
        except ValueError:
            print("Error! Incorrect args!")
            sys.exit()
        for var in result:
            f.write(var + '\n\n')
    elif cipher_type.lower() == 'rsa_keygen':
        try:
            nums = message.split()
            result = RsaKeyGen.keygen_RSA(int(nums[0]), int(nums[1]))
        except IndexError:
            print("Error! Incorrect args!")
            sys.exit()

        f.write('publicKey: ' + str(result['publicKey']) + '\n' +
                'privateKey: ' + str(result['privateKey']))
    elif cipher_type.lower() == 'rsa':
        try:
            result = Rsa.RSA_encryption(message, key)
        except ValueError:
            print("Error! Incorrect args!")
            sys.exit()
        f.write(result)
    elif cipher_type.lower() == 'stream':
        try:
            result = Stream.stream_encryption(message, key)
        except ValueError:
            print("Error! Incorrect args!")
            sys.exit()
        f.write(result)
    else:
        print('Error! Cipher does not exists')
        sys.exit()
