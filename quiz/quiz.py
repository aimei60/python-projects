def questions(question, correct_answer):
    response = input(question)
    if response == correct_answer.lower():
        print("Correct")
        return 1
    else:
        print("Incorrect")
        return 0

def quiz():
    print("Welcome to the Quiz Game!")
    count = 0
    quiz_questions = [("1. What is the deepest ocean trench? ", "mariana trench"),
                ("2. What is the largest island in the world? ", "greenland"),
                ("3. Who wrote the famous novel To Kill a Mockingbird? ", "harper lee"),
                ("4. What is the name of the scale used to measure spiciness of peppers? ", "scoville scale"),
                ("5. What is the capital of Australia? ", "canberra")
                ]
    
    for question, answer in quiz_questions:
        count += questions(question, answer)
    
    print("Your score is:", count, "out of 5")
    percentage = (count / 5) * 100
    print("The percentage of your score is", percentage, "%")

quiz()

