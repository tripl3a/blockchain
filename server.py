from uuid import uuid4
from flask import Flask

from blockchain import Blockchain

# Instantiate our node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace("-", "")

# Instantiate the blockchain
blockchain = Blockchain()


@app.route("/mine", methods=["GET"])
def blockchain_mine():
    return "We'll mine a new block"


@app.route("/transactions/new", methods=["POST"])
def new_blockchain_transaction():
    return "We'll add a new transaction"


@app.route("/chain", methods=["GET"])
def full_chain():
    response = {
        "chain": blockchain.chain,
        "length": len(blockchain.chain)
    }
    return Flask.jsonify(response), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)


@app.route("/transactions/new", methods=["POST"])
def new_blockchain_transaction():
    values = request.get_json()

    # Check that the required fields are in the POST'ed data
    required = ["sender", "recipient", "amount"]
    if not all(k in values for k in required):
        return "Missing values", 400

    # Create a new transaction
    index = blockchain.new_transaction(values["sender"], values["recipient"], values["amount"])

    response = {"message": f"Transaction will be added to Block {index}"}
    return Flask.jsonify(response), 201


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
        "message": "New block forged",
        "index": block["index"],
        "transactions": block["transactions"],
        "proof": block["proof"],
        "previous_hash": block["previous_hash"]
    }
    return Flask.jsonify(response), 200

