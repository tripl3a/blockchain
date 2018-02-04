import hashlib
import json
from time import time
from uuid import uuid4
from flask import Flask
from django.core.serializers.json import DjangoJSONEncoder


class LazyEncoder(DjangoJSONEncoder):
    """
    needed for JSON serialization of my custom classes
    """
    def default(self, obj):
        if isinstance(obj, Block):
            return str(obj)
        return super().default(obj)
    """
    def default(self, obj):
        return json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    """


class Block:
    def __init__(self, index, timestamp, transactions, proof, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.proof = proof
        self.previous_hash = previous_hash

    @staticmethod
    def hash(self):
        """
        Creates a SHA-256 hash of this block

        :return: <str>
        """

        # We must ensure that the dictionary is ordered, or we'll get inconsistent hashes
        block_string = json.dumps(self.__getitem__(), sort_keys=True, cls=LazyEncoder).encode()
        return hashlib.sha256(block_string).hexdigest()

    def __str__(self):
        return str(self.__getitem__())

    __repr__ = __str__

    def __getitem__(self, key=None):
        """
        makes class Block "subscriptable", as it is a container
        """
        if key is not None:
            return self.__dict__[key]
        else:
            return self.__dict__


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Create the genesis block
        self.new_block(previous_hash=1, proof=100)

    # TODO: isn't it a security issue to let previous_hash be optional?!
    def new_block(self, proof, previous_hash=None):
        """
        Creates a new block in the blockchain

        :param proof: <int> The proof given by the proof of work algorithm
        :param previous_hash: (Optional) <str> hash of previous block
        :return: <dict> New block
        """

        # TODO: check if there are current transactions:
        # TODO: implement as a function (-> functional programming)
        #if len(self.current_transactions) == 0:
        #    raise Exception("No current transactions!")

        # TODO: implement proof check, something like this:
        # TODO: implement as a function (-> functional programming)
        #if self.valid_proof(self.last_block["proof"], proof) is False:
        #    raise Exception("Block rejected due to incorrect proof!")

        block = Block(index=len(self.chain) + 1,
                      timestamp=time(),
                      transactions=self.current_transactions,
                      proof=proof,
                      # previous_hash=previous_hash or self.hash(self.chain[-1]
                      previous_hash=previous_hash or self.chain[-1].__hash__())

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined block

        :param sender: <str> Address of the sender
        :param recipient: <str> Address of the recipient
        :param amount: <int> Amount
        :return: <int> The index of the block that will hold this transaction
        """

        self.current_transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        })

        return self.last_block["index"] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """
        Simple proof of work algorithm:
        - find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
        - p is the previous proof, and p' is the new proof

        :param last_proof: <int>
        :return: <int>
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the proof: Does hash(last_proof, proof) contain 4 leading zeros?

        :param last_proof: <int> Previous proof
        :param proof: Current proof
        :return: <bool> True if correct, False if not
        """

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
