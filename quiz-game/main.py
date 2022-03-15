from question_model import NewQuestion
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_question = NewQuestion(question["text"], question["answer"])
    question_bank.append(new_question)

brainy = QuizBrain(question_bank)
while brainy.still_has_question():
    brainy.next_question()
print("You've completed the quiz")
print(f"You're final score was {brainy.score}/{brainy.question_number}")