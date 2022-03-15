
class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_question(self):
        return not self.question_number == len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        if correct_answer.lower() == user_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That is wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def next_question(self):
        ques = self.questions_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}: {ques.text} (True/False)?: ").lower()
        self.check_answer(user_input, ques.ans)


