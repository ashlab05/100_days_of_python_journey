from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    question_bank.append(Question(i["question"],i["correct_answer"]))

quiz_brain = QuizBrain(question_bank)

while not quiz_brain.still_has_question():
    quiz_brain.next_question()

print(f"Your final score is {quiz_brain.score}/{quiz_brain.qno}")