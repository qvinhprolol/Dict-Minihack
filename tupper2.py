question_database = {
    'question1': ['How many legs does an octopus have?','One leg','Two legs','Four legs','Eight legs'],
    'question2': ['How many fingers does a hand have?','Two fingers','Five fingers','Three fingers','Six fingers'],
    'question3': ['How many sides does a cube have?','Four','Five','Six','Seven']
}


def correct(x):
    score = 0
    if x == 3 :
        print("correct")
        score +=1
    
    else:
        print("wrong")
    
    return score


print(correct(3))
