score = 0
questions = {
    "Who is the owner of Tesla? : ": "Elon Musk", 
    "Largest Country in the world?  : " : "Russia",
    "Biggest State in India?  : " : "Rajasthan",
    "Capital of India?  : " : "Delhi",
    "Capital of Maharashtra? : " : "Mumbai"
    }


# <==== Main ====>

print('Welcome to the quiz!')
print('You will get 10 questions')
print('Each correct answer gets 1 point, wrong answer gets 0 points')
print('Lets Begin!!!')
print('\n')

for i in questions.keys():
    print('\n')
    user = input(i)
    if(user == questions[i]):
        print("Correct Answer!")
        score = score + 1
        print('Your Score: ', score)
    else:
        print('Wrong Answer :(')

print("Final Score: ", score)
