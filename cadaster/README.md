# Cadastre Project

## Overview
The Cadastre project is a Python application designed to collect user information and save it to a database. It provides a simple interface for users to input their name, surname, and year of birth.

## Features
- Collects user information through a command-line interface.
- Saves user data to a database.
- Includes unit tests to ensure functionality.

## Project Structure
```
cadaster
├── .github
│   └── workflows
│       └── python-ci.yml
├── src
│   ├── main.py
│   ├── cadastre.py
│   └── register.py
├── tests
│   └── test_main.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd cadaster
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
python src/main.py
```

Follow the prompts to enter your name, surname, and year of birth. The information will be saved to the database.

## Testing
To run the tests, use the following command:
```
pytest tests/test_main.py
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.