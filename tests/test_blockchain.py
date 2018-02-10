from blockchain.blockchain import Blockchain
from blockchain.blockchain import InvalidProofError
import numpy as np
import pytest


def test_proof_of_work():
    bc = Blockchain()
    next_proof = bc.proof_of_work(100)  # proof of genesis block
    assert next_proof == 35293
    next_proof = bc.proof_of_work(35293)
    assert next_proof == 35089
    next_proof = bc.proof_of_work(35089)
    assert next_proof == 119678
    next_proof = bc.proof_of_work(119678)
    assert next_proof == 146502


def mine_new_block(blockchain, proof_num):
    prev_len = len(blockchain.chain)
    prev_block = blockchain.last_block
    # provide valid proof number:
    new_block = blockchain.new_block(proof_num)
    # was the block added to the chain?
    assert prev_len + 1 == len(blockchain.chain)
    # was it mined correctly?
    assert blockchain.valid_proof(prev_block["proof"], new_block["proof"]) is True


def test_new_block_valid_proof():
    bc = Blockchain()
    mine_new_block(bc, 35293)


def test_new_block_invalid_proof():
    bc = Blockchain()
    prev_len = len(bc.chain)
    # provide invalid proof number:
    with pytest.raises(InvalidProofError) as e_info:
        bc.new_block(666)
    # the block should not have been added to the chain
    assert prev_len == len(bc.chain)


def test_new_transaction():
    bc = Blockchain()
    prev_trans_len = len(bc.current_transactions)

    sender, recipient, amount = "1234567890", "0987654321", 33

    next_block_index = bc.new_transaction(sender, recipient, amount)
    # new_transaction() should return the index of the next block
    assert next_block_index == len(bc.chain) + 1

    # was the transaction added to the chain?
    assert prev_trans_len+1 == len(bc.current_transactions)
    assert bc.current_transactions[-1] == {"sender": sender, "recipient": recipient, "amount": amount}

    mine_new_block(bc, 35293)
    assert bc.chain[-1].previous_hash == bc.chain[-2].__hash__()


def test_new_transactions_1000():
    bc = Blockchain()
    num_transactions = 1000

    np.random.seed = 20180210
    transactions_values = np.random.randint(100000, size=(num_transactions, 3))

    for i in range(0, num_transactions):
        prev_trans_len = len(bc.current_transactions)

        sender = transactions_values[i, 0]
        recipient = transactions_values[i, 1]
        amount = transactions_values[i, 2]

        next_block_index = bc.new_transaction(sender, recipient, amount)
        # new_transaction() should return the index of the next block
        assert next_block_index == len(bc.chain) + 1

        # was the transaction added to the chain?
        assert prev_trans_len+1 == len(bc.current_transactions)
        assert bc.current_transactions[-1] == {"sender": sender, "recipient": recipient, "amount": amount}

        if i == 250:
            mine_new_block(bc, 35293)
            assert bc.chain[-1].previous_hash == bc.chain[-2].__hash__()
        if i == 500:
            mine_new_block(bc, 35089)
            assert bc.chain[-1].previous_hash == bc.chain[-2].__hash__()
        if i == 750:
            mine_new_block(bc, 119678)
            assert bc.chain[-1].previous_hash == bc.chain[-2].__hash__()
        if i == 1000:
            mine_new_block(bc, 146502)
            assert bc.chain[-1].previous_hash == bc.chain[-2].__hash__()

