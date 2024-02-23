import json
import datetime as date
import os
from src.node.blockchain import Blockchain
from src.node.block import Block
from src.node.utils import Utils
from src.node.merkle_tree import MerkleTree


# Update blockchain
blockchain = Blockchain()

# Genesis Block
genesis_block = blockchain.create_genesis_block()
blockchain.add_block(genesis_block)

# Create the first blocks
for i in range(1, 5):
    new_block_data = f"Transaction {i}"
    transactions = [f"Transactions {j}" for j in range(i * 10, i * 10 + 10)]
    merkle_tree = MerkleTree(transactions)
    new_block = Block(i, date.datetime.now(), merkle_tree, "")
    blockchain.add_block(new_block)

output_file_path = os.path.abspath("blockchain_build.txt")

# Create output to file
with open(output_file_path, "w") as file:
    # print to file
    block_data_list = []

    for block in blockchain.chain:
        block_data = {
            "Block #": block.index,
            "Timestamp ": str(block.timestamp),
            "Merkle Root": block.data,
            "Hash": block.hash,
            "Previous Hash": block.previous_hash,
        }
        block_data_list.append(block_data)

    json.dump(block_data_list, file, indent=2)

    for block_data in block_data_list:
        for key, value in block_data.items():
            print(f"{key}: {value}")
        print("\n")


print(f"Blockchain is valid: {blockchain.is_valid()}")
print(f"Output written to: {output_file_path}")

print("Thank you for participating in the struggel of mining.")
input("Press Enter to Exit.")
