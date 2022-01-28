import hashlib
NONCE_LIMIT = 10000000000
zeros = 8
def mine(block_number, transactions, previous_hash):
    for nonce in range(NONCE_LIMIT):
        base_text=str(block_number) + transactions + previous_hash + str(nonce)
        hash_try=hashlib.sha256(base_text.encode()).hexdigest()
        if hash_try.startswith('0'*zeros):
            print(f"Found Hash with Nonce:{nonce}")
            return hash_try
    return -1


block_number = 25
transactions = "763ffjke2414"
previous_hash = "842dhlbw3579"

combined_text = str(block_number) + transactions + previous_hash + str(125916)
print(hashlib.sha256(combined_text.encode()).hexdigest())
mine(block_number, transactions, previous_hash)



