from blockchain import Blockchain


def test_new_block_invalid_proof():
    bc = Blockchain()
    prev_len = len(bc.chain)
    pb = bc.last_block
    # provide invalid proof number:
    nb = bc.new_block(666)
    # was the block added to the chain?
    assert prev_len+1 == len(bc.chain)
    # was it mined correctly?
    # TODO: does it make sense to add the block when the proof isn't valid??
    assert bc.valid_proof(pb["proof"], nb["proof"]) is False


def test_new_block_valid_proof():
    bc = Blockchain()
    prev_len = len(bc.chain)
    pb = bc.last_block
    # provide valid proof number:
    nb = bc.new_block(35293)
    # was the block added to the chain?
    assert prev_len+1 == len(bc.chain)
    # was it mined correctly?
    assert bc.valid_proof(pb["proof"], nb["proof"]) is True

