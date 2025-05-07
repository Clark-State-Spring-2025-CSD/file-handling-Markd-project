#For this assignment use the words.txt file.
#Read in all the words. Count how many are palindromes, or words that are spelled the same forwads and backwards.
#For example, wow is a paldindrome.
#A different file wile be used for grading.
#Correct answer for this file: 

Pal = 0
Row =""

with open("words.txt", "r") as i:
    for z in i:
        Wor = z.strip()
        Row = Wor[::-1]
        if Wor == Row:
            Pal += 1

print(f"There are {Pal} palindromes")