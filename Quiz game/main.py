from data import *
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []

for n in question_data:
    text = n["text"]
    answer = n["answer"]
    new_q = Question(text,answer)
    question_bank.append(new_q)
print(len(question_bank))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_questiion()

if quiz.question_number == len(question_bank):
    print("You have completed the quiz")
    print(f"Your final score is {quiz.score}/{quiz.question_number}")

    
