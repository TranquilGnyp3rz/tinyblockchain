import hashlib as hasher
import datetime as date
import json
from urllib.parse import urlparse
from uuid import uuid4
import requests

class Block:
  def __init__(self, index, proof, transactions, previous_hash):
    self.index = index
    self.proof = proof
    self.timestamp = date.datetime.now()
    self.transactions = transactions
    self.previous_hash = previous_hash


class BlockChain:
    def __init__(self) -> None:
        self.chain = []
        self.transactions = []
        self.nodes = set()

    def new_block(self, proof, previous_hash):
       block = Block(len(self.chain) + 1, proof, self.transactions, previous_hash)
       self.transactions = []

       self.chain.append(block)
       return block
    

    def new_transaction(self, sender, recipient, amount):
       self.transactions.append({
          'sender': sender,
          'recipient': recipient,
          'amount': amount
       })

       return self.last_block['index'] + 1
    
    def register_new_nodes(self, url):
        paresed_url = urlparse(url)

        if paresed_url.netloc:
          self.nodes.add(paresed_url.netloc)
        else:
           raise ValueError("Invalid URL")

    def valid_chain(self, chain):

        # To check if a chain is a valid chain we need to check the previous hash of each block the proof of work 

        last_block = chain[0]
       
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]

            last_block_hash = self.hash(last_block)
            if block['previous_hash'] != last_block_hash:
                return False    

            if not self.valid_proof(last_block['proof'], block['proof'], last_block_hash):
                return False    
            last_block = block
            current_index += 1  
        return True
    

    def resolve_conflicts(self):
        pass 
    
    @property
    def last_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def hash_block(block):
       block_encoded = json.dumps(block, sort_keys=True).encode()
       return hasher.sha256(block_encoded).hexdigest()
    
    @staticmethod
    def valid_proof(last_proof, proof, last_hash):
        guess = f'{last_proof}{proof}{last_hash}'.encode()
        guess_hash = hasher.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

