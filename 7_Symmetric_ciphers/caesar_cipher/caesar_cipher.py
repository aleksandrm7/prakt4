def encrypt(text: str, key: int) -> str:
    """
    Шифрует текст обобщенным шифром Цезаря с использованием заданного ключа.

    Аргументы:
    text (str): Исходный текст для шифрования.
    key (int): Ключ сдвига.

    Возвращает:
    str: Зашифрованный текст.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            encrypted_char = shift_character(char, key)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text: str, key: int) -> str:
    """
    Дешифрует текст обобщенным шифром Цезаря с использованием заданного ключа.

    Аргументы:
    text (str): Зашифрованный текст для дешифрования.
    key (int): Ключ сдвига.

    Возвращает:
    str: Расшифрованный текст.
    """
    return encrypt(text, -key)


def shift_character(char: str, shift: int) -> str:
    """
    Сдвигает символ на заданное количество позиций в алфавите.

    Аргументы:
    char (str): Символ для сдвига.
    shift (int): Количество позиций сдвига.

    Возвращает:
    str: Сдвинутый символ.
    """
    if char.islower():
        base = ord('a')
    else:
        base = ord('A')
    shifted_char = chr((ord(char) - base + shift) % 26 + base)
    return shifted_char


def crack_cipher(text: str) -> str:
    """
    Восстанавливает текст без знания ключа обобщенного шифра Цезаря.

    Аргументы:
    text (str): Зашифрованный текст.

    Возвращает:
    str: Восстановленный текст.
    """
    common_words = ["the", "and", "of", "to", "in", "is", "you", "that", "it", "he", "was", "for", "on", "are"]
    max_score = 0
    best_key = 0

    for key in range(26):
        decrypted_text = decrypt(text, key)
        score = calculate_word_score(decrypted_text, common_words)
        if score > max_score:
            max_score = score
            best_key = key

    return decrypt(text, best_key)


def calculate_word_score(text: str, common_words: list[str]) -> int:
    """
    Вычисляет оценку на основе количества распознаваемых слов в тексте.

    Аргументы:
    text (str): Текст для анализа.
    common_words (List[str]): Список распознаваемых слов.

    Возвращает:
    int: Оценка на основе количества распознаваемых слов.
    """
    word_count = 0
    for word in text.split():
        if word.lower() in common_words:
            word_count += 1
    return word_count
