class Brain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number >= len(self.question_list):
            return False
        else:
            return True

    def ask_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)? ")
        self.check_answer(answer, current_question.answer)

    def check_answer(self, answer, q_answer):
        if answer.lower() == q_answer.lower():
            print("You are right!")
            self.score += 1
        else:
            print("You are false!")
        print(f"Answer was: {q_answer}")
        print(f"Score: {self.score}/{self.question_number}")
        print("\n")