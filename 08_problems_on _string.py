# name = input("Enter your name \n")
# print("Good evening," + name)

letter = '''Hi |Name|
        You are selected 
         on |Date| '''

name = input("Ener your Name")
date = input("enter today's date")

letter = letter.replace("|Name|",name)
letter = letter.replace("|Date|",date)

print(letter)