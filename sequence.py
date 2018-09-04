n = int(input("Enter the length of the sequence: ")) # Do not change this line

number1 = 0
number2 = 1
number3 = 2
summ = 0


print(number2)
print(number3)

for i in range(n-2):
    summ = number1 + number2 + number3
    
    
    print(summ)
    number1 = number2
    number2 = number3
    number3 = summ              
