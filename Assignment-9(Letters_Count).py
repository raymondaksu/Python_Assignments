sentence = input("Enter a sentence: ").split()
letter_list = []
for i in sentence:
    for j in i:
        if j.isalpha():
            letter_list.append(j)
my_dict = {}
set_list = set(letter_list)
for i in set_list:
    counter = letter_list.count(i)
    my_dict[i] = counter

print(my_dict)




