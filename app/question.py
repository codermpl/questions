
class Question(object):
    """ Class to represent questions """

    def __init__(self, question, answer, distractors):
        self.question = question
        self.answer = answer
        self.distractors = distractors
