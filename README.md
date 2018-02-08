# A basic Blockchain Implementation in Python 

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

## Clean Code Development

Principles were applied according to: [http://clean-code-developer.de/die-grade/roter-grad/]()

### Using a version control system 

Well, as you can see we're on GitHub here... :white_check_mark:

### Apply simple refactoring patterns

#### Extract methods (DRY principle)

e.g. the hash() method: first it was in the Blockchain class. 
But then I created the class Block where I also wanted a hash() method.
First I copy & pasted the code. Eventually I was able to delete the method in Blockchain.
(see commit f94974e7170cbe10a7e9154a991ae62101df2795)

### Rename cryptic names (scout rule)

for example in commit 7fcebf465a8359312bd1650f62e2c18e257c0519 of test_blockchain.py :white_check_mark:

## Continuous Delivery

[Travis-CI](https://travis-ci.org/tripl3a/blockchain) has been used as the tool for Continuous Integration.

## Metrics

For metrics I used [Sonarcloud](https://sonarcloud.io/dashboard?id=tripl3a-github-token%3Aworking-copy)

## AOP + Functional Programming

The following requirements where solved by writing a Decorator:
* the use of higher order functions :white_check_mark:
* functions as parameters and return values :white_check_mark:
* use closures :white_check_mark:
* AOP :white_check_mark:
The decorator @logger is used in the class Blockchain to print console outputs 
before entering and after executing a (decorated) method. 
Using Decorators is also a way to add aspects to Python methods. (=> AOP)

## DSL

Can be found in a [separate git repository](https://github.com/tripl3a/dsl)

## Interacting with the Blockchain

I used Postman to interact with the Blockchain API over HTTP.

Start the server:
```
$ python server.py

* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

View the full chain by GET requesting [http://localhost:5000/chain]()

Create a new transaction by making a POST request to
[http://localhost:5000/transactions/new]()
with a body containing our transaction structure:
```
{
 "sender": "my address",
 "recipient": "someone else's address",
 "amount": 5
}
```


Mine a block by making a GET request to [http://localhost:5000/mine]()
