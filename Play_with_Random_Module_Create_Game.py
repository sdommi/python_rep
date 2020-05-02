def calulateAnswer(lhs,rhs,operator):
    if operator == "+":
        return lhs + rhs
    if operator == "-":
        return lhs - rhs
    if operator == "/":
        return lhs / rhs
    if operator == "*":
        return lhs * rhs
    raise Exception("Unknow Operaor")
from random import randint
def generateQuestion():
    
    #operators="""+","*","-","/"]
    #or
    operators="+*-/"
    opeIndex = randint(0,len(operators)-1)
    operator = operators[opeIndex]
    lhs=randint(0,10)
    rhs=randint(0,10)
    while(rhs == 0 and operator == "/"):
        rhs=randint(0,10)
    return lhs,rhs,operator
question = generateQuestion()
correctAnswer = calculateAnswers(question[0],question[1],question[2])
playerAnswer = input("{0} {2} {1} =".format(question[0],question[1],question[2]))
if (playerAnswer == str(correctAnswer)):
    print("Guess is Correct")
else:
    print("Guss is Not Correct")
