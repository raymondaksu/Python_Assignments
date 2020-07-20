def FizzBuzz(number=range(1,101)):
    last_file = []
    for i in number:
        if i % 3 == 0 and (not i % 5 == 0):
            last_file.append("Fizz")
        elif i % 5 == 0 and (not i % 3 == 0):
            last_file.append("Buzz")
        elif i % 5 == 0 and i % 3 == 0:
            last_file.append("FizzBuzz")
        else:
            last_file.append(i)
    return print(*last_file, sep='\n')

FizzBuzz()







#def not_string(word):
#    return (lambda word: word if word[:3] == 'not' else 'not '+word)(word)
