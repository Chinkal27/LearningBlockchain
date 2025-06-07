import random
from collections import Counter

# Simulate Proof of Work (PoW)
# Each miner has a random computational power between 1 and 250
miners = {
    "MinerA": random.randint(1, 250),
    "MinerB": random.randint(1, 250),
    "MinerC": random.randint(1, 250)
}

# Select the miner with the highest power
pow_winner = max(miners, key=miners.get)

print("\n[Proof of Work Simulation]")
print(f"Miners and their power: {miners}")
print(f"Selected Validator: {pow_winner} with power {miners[pow_winner]}")
print("Explanation: The miner with the highest computational power is chosen to add the next block.\n")

# Simulate Proof of Stake (PoS)
# Each staker has a random token stake
stakers = {
    "StakerX": random.randint(1, 100),
    "StakerY": random.randint(1, 120),
    "StakerZ": random.randint(1, 100)
}

# Select the staker with the highest stake
pos_winner = max(stakers, key=stakers.get)

print("[Proof of Stake Simulation]")
print(f"Stakers and their stake: {stakers}")
print(f"Selected Validator: {pos_winner} with stake {stakers[pos_winner]}")
print("Explanation: The staker who has staked the most tokens is given the right to validate the block.\n")

# Simulate Delegated Proof of Stake (DPoS)
# Delegates are pre-defined
delegates = ["Delegate1", "Delegate2", "Delegate3"]

# 3 voters randomly vote for one of the delegates
voters = {
    "Voter1": random.choice(delegates),
    "Voter2": random.choice(delegates),
    "Voter3": random.choice(delegates)
}

# Count the votes for each delegate
vote_counts = Counter(voters.values())
# Get the delegate with the most votes
dpos_winner = vote_counts.most_common(1)[0][0]

print("[Delegated Proof of Stake Simulation]")
print(f"Voters and their votes: {voters}")
print(f"Vote tally: {dict(vote_counts)}")
print(f"Selected Delegate: {dpos_winner}")
print("Explanation: In DPoS, voters elect a trusted delegate to validate the next block on their behalf.\n")
