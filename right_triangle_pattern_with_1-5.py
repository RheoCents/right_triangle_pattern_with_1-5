#Print the following pattern
#1
#2 2
#3 3 3
#4 4 4 4 
#5 5 5 5 5
print('For this, we will print a figure of right triangle using the print function and numbers 1-5')
for number_value in range(6):
    print('')
    for _ in range(number_value):
        print (number_value, end=" ") 

