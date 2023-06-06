from typing import List
from utils import xor_bytes


def decrypt(encrypted_blocks: List[bytes], key: bytes) -> str:
    """Дешифрует зашифрованный текст с использованием шифра Вернама"""
    decrypted_blocks = []
    for block in encrypted_blocks:
        decrypted_block = xor_bytes(block, key)
        decrypted_blocks.append(decrypted_block)
    decrypted_message_bytes = b''.join(decrypted_blocks)
    decrypted_message = decrypted_message_bytes.decode('utf-8')
    return decrypted_message
