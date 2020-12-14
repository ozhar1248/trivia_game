from question import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))

quiz = QuizBrain(question_bank)

while quiz.has_questions():
    quiz.next_question()

grade = round(quiz.score / len(question_bank) * 100, 2)
print(f"You've completed the quiz\nYour final score is {grade}")
