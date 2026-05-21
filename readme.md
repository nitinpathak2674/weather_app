# Number Guessing Game

A simple command-line Number Guessing Game built using Python. The player has to guess the correct random number within limited attempts based on selected difficulty level.

## Features

- Multiple difficulty levels
- Random number generation
- Limited attempts system
- High / Low hints
- Input validation
- Simple terminal-based gameplay

## Difficulty Levels

| Difficulty | Range | Attempts |
|------------|-------|----------|
| Easy | 1 - 50 | 10 |
| Medium | 1 - 100 | 7 |
| Hard | 1 - 200 | 5 |

## Technologies Used

- Python
- Random Module

## How to Run

1. Clone the repository

```bash
git clone https://github.com/nitinpathak2674/number_guessing_system.git
```

2. Open project folder

```bash
cd number_guessing_system
```

3. Run the project

```bash
python main.py
```

## Project Structure

```text
number_guessing_system/
│
├── main.py
└── README.md
```

## Sample Output

```text
===== NUMBER GUESSING GAME =====

Select Difficulty Level
1. Easy
2. Medium
3. Hard

Enter choice (1/2/3): 2

Guess the number between 1 and 100
You have 7 attempts

Enter your guess: 50
Too High

Attempts Left: 6

Enter your guess: 25
Too Low

Attempts Left: 5

Enter your guess: 37

Congratulations! Correct Guess.
```

## Learning Outcomes

- Conditional Statements
- Loops
- Exception Handling
- Random Number Generation
- User Input Handling

## Run Command
python weather_app.py

## Author

Nitin Pathak