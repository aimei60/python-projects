print("Welcome to the Quiz Game!")
count = 0

question_one = input("1. What is the deepest ocean trench? ")
if question_one == "mariana trench":
    count += 1
    print("Correct!") 
else:
    print("Incorrect!")
    
question_two = input("2. What is the largest island in the world? ")
if question_two == "greenland":
    count+=1
    print("Correct!") 
else:
    print("Incorrect!")

question_three = input("3. Who wrote the famous novel To Kill a Mockingbird? ")
if question_three == "harper lee":
    count+=1
    print("Correct!") 
else:
    print("Incorrect!")
    
question_four = input("4. What is the name of the scale used to measure spiciness of peppers? ")
if question_four == "scoville scale":
    count+=1
    print("Correct!") 
else:
    print("Incorrect!")   
    
question_five = input("5. What is the capital of Australia? ")
if question_five == "canberra":
    count+=1
    print("Correct!") 
else:
    print("Incorrect!") 
    
    
print("Your score is:", count, "out of 5")
percentage = (count / 5) * 100
print("The percentage of your score is", percentage, "%")
