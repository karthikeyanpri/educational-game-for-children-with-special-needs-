# Educational Game for Grade 1 Students

# Import necessary modules
import random

# Create a list of color matching questions
color_questions = [
    "What color is the apple?",
    "What color is the banana?",
    "What color is the car?",
    "What color is the dog?",
    "What color is the sky?"
]

# Create a list of answers for the color matching questions
color_answers = [
    "red",
    "yellow",
    "blue",
    "brown",
    "blue"
]

# Create a list of shape matching questions
shape_questions = [
    "What shape is the ball?",
    "What shape is the book?",
    "What shape is the cake?",
    "What shape is the hat?",
    "What shape is the apple?"
]

# Create a list of answers for the shape matching questions
shape_answers = [
    "round",
    "rectangle",
    "circle",
    "cone",
    "round"
]

# Create a list of counting questions
counting_questions = [
    "How many fingers do you have?",
    "How many legs does a dog have?",
    "How many wheels does a bike have?",
    "How many days in a week?",
    "How many months in a year?"
]

# Create a list of answers for the counting questions
counting_answers = [
    "5",
    "4",
    "2",
    "7",
    "12"
]

# Print a welcome message
print("Welcome to the Educational Game for Grade 1 Students!")

# Ask the user to select a subject (color, shape, or counting)
subject = input("Please select a subject (color, shape, or counting): ")

# Use an if-elif-else statement to determine which set of questions to use based on the user's selection
if subject.lower() == "color":
    question_list = color_questions
    answer_list = color_answers
elif subject.lower() == "shape":
    question_list = shape_questions
    answer_list = shape_answers
elif subject.lower() == "counting":
    question_list = counting_questions
    answer_list = counting_answers
else:
    print("Invalid selection. Please try again.")
    exit()

# Use a for loop to iterate through the selected list of questions
score = 0
for i in range(len(question_list)):
    # Print the current question
    print(question_list[i])
    # Get the user's answer
    user_answer = input("Your answer: ")
    # Check if the user's answer is correct
    if user_answer.lower() == answer_list[i].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is", answer_list[i])

# Print the final score
print("Your final score is", score, "out of", len(question_list))
