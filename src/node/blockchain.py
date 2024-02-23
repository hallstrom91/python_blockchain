import hashlib
import datetime as date
import os
import json
from src.node.utils import Utils
from src.node.block import Block
from src.node.merkle_tree import MerkleTree


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    # genesis block creation
    def create_genesis_block(self):
        return Block(0, date.datetime.now(), "Genesis Block", 0)

    # control latest block
    def get_latest_block(self):
        if not self.chain:
            return None
        return self.chain[-1]

    # add new block
    def add_block(self, new_block):
        if not self.chain:
            new_block.previous_hash = 0
        else:
            new_block.previous_hash = self.get_latest_block().hash

        if new_block.previous_hash != self.get_latest_block().hash:
            print("Unvalid block. Cant add in blockchain.")
            return

        new_block.calculate_hash()
        self.chain.append(new_block)

        new_block.data["reward"] = Utils.BLOCK_REWARD

    # check if block is valid
    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def to_json(self):
        return {"chain": [block.to_json() for block in self.chain]}

    def from_json(self, json_data):
        self.chain = [
            Block().from_json(block_data) for block_data in json_data["chain"]
        ]
