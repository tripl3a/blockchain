# to start Flask server simply call "python server.py"

from uuid import uuid4
from flask import Flask
from flask import request
import json

from blockchain import Blockchain

# Instantiate our node
app = Flask(__name__)
# In debug mode the server doesn't need a restart to reflect code changes
app.debug = True

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace("-", "")

# Instantiate the blockchain
blockchain = Blockchain()


@app.route("/chain", methods=["GET"])
def full_chain():
    response = {
        "chain": blockchain.chain,
        "length": len(blockchain.chain)
    }
    return json.dumps(response), 200


@app.route("/transactions/new", methods=["POST"])
def new_blockchain_transaction():
    print("new transaction started...")
    values = request.get_json()

    # Check that the required fields are in the POST'ed data
    required = ["sender", "recipient", "amount"]
    if not all(k in values for k in required):
        return "Missing values", 400

    # Create a new transaction
    index = blockchain.new_transaction(values["sender"], values["recipient"], values["amount"])

    response = {"message": f"Transaction will be added to Block {index}"}
    print("...new transaction finished")
    return json.dumps(response), 201


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

    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return json.dumps(response), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
