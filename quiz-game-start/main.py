from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [] # Initialize the list
for question in question_data: # loop through the question_data list
    question_text = question["text"] # text is the key-value pair at text
    question_answer = question["answer"] # answer is the key-value pair at answer
    new_question = Question(question_text, question_answer) # Pass in the variables into question constructor
    question_bank.append(new_question) # Append it to the question_bank list

quiz = QuizBrain(question_bank) # Takes the QuizBrain class and initalizes the question_bank list

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was {quiz.score}/{quiz.question_number}")