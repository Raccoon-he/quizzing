class QuizSession:
    def __init__(self):
        self.score = 0
        self.questions = []
        self.current_question_index = 0
        self.wrong_answers = []  

    def start_quiz(self, questions):
        self.questions = questions
        self.score = 0
        self.current_question_index = 0
        self.wrong_answers = []  # reset the wrong answer list

    def submit_answer(self, answer):
        question = self.questions[self.current_question_index]
        if answer == question["answer"]:
            self.score += 1  
        else:
            # save information of wrong quesions
            wr_question = question # make a copy
            wr_question['users_answer'] = answer
            self.wrong_answers.append(wr_question)
        self.current_question_index += 1
        
    def end_quiz(self):
        total_score = self.score # show the final score to user
        print("Score you got is: {}.\n".format(total_score))

    def get_wrong_answers(self): # show information about wrong questions
        print('------ Questions your answered wrong ------')
        for i in range(len(self.wrong_answers)):
            print('Question {}'.format(self.wrong_answers[i]['id']))
            print(self.wrong_answers[i]['text'])
            print('Category: {}'.format(self.wrong_answers[i]['category']))
            print('Difficulty: {}'.format(self.wrong_answers[i]['difficulty']))
            print('Answer: {}'.format(self.wrong_answers[i]['answer']))
            print('Your answer: {}\n'.format(self.wrong_answers[i]['users_answer']))
        print('------ Above are all ------')
        return 'Good luck for next time!'