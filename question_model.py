class Question:
  def __init__(self, question, answer):
    self.question = question
    self.answer = answer

  def answer_question(self, answer):
    return answer == self.answer