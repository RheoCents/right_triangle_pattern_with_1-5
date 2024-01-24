#Print the following pattern
#1
#2 2
#3 3 3
#4 4 4 4 
#5 5 5 5 5
for i in range (4):
    if i == 1:
        print(i)
    if i == 2:
        for _ in range (1):
            contant_for_second_line = 2
            print(i,str(contant_for_second_line))