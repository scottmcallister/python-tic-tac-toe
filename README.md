# python-tic-tac-toe

A terminal game of tic tac toe for playing against an unbeatable AI opponent.

<p align="center">
    <img src="screen.png" style="margin: auto;" >
</p>

## Getting Started

To play the game in your terminal, you can clone this repository and run main.py with Python 3:

```
# clone and cd into directory

$ git clone https://github.com/scottmcallister/python-tic-tac-toe.git
$ cd python-tic-tac-toe


# if you don't have curses and/or want to use virtualenv

$ virtualenv -p python3 env
$ source env/bin/activate
(env) $ pip install -r requirements.txt
(env) $ python main.py
```

### Prerequisites

To run this game you'll need Python 3 and curses installed through pip. 

## Running Tests

All unit tests have been written in `test.py`. The unit tests do not cover the rendering logic in `main.draw_game`, but all other helper functions can be tested. 

```
(env) $ python test.py
......
----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK
```

## Built With

* [Python 3](https://www.python.org/) - Programming language
* [curses](https://docs.python.org/3/howto/curses.html) - UI library
