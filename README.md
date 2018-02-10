# A basic Blockchain Implementation in Python 

![TravisCI](https://travis-ci.org/tripl3a/blockchain.svg?branch=master) 
![SonarCloud](https://sonarcloud.io/api/project_badges/measure?project=tripl3a-github-token%3Aworking-copy&metric=alert_status)

Advanced Software Engineering Pet Project
for the Data Sciences Master's Program at Beuth University of Applied Sciences, Berlin.

requirements: see requirements.txt

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

I worked with Python 3 and installed the following additional packages via anaconda.

```
conda install flask
conda install django
```

Furthermore I used Postman as HTTP client to interact with the Flask WebApp.

### Installing

Just clone / download this repository.

## Interacting with the Blockchain

I used Postman to interact with the Blockchain API over HTTP.

Start the server:
```
$ python server.py

* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### Adding a transaction

Create a new transaction by making a POST request to
[http://localhost:5000/transactions/new]()
with a body containing our transaction structure, e.g.:
```
{
 "sender": "my address",
 "recipient": "someone else's address",
 "amount": 3
}
```

![POST new transaction](./docs/screenshots/POST_new_transaction.png)

### Mining a block

Mine a block by making a GET request to [http://localhost:5000/mine]()

![GET mine](./docs/screenshots/GET_mine.png)

### Viewing the chain 

View the full chain by GET requesting [http://localhost:5000/chain]()

![GET chain](./docs/screenshots/GET_chain.png)

## Clean Code Development

Principles were applied according to: 
* [http://clean-code-developer.de/die-grade/roter-grad/]()
* [http://clean-code-developer.de/die-grade/orangener-grad/]()

### Using a version control system 

Well, as you can see we're on GitHub here... :white_check_mark:

### Apply simple refactoring patterns

#### Extract methods (DRY principle)

e.g. the hash() method: First it was in the Blockchain class. 
Then I created the class Block where I also wanted a hash() method.
After copy & pasting the code I was eventually able to delete the method in Blockchain.
(see [this commit](https://github.com/tripl3a/blockchain/commit/f94974e7170cbe10a7e9154a991ae62101df2795)) :white_check_mark:

### Rename cryptic names (scout rule)

for example in [this commit](https://github.com/tripl3a/blockchain/commit/7fcebf465a8359312bd1650f62e2c18e257c0519) of test_blockchain.py :white_check_mark:

### Automated Integration/Unit Tests

Automated integration/unit tests have been implemented, see [test_blockchain.py](./tests/test_blockchain.py)). :white_check_mark:

Run them manually in terminal: 
```
py.test test_blockchain.py
```

## Continuous Delivery

[Travis-CI](https://travis-ci.org/tripl3a/blockchain) has been used as the tool for Continuous Integration.
The config file can be found [here][1] and the builds are located [here][2].

[1]: https://github.com/tripl3a/blockchain/blob/working-copy/.travis.yml
[2]: https://travis-ci.org/tripl3a/blockchain/builds

## Metrics

For metrics I used [Sonarcloud](https://sonarcloud.io/dashboard?id=tripl3a-github-token%3Aworking-copy).

![CodeSmells](https://sonarcloud.io/api/project_badges/measure?project=tripl3a-github-token%3Aworking-copy&metric=code_smells)

![DuplicatedLines](https://sonarcloud.io/api/project_badges/measure?project=tripl3a-github-token%3Aworking-copy&metric=duplicated_lines_density)

![Maintainability](https://sonarcloud.io/api/project_badges/measure?project=tripl3a-github-token%3Aworking-copy&metric=sqale_rating)

![Reliability](https://sonarcloud.io/api/project_badges/measure?project=tripl3a-github-token%3Aworking-copy&metric=reliability_rating)

![Security](https://sonarcloud.io/api/project_badges/measure?project=tripl3a-github-token%3Aworking-copy&metric=security_rating)

![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=tripl3a-github-token%3Aworking-copy&metric=vulnerabilities)

## Aspect Oriented Programming & Functional Programming

The following requirements where solved by writing a Decorator:
* the use of higher order functions :white_check_mark:
* functions as parameters and return values :white_check_mark:
* use closures :white_check_mark:
* AOP :white_check_mark:

The decorator [@logger](https://github.com/tripl3a/blockchain/blob/566117b215bd88af58da5b26237b1389282e2789/blockchain.py#L66) is used in the class Blockchain to print console outputs 
before entering and after executing a (decorated) method. 
Using Decorators is also a way to add aspects to Python methods. (=> AOP)

## Domain Specific Language

A small example for a DSL in Python can be found in a [separate git repository](https://github.com/tripl3a/dsl).

## UML

### Use case diagram

![UML use case](./docs/diagrams/UML_UseCaseDiagram.png)

### Class diagram

![UML classes](./docs/diagrams/classes_blockchain.png)

### Sequence diagram for adding a transaction

![UML transaction](./docs/diagrams/UML_SequenceDiagram_transaction.png)

### Sequence diagram for mining a block

![UML mine](./docs/diagrams/UML_SequenceDiagram_mine.png)

### Sequence diagram for viewing the block chain

![UML chain](./docs/diagrams/UML_SequenceDiagram_chain.png)

### State diagram

![UML state](./docs/diagrams/UML_StateDiagram.png)



