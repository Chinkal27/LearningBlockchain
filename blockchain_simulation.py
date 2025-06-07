import hashlib
import time

# Block class
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

# Create the blockchain
blockchain = []

# Function to create a new block
def create_block(index, data, previous_hash):
    timestamp = time.time()
    return Block(index, timestamp, data, previous_hash)

# Genesis block (first block)
genesis_block = create_block(0, "Hello My Name is Chinkal", "0")
blockchain.append(genesis_block)

# Add second and third blocks
blockchain.append(create_block(1, "I like BLockChain Technology", blockchain[-1].hash))
blockchain.append(create_block(2, "Block Chain Technology is new future to be observed", blockchain[-1].hash))

# Display blocks
print("Initial Blockchain:")
for block in blockchain:
    print(f"Block {block.index} | Data: {block.data} | Hash: {block.hash[:10]}... | Prev Hash: {block.previous_hash[:10]}...")

# Simulate tampering
print("\n--- Tampering with Block 1 ---")
blockchain[1].data = "Tampered Data"
blockchain[1].hash = blockchain[1].calculate_hash()

# Check validity after tampering
print("\nBlockchain after Tampering:")
for block in blockchain:
    print(f"Block {block.index} | Data: {block.data} | Hash: {block.hash[:10]}... | Prev Hash: {block.previous_hash[:10]}...")

# Validation function
def is_chain_valid(chain):
    for i in range(1, len(chain)):
        current = chain[i]
        previous = chain[i - 1]
        if current.hash != current.calculate_hash():
            return False
        if current.previous_hash != previous.hash:
            return False
    return True

print("\nIs blockchain valid?", is_chain_valid(blockchain))
