# Midnight Calculator

A dark mode GUI calculator created with Tkinter in Python. 

<picture>
    <img src="https://i.imgur.com/UZTSVZ7.gif" alt="demo of calculator GUI">
</picture>

## Motivation

More Python practice and an exploration into graphical user interfaces 
as an aspiring software developer.

## Installation

    git clone https://github.com/praerie/midnight-calculator
    cd midnight-calculator
    python main.py

## Capabilities

### Current:
* Performs addition, subtraction, multiplication, and division on types `int` and `float`.
* Handles complex expressions with use of parentheses.
* Calculates modulus of any two numbers or expressions with "%" button.
* Drops unnecessary decimal points when displaying answers (e.g. `n.0` displays as `n`). 
* Automatically clears leading zeros.
* Erases entire input field with "clear" button and erases last character with "❰" button.

### Future:
* Automatically add leading zero before initial decimal points.
* Replace last symbol in input field with most recently selected symbol.
* Calculate square root of a number.
* Display expression above answer.
* Improve exceptions and error messages.
