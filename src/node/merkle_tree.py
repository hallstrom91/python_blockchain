import hashlib
import json


class MerkleTree:
    def __init__(self, transactions):
        self.transactions = transactions
        self.tree = self.build_merkle_tree()

    def build_merkle_tree(self):
        if not self.transactions or len(self.transactions) < 2:
            return None

        tree = [
            hashlib.sha256(json.dumps(data).encode()).hexdigest()
            for data in self.transactions
        ]

        while len(tree) > 1:
            tree = [
                hashlib.sha256((tree[i] + tree[i + 1]).encode()).hexdigest()
                for i in range(0, len(tree), 2)
            ]

        return tree[0]

    @classmethod
    def get_root(cls, merkle_tree):
        return merkle_tree


# Ex of use
transactions = ["Tx1", "Tx2", "Tx3", "Tx4"]
merkle_tree = MerkleTree(transactions)
root_hash = MerkleTree.get_root(merkle_tree)

print("Merkle Root Hash:", root_hash)
