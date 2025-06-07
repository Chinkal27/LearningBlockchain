import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(content.encode()).hexdigest()

    def mine_block(self, difficulty):
        print(f"\nMining block {self.index} with difficulty {difficulty}...")
        start_time = time.time()
        target = "0" * difficulty

        attempts = 0
        while True:
            self.hash = self.calculate_hash()
            attempts += 1
            if self.hash.startswith(target):
                break
            self.nonce += 1

        end_time = time.time()
        print(f"Block mined! Hash: {self.hash}")
        print(f"Nonce found: {self.nonce}")
        print(f"Attempts: {attempts}")
        print(f"Time taken: {round(end_time - start_time, 4)} seconds")

# Example usage
difficulty = 6  # You can change this (e.g., 5 or 6) for more difficulty

# Create a genesis block and mine it
genesis_block = Block(0, "Genesis Block", "0")
genesis_block.mine_block(difficulty)
