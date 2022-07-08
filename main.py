print('Welcome to TubeLight Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=6
 
if  answer.lower()=='yes':
    answer=input('Question 1: What is your Favourite programming language?')
    if answer.lower()=='python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: Do you follow any author on TubeLight? ')
    if answer.lower()=='yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: Who is the founder of Python?')
    if answer.lower()=='Guido van Rossum':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 4: What is the name of your favourite website for learning Python?')
    if answer.lower()=='w3schools':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 5: Who created TubeLight?')
    if answer.lower()=='TinTinNyamaz':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    M = input("Want to talk to us? (yes/no) ")
    print(M)
    if "yes":
        print("contact: ( tnyamadzuda@gmail.com ) for more.")
    print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
    mark=(score/total_questions)*100
    print('Marks obtained:',mark)
    print('BYE!')
