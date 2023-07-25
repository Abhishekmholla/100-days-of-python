from quiz_data import question_data
from quiz_question_model import QuestionModel
from quiz_brain import QuizBrain

question_bank = list()
for q_data in question_data:
    question_bank.append(QuestionModel(q_data['text'], q_data['answer']))

quiz = QuizBrain(question_bank)

for _ in question_bank:
    question = quiz.next_question()
    user_choice = input(f"\nQ.{quiz.question_number}: {question.text}(True/False)?: ").lower()

    total = quiz.check_result(question,user_choice)
    print(f"Your current score is: {total}/{quiz.question_number}")

print("\nYou have completed the quiz")
print(f"Your final score is {total}/{quiz.question_number}")