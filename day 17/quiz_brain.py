class QuizBrain:
    def __init__(self, question_list):
        self.qno = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.qno].question_text
        answer = self.question_list[self.qno].answer_text

        self.qno += 1

        inp = input(f"Q.{self.qno}.{question}: True or False ")

        self.check_answer(inp, answer)

    def still_has_question(self):
        return self.qno == len(self.question_list)

    def check_answer(self,qn,ans):
        if qn == ans:
            print("Correct!")
            self.score += 1
        else:
            print("Wrong!")
        print(f'Your score is {self.score}/{self.qno}.')