# easygames
The easygames library in Python

## Installation

#### Install from PIP

```
$ pip install oneplayergames
```

## From Python scripts

### Import module

```python
import easygames
```

### Rock-Paper-Scissors

```python
winner = easygames.rock_paper_scissors()
```

This gets the input from the user, randomly generates one for the computer, and works out the winner.

#### Return values:
* 0 if draw
* 1 if player wins
* 2 if computer wins

### Guess the number

```python
guesses = easygames.guess_the_number()
```

This gets the input from the user until the number is guessed correctly.

#### Parameters:
n: int (optional, default: 100) = Maximum number which can be the computer's number. In other words, the computer generates a random number from 1 to n.

#### Return value:
Number of guesses it took for the user to guess the number correctly

### Fizz Buzz

```python
num = easygames.fizz_buzz()
```

Count up from 1:
- if the number is a multiple of 3, type 'F' for 'Fizz'
- if the number is a multiple of 5, type 'B' for 'Buzz'
- if the number is a multiple of 3 and 5, type 'FB' for 'FizzBuzz'
- otherwise, just type the number

For example ('#' indicates comment)

```python
1
2
F # instead of 3
4
B # instead of 5
F # instead of 6
7
8
F # instead of 9
B # instead of 10
11
F # instead of 12
13
14
FB # instead of 15
```

#### Return value:
The number that the user got up to before making a mistake

## From the terminal

### Use the `play` command

#### Rock-Paper-Scissors

```
$ play rps
```

#### Guess the number

```
$ play gtn
```

#### Fizz Buzz

```
$ play fb
```
