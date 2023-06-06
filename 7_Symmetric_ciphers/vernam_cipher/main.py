from encryption import encrypt
from decryption import decrypt
from utils import generate_key


def main():
    message = input("Введите сообщение для шифрования: ")
    key_length = len(message.encode('utf-8'))
    key = generate_key(key_length)

    encrypted_blocks = encrypt(message, key)
    decrypted_message = decrypt(encrypted_blocks, key)

    print("Зашифрованное сообщение:", encrypted_blocks)
    print("Дешифрованное сообщение:", decrypted_message)


if __name__ == '__main__':
    main()
