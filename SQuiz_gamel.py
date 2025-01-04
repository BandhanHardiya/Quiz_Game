import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="quiz"
)

cursor=conn.cursor()

def fetch_questions():
    cursor.execute("SELECT * FROM questions")
    return cursor.fetchall()

def play_quiz(questions):
    global score 
    score = 0
    for question in questions:
        print(f"Q: {question[1]}")
        print(f"1: {question[2]}")
        print(f"2: {question[3]}")
        print(f"3: {question[4]}")
        print(f"4: {question[5]}")
        user_answer = int (input("Enter your answer (1 - 4): "))
        if user_answer == question[6]:
           print("Correct!")
           score += 1
        else:
           print(f"Wrong! the correct answer is {question[6]} ")


def insert_questions():
    while True:
        que=input("Enter Question: ")
        op1=input("Enter option 1: ")
        op2=input("Enter option 2: ")
        op3=input("Enter option 3: ")
        op4=input("Enter option 4: ")
        ans=input("Enter correct option (1 - 4): ")

        querry="INSERT INTO questions (question,option1,option2,option3,option4,correct_option) VALUES (%s,%s,%s,%s,%s,%s)"
        values=(que,op1,op2,op3,op4,ans)
        cursor.execute(querry,values)
        conn.commit()
        print("details are inserted succesfully! ")
        choi=int(input("Enter 1 to submit another question & 2 for exit: "))
        if choi==1:
            continue
        else:
            break


cursor.execute("Use quiz")
while True:
    num = int(input("Enter 1 for playing quiz & 2 for input questions 3 for exit:"))
    if num == 1:
      questions = fetch_questions()
      play_quiz(questions)
      print(f"Your score {score}")
    
    elif num == 2:
        insert_questions()

    else:
        print("Created by Bandhan Hardiya")
        conn.close()
        cursor.close()
        break





