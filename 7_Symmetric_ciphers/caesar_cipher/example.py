# Импортируем функции из файла caesar_cipher.py
from caesar_cipher import encrypt, decrypt, crack_cipher

# Пример использования функции encrypt
plaintext = "Hello, World!"
key = 5
encrypted_text = encrypt(plaintext, key)
print("Зашифрованный текст:", encrypted_text)

# Пример использования функции decrypt
decrypted_text = decrypt(encrypted_text, key)
print("Расшифрованный текст:", decrypted_text)

# Пример использования функции crack_cipher
cracked_text = crack_cipher(encrypted_text)
print("Восстановленный текст без знания ключа:", cracked_text)
