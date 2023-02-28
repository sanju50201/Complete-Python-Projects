# function to display the questions

def display_questions(question):
    print(question['prompt'])
    for i, option in enumerate(question['options']):
        print(f'{i+1}. {option}')


# function to get the answer

def get_answer(question):
    while True:
        response = input("Enter the number of your answer: ")
        if response.isdigit():
            response = int(response)

            if response in range(1, len(question['options']) + 1):
                return response - 1
        print('Invalid input. Please enter a number between 1 and',
              len(question['options']))


# function to grade the question

def grade_question(question, answer):
    return question['options'][answer] == question['answer']


# function to take the quiz

def take_quiz(questions):
    score = 0
    for question in questions:
        display_questions(question)
        answer = get_answer(question)
        if grade_question(question, answer):
            score += 1
            print('Correct!')
        else:
            print('Incorrect!')
    print(f'You got {score} out of {len(questions)} questions correct.')


questions = [
    {
        'prompt': 'What is the capital of France?',
        'options': ['London', 'Paris', 'Berlin'],
        'answer': 'Paris'
    },
    {
        'prompt': 'What is the Fastest Land Animal?',
        'options': ['Elephant', 'Dog', 'Cheetah'],
        'answer': 'Cheetah'
    },
    {
        'prompt': 'What is the capital of Germany?',
        'options': ['London', 'Paris', 'Berlin'],
        'answer': 'Berlin'
    },
    {
        'prompt': 'Who is the founder of Apple?',
        'options': ['Larry Page', 'Elon Musk', 'Steve Jobs'],
        'answer': 'Steve Jobs'
    },
    {
        'prompt': 'Who is the richest man in the world?',
        'options': ['Jeff Bezoz', 'Gautam Adani', 'Elon Musk'],
        'answer': 'Elon Musk'
    },
    {
        'prompt': 'What is the founder of FaceBook?',
        'options': ['Eduardo Savarin', 'Winkelvos Twins', 'Mark Zuckerberg'],
        'answer': 'Mark Zuckerberg'
    },
    {
        'prompt': 'Who is the Prime minister of India currently?',
        'options': ['Mahatma Gandhi', 'Jawaharlal Nehru', 'Narendra Modi'],
        'answer': 'Narendra Modi'
    },
    {
        'prompt': 'C is a object oriented Language?',
        'options': [True, False],
        'answer': False
    },
]

take_quiz(questions)
