# Quiz Game Application

This project is a Python-based quiz application that uses MySQL as its backend database. The application allows users to play a quiz game or insert new questions into the database. 

## Features
- Play a quiz and test your knowledge.
- Dynamically fetch questions from the MySQL database.
- Add new questions to the database through a simple interface.
- Track your score during the quiz.

## Requirements
To run this project, you need the following:

- Python 3.8 or later
- MySQL Server
- `mysql-connector-python` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<repository-name>.git
   cd <repository-name>
   ```

2. Install required Python dependencies:
   ```bash
   pip install mysql-connector-python
   ```

3. Set up the MySQL database:
   - Create a database named `quiz`.
   - Create a table named `questions` with the following schema:
     ```sql
     CREATE TABLE questions (
         id INT AUTO_INCREMENT PRIMARY KEY,
         question VARCHAR(255),
         option1 VARCHAR(100),
         option2 VARCHAR(100),
         option3 VARCHAR(100),
         option4 VARCHAR(100),
         correct_option INT
     );
     ```

4. Update the `host`, `user`, `password`, and `database` parameters in the script to match your MySQL credentials.

## Usage

1. Run the script:
   ```bash
   python quiz_game.py
   ```

2. Choose from the following options:
   - **1**: Play the quiz. The script fetches questions from the database and lets you answer them. Your score is displayed at the end.
   - **2**: Insert new questions into the database. Enter the question, options, and the correct answer when prompted.
   - **3**: Exit the program.

## Example Interaction

**Play Quiz**:
```text
Enter 1 for playing quiz & 2 for input questions 3 for exit: 1
Q: What is the capital of France?
1: Berlin
2: Madrid
3: Paris
4: Rome
Enter your answer (1 - 4): 3
Correct!
Your score 1
```

**Insert Question**:
```text
Enter 1 for playing quiz & 2 for input questions 3 for exit: 2
Enter Question: What is 2+2?
Enter option 1: 3
Enter option 2: 4
Enter option 3: 5
Enter option 4: 6
Enter correct option (1 - 4): 2
details are inserted successfully! 
Enter 1 to submit another question & 2 for exit: 2
```

## Author
Created by Bandhan Hardiya

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
