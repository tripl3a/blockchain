# to start Flask server simply call "python server.py"

from uuid import uuid4
from flask import Flask
from flask import request
import json
import blockchain as bc
import json

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
    new_proof = blockchain.proof_of_work(blockchain.last_proof)

    blockchain.new_transaction(
        sender=blockchain.mining_sender_address,
        recipient=node_identifier,
        amount=blockchain.mining_reward_amount
    )

    block = blockchain.new_block(new_proof)

    response = {
        'message': "New Block Forged",
        'index': block.index,
        'transactions': block.transactions,
        'proof': block.proof,
        'previous_hash': block.previous_hash,
    }
    return json.dumps(response, cls=bc.LazyEncoder, indent=4), 200


@app.route("/sum", methods=["GET"])
def sum_transactions():
    response = {
        "total amount of all transactions": blockchain.total_transactions_amount()
    }
    return json.dumps(response, cls=bc.LazyEncoder, indent=4), 200


with open('config.json', 'r') as f:
    config = json.load(f)

ip_address = config['HOST_IP']['IP_ADDRESS']
port_number = int(config['HOST_IP']['PORT_NUMBER'])

if __name__ == "__main__":
    app.run(host=ip_address, port=port_number)

