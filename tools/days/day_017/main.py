from days.day_017.files.helpers import *
from days.day_017.files.question_model import Question
from days.day_017.files.data import question_data
from days.day_017.files.quiz_brain import QuizBrain

def day_017():
	title("QUIZ")
	question_bank = []

	for i in question_data:
		question_text = i["question"]
		question_answer = i["correct_answer"]
		question = Question(question_text,question_answer)
		question_bank.append(question)

	random.shuffle(question_bank)

	quiz = QuizBrain(question_bank)
	quiz.next_question()