from typing import List
from utils import xor_bytes, split_blocks


def encrypt(message: str, key: bytes) -> List[bytes]:
    """Шифрует сообщение с использованием шифра Вернама"""
    message_bytes = message.encode('utf-8')
    encrypted_blocks = []
    for block in split_blocks(message_bytes, len(key)):
        encrypted_block = xor_bytes(block, key)
        encrypted_blocks.append(encrypted_block)
    return encrypted_blocks
