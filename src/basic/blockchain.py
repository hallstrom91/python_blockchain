import hashlib
import datetime as date
import os


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.calculate_hash()

    def calculate_hash(self):
        hash_string = (
            str(self.index)
            + str(self.timestamp)
            + str(self.data)
            + str(self.previous_hash)
        )
        self.hash = hashlib.sha256(hash_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, date.datetime.now(), "Genesis Block", 0)

    def get_latest_block(self):
        if not self.chain:
            return None
        return self.chain[-1]

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

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True


blockchain = Blockchain()

genesis_block = blockchain.create_genesis_block()
blockchain.add_block(genesis_block)

# Create the first 4 blocks.
for i in range(1, 501):
    new_block_data = f"Transaction {i}"
    new_block = Block(i, date.datetime.now(), new_block_data, "")
    blockchain.add_block(new_block)

output_file_path = os.path.abspath("blockchain_output.txt")

# Show output in terminal
with open(output_file_path, "w") as file:
    # print to file
    for block in blockchain.chain:
        file.write(f"Block # {block.index}\n")
        file.write(f"Timestamp: {block.timestamp}\n")
        file.write(f"Data: {block.data}\n")
        file.write(f"Hash: {block.hash}\n")
        file.write(f"Previous Hash: {block.previous_hash}\n\n")


print(f"Blockchain is valid: {blockchain.is_valid()}")
print(f"Output written to: {output_file_path}")

print("Thank you for participating in the struggel of mining.")
input("Press Enter to Exit.")
