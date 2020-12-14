class QuizBrain:
    def __init__(self, bank):
        self.question_bank = bank
        self.question_number = 0
        self.score = 0

    def next_question(self):
        ans = input(f"Q.{self.question_number+1}: {self.question_bank[self.question_number].question} (True / False): ")
        self.check_answer(ans, self.question_bank[self.question_number].answer)
        self.question_number += 1

    def has_questions(self):
        return self.question_number < len(self.question_bank)

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("Right!")
            self.score += 1
        else:
            print("Wrong!")
        print(f"The correct answer is {correct_ans}")
        print(f"Your current score is {self.score}/{len(self.question_bank)}\n")
