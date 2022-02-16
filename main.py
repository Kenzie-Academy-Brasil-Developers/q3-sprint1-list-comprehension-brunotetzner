def list_comprehension_exercise_1():
    return [n for n in range(11)]

print(list_comprehension_exercise_1())



def list_comprehension_exercise_2():
    return [ n for n in range(22) if n % 2 == 0 or n % 3 == 0]

print(list_comprehension_exercise_2())



def list_comprehension_exercise_3():
    return [ n for n in range(-5,32) if n % 2 != 0 and n % 5 != 0]

print(list_comprehension_exercise_3())



def list_comprehension_exercise_4():
    return [n*n for n in range(11)]


print(list_comprehension_exercise_4())


def list_comprehension_exercise_5(sentence):

     return [sentence[index] for index in range(len(sentence)) if sentence[index].isupper() == True ]

print(list_comprehension_exercise_5('O Rato Rui Gosta De QueiJo FresQuiNho'))


def list_comprehension_exercise_6(sentence):

    return [word for word in sentence.split() if word[0] == 'r' and len(word)>3]
    
print(list_comprehension_exercise_6('o rato rui roeu a roupa do rei de roma'))
