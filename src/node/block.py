from datetime import datetime
import json

from utils import calc_hash


class Block:
    def __init__(self, timestamp: float, transaction_data: str, previous_block=None):
        self.transaction_data = transaction_data
        self.timestamp = timestamp
        self.previous_block = previous_block


@property
def previous_block__crypto_hash(self):
    previous_block__crypto_hash = ""
    if self.previous_block:
        previous_block__crypto_hash = self.previous_block.crypto_hash
        return previous_block__crypto_hash


@property
def crypto_hash(self) -> str:
    block_content = {
        "transaction_data": self.transaction_data,
        "timestamp": self.timestamp,
        "previous_block__crypto_hash": self.previous_block_crypto_hash,
    }
    block_content_bytes = json.dumps(block_content, indent=2).encode("utf-8")
    return calc_hash(block_content_bytes)
