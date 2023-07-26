from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for i in question_data:
    question=Question(i["text"],i["answer"])
    question_bank.append((question))
quiz=QuizBrain(question_bank )
checkans=True
while quiz.still_has_question() and checkans:
    user_answer=quiz.next_question()
    checkans=quiz.check_answer(user_answer)
print(f"your score is {quiz.score}/{len(quiz.question_list)}")

