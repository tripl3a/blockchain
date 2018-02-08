from blockchain.blockchain import Blockchain


def test_new_block_invalid_proof():
    bc = Blockchain()
    prev_len = len(bc.chain)
    prev_block = bc.last_block
    # provide invalid proof number:
    new_block = bc.new_block(666)
    # was the block added to the chain?
    assert prev_len+1 == len(bc.chain)
    # was it mined correctly?
    # TODO: does it make sense to add the block when the proof isn't valid??
    assert bc.valid_proof(prev_block["proof"], new_block["proof"]) is False


def test_new_block_valid_proof():
    bc = Blockchain()
    prev_len = len(bc.chain)
    prev_block = bc.last_block
    # provide valid proof number:
    new_block = bc.new_block(35293)
    # was the block added to the chain?
    assert prev_len+1 == len(bc.chain)
    # was it mined correctly?
    assert bc.valid_proof(prev_block["proof"], new_block["proof"]) is True


def test_new_transaction():
    bc = Blockchain()
    prev_trans_len = len(bc.current_transactions)
    next_block = bc.new_transaction("senderID", "receipientID", 33)
    # new_transaction() should return the index of the next block
    assert next_block == len(bc.chain) + 1
    # was the transaction added to the chain?
    assert prev_trans_len+1 == len(bc.current_transactions)




