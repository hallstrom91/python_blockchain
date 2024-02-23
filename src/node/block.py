import hashlib
import datetime as date
import json
from src.node.utils import Utils
from src.node.merkle_tree import MerkleTree


class Block:
    def __init__(
        self,
        index,
        timestamp,
        data,
        previous_hash,
        miner_reward_adress=None,
        merkle_tree=None,
    ):
        self.index = index
        self.timestamp = timestamp
        self.data = {"data": data}
        self.previous_hash = previous_hash
        self.miner_reward_adress = miner_reward_adress
        self.merkle_tree = merkle_tree
        self.calculate_hash()

    def calculate_hash(self):
        hash_string = (
            str(self.index)
            + str(self.timestamp)
            + str(self.data)
            + str(self.previous_hash)
        )
        self.hash = hashlib.sha256(hash_string.encode()).hexdigest()

    def build_merkle_tree(self, transactions):
        self.merkle_tree = MerkleTree(transactions)

    def get_merkle_root(self):
        return MerkleTree.get_root(self.merkle_tree)

    def to_json(self):
        return {
            "index": self.index,
            "timestamp": str(self.timestamp),
            "data": self.data,
            "previous_hash": self.previous_hash,
            "miner_reward_adress": self.miner_reward_adress,
            "hash": self.hash,
            "merkle_tree_root": self.get_merkle_root(),
        }

    def from_json(self, json_data):
        self.index = json_data["index"]
        self.timestamp = date.datetime.strptime(
            json_data["timestamp"], "%Y-%m-%d %H:%M:%S:%f"
        )
        self.data = json_data["data"]
        self.previous_hash = json_data["previous_hash"]
        self.miner_reward_adress = json_data["miner_reward_adress"]
        self.hash = json_data["hash"]

        transactions = json_data["data"]["data"] if "data" in json_data["data"] else []
        self.merkle_tree = MerkleTree(transactions)

        return self
