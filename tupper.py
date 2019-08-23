question_database = {
    'question1': ['How many legs does an octopus have?','One leg','Two legs','Four legs','Eight legs'],
    'question2': ['How many fingers does a hand have?','Two fingers','Five fingers','Three fingers','Six fingers'],
    'question3': ['How many sides does a cube have?','Four','Five','Six','Seven']
}


def question(q_pos,a_pos):
    name = 'question'+str(q_pos)
    print(question_database[name][0])
    for i in range(1,5):
        print(i,end='')
        print('.',end=' ')
        print(question_database[name][i])

    answer = int(input('Your answer: '))
    print()
    if answer == a_pos:
        print('Hura!!!!')
        correct = 1
        return correct
    else:
        print('Not a correct answer :’(')
        correct = 0
        return correct


correct = question(1,4)+question(2,2)+question(3,3)
print('The number of your correct answers are: ', correct)
print('The percentage of correct answers: ',correct/3*100,'%')





