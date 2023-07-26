class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0
    def still_has_question(self):
        if self.question_number>=len(self.question_list):
            return False
        else:
            return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        return input(f"Q.{self.question_number }: {current_question.text} (True/False): ")
    def check_answer(self,u_ans):
        if u_ans == self.question_list[self.question_number].answer:
            self.score+=1
            return True

