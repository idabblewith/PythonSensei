from days.day_034.files.helpers import *
from days.day_034.files.question_model import Question
from days.day_034.files.data import get_data
from days.day_034.files.quiz_brain import QuizBrain
from days.day_034.files.ui import QuizInterface

def day_034():
	title("QUIZZLER")
	question_bank = []
	question_data = get_data()
	for question in question_data:
		question_text = question["question"]
		question_answer = question["correct_answer"]
		new_question = Question(question_text, question_answer)
		question_bank.append(new_question)


	quiz = QuizBrain(question_bank)
	quiz_ui = QuizInterface(quiz)

	print("You've completed the quiz")
	print(f"Your final score was: {quiz.score}/{quiz.question_number}")