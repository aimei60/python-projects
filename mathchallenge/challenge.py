import time

print("Are you ready for the maths challenge? You will be timed and need to answer all 4 of the questions correctly with the fastest time.")

running = True
seconds = 0
end_quiz = False

while running:
    start_time = time.time()
    question_1 = input("What is 8 + 5? ")
    if question_1 == "q":
        end_quiz = True
        break
    
    if question_1 == "13":
        print("Correct! Next Question")
        while True:
            question_2 = input("If a shirt costs $20 and is on sale for 30% off, what is the sale price? ")
            if question_2 == "q":
                end_quiz = True
                break  
              
            if question_2 == "14":
                print("Correct! Next Question")
                while True:
                    question_3 = input("Solve for x: 2x + 5 = 17. What is x? ")
                    if question_3 == "q":
                        end_quiz = True
                        break
                    
                    if question_3 == "6":
                        print("Correct! Next Question")
                        while True:
                            question_4 = input("What is the value of π (pi) rounded to two decimal places? ")
                            if question_4 == "q":
                                end_quiz = True
                                break
                            
                            if question_4 == "3.14":
                                end_time = time.time()
                                seconds += round(end_time - start_time)
                                running = False
                                end_quiz = True
                                print("Correct!")
                                mins = seconds // 60
                                secs = seconds % 60
                                print(f"You spent {mins} minutes and {secs} seconds in this challenge!")
                                break
                            else:
                                print("Incorrect! Try again!")
                        if end_quiz:
                            break
                    else:
                        print("Incorrect! Try again!")
                if end_quiz:
                    break
            else:
                print("Incorrect! Try again!")
        if end_quiz:
                    break
    else:
        print("Incorrect! Try again!")
