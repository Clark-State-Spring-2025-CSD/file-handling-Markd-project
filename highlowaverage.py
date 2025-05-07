#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file:

T = 0
A = 0
H = 0
L = 10000000000

with open("numbers.txt", "r") as i:
    for x in i:
        Number = float(x)
        T += Number
        A += 1
        if Number > H:
            H = Number
        if Number < L:
            L = Number

Av = T / A

print(f"The total of all numbers is {T}")
print(f"The average of all numbers is {Av}")
print(f"The highest number is {H}")
print(f"The lowest number is {L}")