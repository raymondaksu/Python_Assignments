ramazan=True
while ramazan==True:
    number = input("Please enter a positive number: ")
    number_count = len(number)
    summ = 0
    if number.isdigit() == False:
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    else:
        for i in range(number_count):
            summ += int(number[i])**len(number)
        if summ == int(number):
            print(f"{number} is an Armstrong number")
        else:
            print(f"{number} is not an Armstrong number")
    devam = input('Devam etmek istiyor musunuz (y/n) : ')
    if devam=='y':
        ramazan=True
    else:
        ramazan=False


