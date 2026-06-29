# Python CLI Calculator

A simple Command Line Interface (CLI) calculator built with Python. It allows users to perform basic arithmetic operations through an interactive menu.

## Features

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- Supports decimal (float) numbers
- Handles division by zero
- Menu-driven interface
- Perform multiple calculations until you choose to exit

## Requirements

- Python 3.x

## Installation

Clone this repository:

```bash
git clone https://github.com/your-username/python-cli-calculator.git
```

Navigate to the project directory:

```bash
cd python-cli-calculator
```

## Usage

Run the program:

```bash
python calculator.py
```

Example:

```text
===== Calculator =====
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

Enter choice (1-5): 3
Enter first number: 10
Enter second number: 5

Result = 50.0
```

## Project Structure

```text
python-cli-calculator/
├── calculator.py
└── README.md
```

## Notes

- Supports both whole numbers and decimal numbers.
- Selecting **5** exits the program.
- Division by zero displays an error message instead of crashing the program.

## Future Improvements

- Add modulus (%) and exponent (**) operations.
- Add square root and power functions.
- Improve input validation for non-numeric values.
- Create a graphical user interface (GUI).

## License

This project is open source and free to use.