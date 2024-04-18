from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    q = i['question']
    a = i['correct_answer']
    new_question = Question(q, a)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    u_answer = quiz.next_question()
