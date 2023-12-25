from question_model import Question
from quiz_brain import Brain
from data import questions


question_bank = []
for question in questions:
    tmp_question = Question(question["question"], question["correct_answer"])
    question_bank.append(tmp_question)

brain = Brain(question_bank)

while brain.still_has_questions():
    brain.ask_question()
