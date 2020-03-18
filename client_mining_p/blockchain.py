# Paste your version of blockchain.py from the basic_block_gp
# folder here
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Create the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            "index": len(self.chain + 1),
            "proof": proof,
            "timestamp": time(),
            "transactions": self.current_transactions,
            "previous_hash": previous_hash
        }

        # Reset the current list of transactions
        self.current_transactions = []
        # Append the chain to the block
        self.chain.append(block)
        # Return the new block
        return block

    def hash(self, block):
   
        block_string = json.dumps(block, sort_keys=True)
        string_in_bytes = block_string.encode()

        hash_object = hashlib.sha256(string_in_bytes)
        hash_string = hash_object.hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]