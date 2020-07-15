n = int(input("Please enter a number: "))
prime_num = []
for i in range(2, n+1):
    count_1 = 0
    for ii in range(1, i):
        if i % ii == 0:
            count_1 += 1
    if count_1 <= 1:
        prime_num.append(i)

print(prime_num)