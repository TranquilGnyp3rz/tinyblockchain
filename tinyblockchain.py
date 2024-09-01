import hashlib as hasher
import datetime as date

def create_genesis_block():
  return Block(0, date.datetime.now(), "In the beginning God created the heaven and the earth", "0")


def next_block(last_block):
  this_index = last_block.index + 1
  this_timestamp = date.datetime.now()
  this_data = "Hey! I'm block " + str(this_index)
  return Block(this_index, this_timestamp, this_data, last_block.hash)

class Block:
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block()
  
  def hash_block(self):
    sha = hasher.sha256()
    sha.update(str(self.index).encode() + 
               str(self.timestamp).encode() + 
               str(self.data).encode() + 
               str(self.previous_hash).encode())
    return sha.hexdigest()

blockchain = [create_genesis_block()]
previous_block = blockchain[0]

num_of_blocks_to_add = 20


for i in range(0, num_of_blocks_to_add):
  block_to_add = next_block(previous_block)
  blockchain.append(block_to_add)
  previous_block = block_to_add
  print ("Block #{} has been added to the blockchain!".format(block_to_add.index))
  print ("Hash: {}\n".format(block_to_add.hash))

    
