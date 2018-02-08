# to start Flask server simply call "python server.py"

from uuid import uuid4
from flask import Flask
from flask import request
import json
import blockchain as bc

# Instantiate our node
app = Flask(__name__)
# In debug mode the server doesn't need a restart to reflect code changes
app.debug = True

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace("-", "")

# Instantiate the blockchain
blockchain = bc.Blockchain()


@app.route("/chain", methods=["GET"])
def full_chain():
    response = {
        "chain": blockchain.chain,
        "length": len(blockchain.chain)
    }
    return json.dumps(response, cls=bc.LazyEncoder, indent=4), 200


@app.route("/transactions/new", methods=["POST"])
def new_blockchain_transaction():
    values = request.get_json()

    # Check that the required fields are in the POST'ed data
    required = ("sender", "recipient", "amount")
    if not all(k in values for k in required):
        return "Missing values", 400

    # Create a new transaction
    index = blockchain.new_transaction(values["sender"], values["recipient"], values["amount"])

    response = {"message": f"Transaction will be added to Block %s" % index}
    return json.dumps(response, cls=bc.LazyEncoder, indent=4), 201


@app.route("/mine", methods=["GET"])
def blockchain_mine():
    last_block = blockchain.last_block
    last_proof = last_block["proof"]
    proof = blockchain.proof_of_work(last_proof)

    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1
    )

    previous_hash = last_block.__hash__()
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return json.dumps(response, cls=bc.LazyEncoder, indent=4), 200


host_ip = "127.0.0.1"

if __name__ == "__main__":
    app.run(host=host_ip, port=5000)

