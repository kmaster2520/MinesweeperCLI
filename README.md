# MinesweeperCLI

I developed Minesweeper that can be played on the command line interface (CLI). 

## Setup

MinesweeperCLI only requires Python 3 the numpy library to run.

## Running

The game starts by typing the following command:
```
$ python game.py
```
Depending on your Python 3 installation, you have to type ```python3``` instead of ```python```. It is recommended to make the terminal window large to fit the game board view.


## Player Commands

To select a space, type:
```
> s <row> <column>
```
The game map will update upon the execution of the command. If the command is not formatted correctly, the command prompt will appear again with or without an error message.

Note: The ability to flag certain spaces has not been implemented yet.