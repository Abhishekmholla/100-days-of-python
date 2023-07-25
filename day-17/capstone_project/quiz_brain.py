class QuizBrain:
    
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.questions_list = question_list
        self.score  = 0
    
    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        return question
    
    def check_result(self, question,user_choice):
        if user_choice != question.answer.lower():
            print("That's wrong.")
            return self.score
        
        print("That's correct.")
        self.score +=1
        return self.score