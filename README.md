# A simple Blockchain Implementation in Python 

Advanced Software Engineering Pet Project
for the Data Sciences Master's Program at Beuth University of Applied Sciences, Berlin

## Exercise

A) Write a small pet project to get into coding again. 
You might want to use a language as Python which is also good for this Master! 
The Code can be relatively simple (as a simple game with console output).

B) Make sure each Person has applied the following topics on the code which have been taught in the lecture:

* UML (at least 5 diagrams)
* Metrics (at least two. Sonarcube would be great)
* Clean Code Development (at least 5 points you can show me)
* Continous Delivery (show me your pipeline in e.g. Jenkins and Travis-CI)
* AOP (show me where you could have integrated AOP stuff => the jointpoints)
* DSL (Create a small DSL Demo example snippet in your code even if it does not contribute to your project)
* Functional Programming (prove that you have covered all functional definitions in your code as
    * only final data structures
    * (mostly) side effect free functions
    * the use of higher order functions
    * functions as parameters and return values
    * use clojures / anonymous functions
* Show me an idea where to use a logical solver in your code and how you would do it!
* Write a little code fragment (like data preparation etc.) in Scala or Clojure!

The complete project must be sent to the lecturer in the last weeks before the semester ends = 8th February 2018! 
The contribution must include the link to GitHub and 3 pages explaining B (or links to B) as a MarkupPage in GitHub!

Zuletzt geändert: Freitag, 12. Januar 2018, 19:35


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Interacting with the Blockchain

I used Postman to interact with the Blockchain API over HTTP.

Start the server:
```
$ python server.py

* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

View the full chain by requesting [http://localhost:5000/chain]()

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











