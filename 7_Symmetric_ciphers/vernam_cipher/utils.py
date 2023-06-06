import secrets
from typing import List


def generate_key(length: int) -> bytes:
    """Генерирует случайный ключ заданной длины"""
    return secrets.token_bytes(length)


def xor_bytes(message: bytes, key: bytes) -> bytes:
    """Выполняет операцию XOR между сообщением и ключом"""
    return bytes(x ^ y for x, y in zip(message, key))


def split_blocks(message: bytes, block_size: int) -> List[bytes]:
    """Разделяет сообщение на блоки заданного размера"""
    return [message[i:i+block_size] for i in range(0, len(message), block_size)]
