#create a txt file "quiz.txt" that contain multiple choice 
'''
import os 
def create_file(filename):
    try:
        with open(filename,"quiz"):
            f.write('')
        print("quiz"+filename)
    except IOError:
        print("the is some error")

def write_file(filename):
    try:
        with open(filename):
            f.write("who was the first Persident of United States of America")


def load_quiz(filename):
    with open(filename, 'r') as file:
        quiz_data = file.readlines()
    return quiz_data

def quiz():
    quiz_data = load_quiz('quiz.txt')
    score = 0

    for line in quiz_data:
        print(line.strip())
        user_answer = input("Your answer (Enter A, B, or C): ").upper()
        correct_answer = line[-2].upper()  # Get the correct answer from the last character of the line

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}\n")

    print(f"Your final score is: {score}/{len(quiz_data)//4}")

if __name__ == "__main__":
    quiz()
'''
def load_quiz(filename):
    with open(filename, 'r') as f:
        quiz_data = f.readlines()
        
    question = ''
    options = ''
    for line in quiz_data:
        line = line.strip()
        if line.endswith('?'):
            if question:
                print(question)
                print(options)
            question = line
            options = ''
        else:
            options += line + "\n"

    print(question)
    print(options)


load_quiz('quiz.txt')

